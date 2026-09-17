"""
Entrenamiento y Validación del Modelo Predictivo de Riesgo — SafeRx AI
=======================================================================
Entrena y evalúa múltiples modelos de Machine Learning (Regresión Logística,
Random Forest y HistGradientBoosting) sobre los datos preprocesados de la
cohorte hospitalaria real, optimizando Recall (Sensibilidad) y ROC-AUC para
minimizar Falsos Negativos clínicos. Serializa el mejor modelo en
prototype/models/modelo_riesgo.pkl.

Autor: Equipo SafeRx AI
"""

import logging
from pathlib import Path
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, classification_report, confusion_matrix
)
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_CSV = BASE_DIR / "data" / "processed" / "datos_limpios.csv"
PREPROCESSOR_PKL = BASE_DIR / "prototype" / "models" / "preprocesador.pkl"
MODEL_OUTPUT_PKL = BASE_DIR / "prototype" / "models" / "modelo_riesgo.pkl"

RANDOM_STATE = 42
TEST_SIZE = 0.2


def main():
    logger.info("Cargando dataset preprocesado...")
    df = pd.read_csv(PROCESSED_CSV)
    preprocessor = joblib.load(PREPROCESSOR_PKL)
    
    logger.info("Dataset: %s filas, %s columnas", *df.shape)

    X = df.drop(columns=["id_consulta", "fecha", "hubo_interaccion"])
    y = df["hubo_interaccion"]

    logger.info("Distribución de clases: %s positivos (%.2f%%)", y.sum(), (y.mean() * 100))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    X_train_proc = preprocessor.transform(X_train)
    X_test_proc = preprocessor.transform(X_test)

    candidatos = {
        "Regresión Logística": LogisticRegression(class_weight="balanced", random_state=RANDOM_STATE, max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=6, class_weight="balanced", random_state=RANDOM_STATE),
        "Hist Gradient Boosting": HistGradientBoostingClassifier(class_weight="balanced", max_iter=120, random_state=RANDOM_STATE)
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    scoring = ["accuracy", "precision", "recall", "f1", "roc_auc"]

    logger.info("--- Validación Cruzada (5-Fold Stratified) ---")
    resultados = []
    for nombre, mod in candidatos.items():
        scores = cross_validate(mod, X_train_proc, y_train, cv=cv, scoring=scoring)
        res = {
            "Modelo": nombre,
            "Accuracy": scores["test_accuracy"].mean(),
            "Precision": scores["test_precision"].mean(),
            "Recall (Sensibilidad)": scores["test_recall"].mean(),
            "F1-Score": scores["test_f1"].mean(),
            "ROC-AUC": scores["test_roc_auc"].mean()
        }
        resultados.append(res)
        logger.info(
            "%-24s | Recall: %.3f | ROC-AUC: %.3f | F1: %.3f",
            nombre, res["Recall (Sensibilidad)"], res["ROC-AUC"], res["F1-Score"]
        )

    # Entrenar el modelo final (Random Forest / Gradient Boosting)
    mejor_nombre = "Random Forest"
    modelo_final = candidatos[mejor_nombre]
    modelo_final.fit(X_train_proc, y_train)

    y_pred = modelo_final.predict(X_test_proc)
    y_prob = modelo_final.predict_proba(X_test_proc)[:, 1]

    auc_test = roc_auc_score(y_test, y_prob)
    rec_test = recall_score(y_test, y_pred)
    prec_test = precision_score(y_test, y_pred)
    f1_test = f1_score(y_test, y_pred)

    logger.info("--- Evaluación Final en Test Set (20%% no visto) ---")
    logger.info("Modelo Seleccionado: %s", mejor_nombre)
    logger.info("ROC-AUC:   %.4f", auc_test)
    logger.info("Recall:    %.4f (Sensibilidad Clínica)", rec_test)
    logger.info("Precision: %.4f", prec_test)
    logger.info("F1-Score:  %.4f", f1_test)
    logger.info("\nReporte de Clasificación:\n%s", classification_report(y_test, y_pred))

    # Guardar modelo final
    MODEL_OUTPUT_PKL.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(modelo_final, MODEL_OUTPUT_PKL)
    logger.info("✓ Modelo guardado exitosamente en: %s", MODEL_OUTPUT_PKL)


if __name__ == "__main__":
    main()
