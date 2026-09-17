"""
Pipeline de preprocesamiento — Detección de interacciones medicamentosas graves
================================================================================
Carga datos clínicos desde SQLite, construye la variable objetivo
(hubo_interaccion), limpia y transforma los datos, y guarda tanto el dataset
procesado como el ColumnTransformer entrenado para su uso posterior
(p. ej. en la app de Streamlit).

Autor: Ana
"""

import logging
from pathlib import Path
import sqlite3

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ---------------------------------------------------------------------------
# Configuración (Rutas dinámicas respecto a la raíz del proyecto)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "hospital.db"
OUTPUT_CSV = BASE_DIR / "data" / "processed" / "datos_limpios.csv"
OUTPUT_PIPELINE = BASE_DIR / "prototype" / "models" / "preprocesador.pkl"

RANDOM_STATE = 42
TEST_SIZE = 0.2
MIN_AGE, MAX_AGE = 0, 110
POLYFARMACIA_THRESHOLD = 3
WEEKEND_DAYS = {5, 6}  # sábado, domingo

NUM_FEATURES = ["edad", "num_medicamentos", "mes_consulta"]
CAT_FEATURES = ["genero", "condiciones_previas", "especialidad"]

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 1-2. Carga de datos
# ---------------------------------------------------------------------------
def cargar_datos(db_path: Path) -> pd.DataFrame:
    """Extrae consultas con datos de paciente y médico, y etiqueta interacciones graves."""
    if not db_path.exists():
        raise FileNotFoundError(f"No se encontró la base de datos en {db_path}")

    query_base = """
        SELECT
            c.id_consulta, p.edad, p.genero, p.condiciones_previas,
            m.especialidad, c.fecha,
            COUNT(r.id_medicamento) AS num_medicamentos
        FROM Consultas c
        JOIN Pacientes p ON c.id_paciente = p.id_paciente
        JOIN Medicos m ON c.id_medico = m.id_medico
        LEFT JOIN Recetas r ON c.id_consulta = r.id_consulta
        GROUP BY c.id_consulta
    """

    # NOTA (fix): la versión original solo comparaba
    # (r1.id_medicamento = i.id_medicamento_1 AND r2.id_medicamento = i.id_medicamento_2),
    # lo que ignoraba interacciones registradas en el orden inverso de fármacos.
    # Se añade el OR para capturar ambas direcciones del par.
    query_peligrosas = """
        SELECT DISTINCT c.id_consulta
        FROM Consultas c
        JOIN Recetas r1 ON c.id_consulta = r1.id_consulta
        JOIN Recetas r2 ON c.id_consulta = r2.id_consulta AND r1.id_receta < r2.id_receta
        JOIN Interacciones i
          ON (r1.id_medicamento = i.id_medicamento_1 AND r2.id_medicamento = i.id_medicamento_2)
          OR (r1.id_medicamento = i.id_medicamento_2 AND r2.id_medicamento = i.id_medicamento_1)
    """

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql(query_base, conn)
        df_peligrosas = pd.read_sql(query_peligrosas, conn)

    df_peligrosas["hubo_interaccion"] = 1
    df = df.merge(df_peligrosas, on="id_consulta", how="left")
    df["hubo_interaccion"] = df["hubo_interaccion"].fillna(0).astype(int)

    logger.info("Datos cargados: %s filas, %s columnas", *df.shape)
    return df


# ---------------------------------------------------------------------------
# 3-9. Limpieza (nulos, duplicados, tipos, texto, outliers)
# ---------------------------------------------------------------------------
def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    logger.info("Nulos por columna antes de limpiar:\n%s", df.isnull().sum())

    # Nulos: valor por defecto explícito antes de eliminar residuales
    df["condiciones_previas"] = df["condiciones_previas"].fillna("Ninguna")
    df = df.dropna()

    # Duplicados
    df = df.drop_duplicates(subset="id_consulta")

    # Tipos
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = df.dropna(subset=["fecha"])

    # Texto
    for col in ("genero", "especialidad", "condiciones_previas"):
        df[col] = df[col].str.lower().str.strip()

    # Outliers de edad (límites lógicos)
    antes = len(df)
    df = df[(df["edad"] >= MIN_AGE) & (df["edad"] <= MAX_AGE)]
    logger.info("Outliers de edad eliminados: %d filas", antes - len(df))

    return df


# ---------------------------------------------------------------------------
# 12-13. Feature engineering
# ---------------------------------------------------------------------------
def generar_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["mes_consulta"] = df["fecha"].dt.month
    df["es_fin_de_semana"] = df["fecha"].dt.dayofweek.isin(WEEKEND_DAYS).astype(int)
    df["es_polifarmacia"] = (df["num_medicamentos"] >= POLYFARMACIA_THRESHOLD).astype(int)
    return df


# ---------------------------------------------------------------------------
# 10-11, 17. Pipeline de transformación
# ---------------------------------------------------------------------------
def construir_preprocesador() -> ColumnTransformer:
    num_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    cat_transformer = Pipeline(
        steps=[("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]
    )

    return ColumnTransformer(
        transformers=[
            ("num", num_transformer, NUM_FEATURES),
            ("cat", cat_transformer, CAT_FEATURES),
        ],
        remainder="passthrough",  # conserva es_fin_de_semana y es_polifarmacia
    )


# ---------------------------------------------------------------------------
# Orquestación
# ---------------------------------------------------------------------------
def main() -> None:
    df = cargar_datos(DB_PATH)
    df = limpiar_datos(df)
    df = generar_features(df)

    # 14. Selección de características
    X = df.drop(columns=["id_consulta", "fecha", "hubo_interaccion"])
    y = df["hubo_interaccion"]

    # 15. Balance de clases (informativo — decide class_weight/SMOTE en el modelo)
    logger.info("Balance de clases:\n%s", (y.value_counts(normalize=True) * 100).round(2))

    # 16. División train/test
    stratify_option = y if y.value_counts().min() >= 2 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=stratify_option
    )

    # 10-11, 17. Ajuste del preprocesador (solo con train, evita fuga de datos)
    preprocessor = construir_preprocesador()
    X_train_procesado = preprocessor.fit_transform(X_train)
    X_test_procesado = preprocessor.transform(X_test)
    logger.info("Forma final de X_train procesado: %s", X_train_procesado.shape)

    # 18. Guardado
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PIPELINE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_CSV, index=False)
    joblib.dump(preprocessor, OUTPUT_PIPELINE)

    logger.info("Preprocesamiento finalizado. Datos y pipeline guardados correctamente.")


if __name__ == "__main__":
    main()
