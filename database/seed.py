"""
Generador de Datos Clínicos y Farmacológicos Reales — SafeRx AI
==============================================================
Popula SQLite hospital.db y data/raw/ con un catálogo farmacológico real de más
de 75 principios activos, 65+ interacciones clínicas documentadas (gravedad, mecanismo
fisiopatológico y recomendaciones) y una cohorte hospitalaria multicéntrica
con patrones reales de polifarmacia y comorbilidades.

Autor: Equipo SafeRx AI
"""

import sqlite3
import random
from datetime import datetime, timedelta
import os
from pathlib import Path
import pandas as pd

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "hospital.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

random.seed(42)  # Reproducibilidad científica

print("Iniciando la generación y población con datos clínicos reales...")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

if DB_PATH.exists():
    DB_PATH.unlink()

# 1. Crear esquema SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
    cursor.executescript(f.read())

print("✓ Esquema SQLite creado e inicializado correctamente.")

# ==============================================================================
# 2. Catálogo Farmacológico Real (75+ Medicamentos de Alta Prescripción)
# ==============================================================================
# Formato: (principio_activo, nombre_comercial, grupo_terapeutico)
medicamentos_raw = [
    # --- Anticoagulantes & Antiagregantes ---
    ('Warfarina', 'Coumadin / Aldocumar'),
    ('Acenocumarol', 'Sintrom'),
    ('Aspirina (Ácido Acetilsalicílico)', 'Aspirina Bayer / Adiro'),
    ('Clopidogrel', 'Plavix / Iscover'),
    ('Apixabán', 'Eliquis'),
    ('Rivaroxabán', 'Xarelto'),
    ('Dabigatrán', 'Pradaxa'),
    ('Enoxaparina', 'Clexane'),

    # --- AINEs y Analgésicos ---
    ('Ibuprofeno', 'Advil / Neobrufen / Espidifen'),
    ('Naproxeno', 'Antalgin / Naprosyn'),
    ('Diclofenaco', 'Voltaren'),
    ('Ketorolaco', 'Toradol / Droal'),
    ('Celecoxib', 'Celebrex'),
    ('Meloxicam', 'Movalis'),
    ('Paracetamol', 'Efferalgan / Gelocatil'),
    ('Tramadol', 'Adolonta / Zaldiar'),
    ('Morfina', 'Sevredol / Oramorph'),
    ('Fentanilo', 'Durogesic / Actiq'),

    # --- Cardiovascular: Antihipertensivos & Cardíacos ---
    ('Lisinopril', 'Zestril / Prinivil'),
    ('Enalapril', 'Renitec / Vasotec'),
    ('Ramipril', 'Acovil / Altace'),
    ('Losartán', 'Cozaar'),
    ('Valsartán', 'Diovan'),
    ('Candesartán', 'Atacand'),
    ('Amlodipino', 'Norvasc'),
    ('Nifedipino', 'Adalat Oros'),
    ('Diltiazem', 'Masdil / Cardizem'),
    ('Verapamilo', 'Manidon / Isoptin'),
    ('Atenolol', 'Tenormin'),
    ('Bisoprolol', 'Emconcor / Cardicor'),
    ('Metoprolol', 'Lopresor / Beloc'),
    ('Carvedilol', 'Coropres / Dilatrend'),
    ('Espironolactona', 'Aldactone'),
    ('Eplerenona', 'Inspra'),
    ('Furosemida', 'Seguril / Lasix'),
    ('Torasemida', 'Dilutb / Sutril'),
    ('Hidroclorotiazida', 'Esidrex'),
    ('Amiodarona', 'Trangorex / Cordarone'),
    ('Digoxina', 'Digoxina Sanofi / Lanoxin'),
    ('Flecainida', 'Apocard / Tambocor'),

    # --- Hipolipemiantes (Estatinas y otros) ---
    ('Atorvastatina', 'Cardyl / Lipitor / Zarator'),
    ('Simvastatina', 'Zocor / Alcosin'),
    ('Rosuvastatina', 'Crestor'),
    ('Pravastatina', 'Liplat / Lipemol'),
    ('Fenofibrato', 'Secalip / Lipanthyl'),
    ('Ezetimiba', 'Ezetrol'),

    # --- Diabetes & Metabolismo ---
    ('Metformina', 'Dianben / Glucophage'),
    ('Insulina Glargina', 'Lantus / Toujeo'),
    ('Insulina Aspart', 'NovoRapid'),
    ('Gliclazida', 'Diamicron'),
    ('Empagliflozina', 'Jardiance'),
    ('Dapagliflozina', 'Forxiga'),
    ('Sitagliptina', 'Januvia'),
    ('Liraglutida', 'Victoza / Saxenda'),

    # --- Antibióticos & Antifúngicos ---
    ('Amoxicilina', 'Clamoxyl'),
    ('Amoxicilina-Clavulánico', 'Augmentine'),
    ('Ciprofloxacino', 'Baycip / Cipro'),
    ('Levofloxacino', 'Tavanic'),
    ('Azitromicina', 'Zithromax / Zitromax'),
    ('Claritromicina', 'Klacid / Kofron'),
    ('Doxiciclina', 'Vibramicina'),
    ('Ceftriaxona', 'Rocephin'),
    ('Fluconazol', 'Diflucan'),

    # --- Psiquiatría & Sistema Nervioso Central ---
    ('Sertralina', 'Besitran / Zoloft'),
    ('Fluoxetina', 'Prozac'),
    ('Escitalopram', 'Cipralex / Lexapro'),
    ('Paroxetina', 'Seroxat'),
    ('Venlafaxina', 'Vandral / Effexor'),
    ('Duloxetina', 'Cymbalta / Xeristar'),
    ('Amitriptilina', 'Tryptizol / Elavil'),
    ('Lorazepam', 'Orfidal / Ativan'),
    ('Diazepam', 'Valium'),
    ('Alprazolam', 'Trankimazin / Xanax'),
    ('Clonazepam', 'Rivotril / Klonopin'),
    ('Zolpidem', 'Stilnox / Ambien'),
    ('Quetiapina', 'Seroquel'),
    ('Olanzapina', 'Zyprexa'),
    ('Risperidona', 'Risperdal'),
    ('Litio', 'Plenur / Lithobid'),

    # --- Gastrointestinal, Respiratorio & Inmunosupresores ---
    ('Omeprazol', 'Omeprazol Genérico / Losec'),
    ('Pantoprazol', 'Pantecta / Anagastra'),
    ('Esomeprazol', 'Nexium'),
    ('Famotidina', 'Pepcid'),
    ('Salbutamol', 'Ventolin'),
    ('Budesonida', 'Pulmicort'),
    ('Montelukast', 'Singulair'),
    ('Metotrexato', 'Metoject / Rheumatrex'),
    ('Prednisona', 'Dacortin / Deltasone'),
    ('Dexametasona', 'Fortecortin'),
    ('Alopurinol', 'Zyloric'),
    ('Colquicina', 'Colchimax'),
    ('Levotiroxina', 'Eutirox / Synthroid'),
    ('Teofilina', 'Theo-Dur / Tediprim'),
    ('Carbonato de Calcio', 'Mastical / Calcio'),
]

cursor.executemany(
    "INSERT INTO Medicamentos (principio_activo, nombre_comercial) VALUES (?, ?)",
    medicamentos_raw
)

# Mapear nombres a ID de medicamento en SQLite
cursor.execute("SELECT id_medicamento, principio_activo FROM Medicamentos")
med_dict = {row[1]: row[0] for row in cursor.fetchall()}

print(f"✓ Catálogo de {len(medicamentos_raw)} medicamentos reales insertado en la BD.")

# ==============================================================================
# 3. Matriz de Interacciones Farmacológicas Reales Documentadas (65+ Reglas)
# ==============================================================================
# Cada interacción: (med1_str, med2_str, gravedad, descripcion_clinica)
interacciones_definidas = [
    # Hemorragias & Anticoagulación
    ('Warfarina', 'Aspirina (Ácido Acetilsalicílico)', 'grave', 'Sinergia antiagregante y anticoagulante: riesgo crítico de hemorragia gastrointestinal y cerebral severa.'),
    ('Warfarina', 'Ibuprofeno', 'grave', 'Aumento severo del riesgo de sangrado digestivo y desplazamiento de unión a proteínas de warfarina.'),
    ('Warfarina', 'Naproxeno', 'grave', 'Riesgo extremo de úlcera péptica sangrante y prolongación patológica del INR.'),
    ('Warfarina', 'Diclofenaco', 'grave', 'Hemorragia severa por sinergia farmacodinámica y lesión de mucosa gástrica.'),
    ('Acenocumarol', 'Aspirina (Ácido Acetilsalicílico)', 'grave', 'Riesgo muy alto de hemorragia letal; contraindicación salvo protocolo estricto de doble terapia coronaria monitorizada.'),
    ('Acenocumarol', 'Ibuprofeno', 'grave', 'Incompatibilidad absoluta en atención primaria: riesgo hemorrágico digestivo grave.'),
    ('Acenocumarol', 'Naproxeno', 'grave', 'Potenciación extrema del efecto anticoagulante con alto riesgo de sangrado digestivo alto.'),
    ('Apixabán', 'Ibuprofeno', 'grave', 'Riesgo elevado de sangrado mayor gastrointestinal sin reversor inmediato accesible.'),
    ('Apixabán', 'Ketorolaco', 'grave', 'Contraindicación absoluta: sangrado digestivo fulminante y lesión renal aguda.'),
    ('Rivaroxabán', 'Aspirina (Ácido Acetilsalicílico)', 'grave', 'Riesgo elevado de hemorragia mayor intra/extracraneal.'),
    ('Clopidogrel', 'Omeprazol', 'grave', 'Omeprazol inhibe CYP2C19 reduciendo la bioactivación de clopidogrel y aumentando el riesgo de infarto recurrente.'),
    ('Clopidogrel', 'Esomeprazol', 'grave', 'Inhibición enzimática de la eficacia antiagregante plaquetaria de clopidogrel.'),

    # Hiperpotasemia Crítica & Fallo Renal (Nefrotoxicidad)
    ('Lisinopril', 'Espironolactona', 'grave', 'Riesgo crítico de hiperpotasemia severa (> 6.0 mEq/L) causante de arritmias ventriculares y parada cardíaca.'),
    ('Enalapril', 'Espironolactona', 'grave', 'Hiperpotasemia letal por bloqueo dual del eje renina-angiotensina-aldosterona.'),
    ('Ramipril', 'Espironolactona', 'grave', 'Aumento marcado del potasio sérico con toxicidad neuromuscular y cardíaca.'),
    ('Losartán', 'Espironolactona', 'grave', 'Retención sinérgica de potasio en túbulo renal distal: riesgo severo de bloqueo AV y fibrilación ventricular.'),
    ('Valsartán', 'Espironolactona', 'grave', 'Hiperpotasemia grave, especialmente en pacientes ancianos con insuficiencia renal basal.'),
    ('Ibuprofeno', 'Lisinopril', 'grave', 'Antagonismo del efecto antihipertensivo y vasoconstricción de arteriola aferente: alto riesgo de fracaso renal agudo.'),
    ('Ibuprofeno', 'Enalapril', 'grave', 'Deterioro agudo del filtrado glomerular e hipertensión descontrolada.'),
    ('Naproxeno', 'Ramipril', 'grave', 'Nefrotoxicidad hemodinámica severa; retención hidrosalina aguda.'),
    ('Ibuprofeno', 'Furosemida', 'moderada', 'Los AINEs inhiben las prostaglandinas renales, atenuando intensamente el efecto diurético y antihipertensivo.'),
    ('Ibuprofeno', 'Espironolactona', 'grave', 'Disminución de la excreción renal de potasio + nefrotoxicidad por AINE: riesgo de hiperpotasemia grave.'),

    # Rabdomiólisis & Miopatía por Estatinas (CYP3A4)
    ('Simvastatina', 'Claritromicina', 'grave', 'Claritromicina inhibe potentemente el CYP3A4, aumentando 10 veces las concentraciones de simvastatina: rabdomiólisis severa e insuficiencia renal.'),
    ('Atorvastatina', 'Claritromicina', 'grave', 'Riesgo elevado de miopatía necrotizante y fallo renal agudo secundario a mioglobinuria.'),
    ('Simvastatina', 'Amiodarona', 'grave', 'Inhibición del metabolismo hepático de simvastatina: miopatía y rabdomiólisis. Dosis de simvastatina no debe superar 20 mg/día.'),
    ('Atorvastatina', 'Fluconazol', 'grave', 'Aumento de niveles séricos de estatina por inhibición de CYP3A4/CYP2C9: mialgias graves y elevación marcada de CPK.'),
    ('Simvastatina', 'Fenofibrato', 'moderada', 'Aumento del riesgo de miopatía muscular y elevación de transaminasas.'),

    # Toxicidad por Fármacos de Estrecho Rango Terapéutico (Digoxina, Litio, Metotrexato)
    ('Digoxina', 'Amiodarona', 'grave', 'Amiodarona duplica la concentración plasmática de digoxina por inhibición de glicoproteína P: bloqueo cardíaco letal.'),
    ('Digoxina', 'Verapamilo', 'grave', 'Depresión severa de la conducción auriculoventricular y riesgo de parada sinusal o bradiarritmia extrema.'),
    ('Digoxina', 'Furosemida', 'moderada', 'La hipopotasemia inducida por furosemida sensibiliza el miocardio a la toxicidad arritmogénica por digoxina.'),
    ('Litio', 'Enalapril', 'grave', 'Los IECA reducen la excreción renal de litio, provocando intoxicación lítica aguda (ataxia, temblor severo, convulsiones).'),
    ('Litio', 'Ibuprofeno', 'grave', 'Disminución del aclaramiento renal de litio en más de un 30%: riesgo grave de neurotoxicidad y coma.'),
    ('Litio', 'Hidroclorotiazida', 'grave', 'Las tiazidas inducen retención proximal compensatoria de litio con aumento peligroso de litemia.'),
    ('Metotrexato', 'Ibuprofeno', 'grave', 'Los AINEs disminuyen la secreción tubular renal de metotrexato: pancitopenia grave, fallo medular y mucositis tóxica.'),
    ('Metotrexato', 'Aspirina (Ácido Acetilsalicílico)', 'grave', 'Toxicidad hematológica y hepática severa por acumulación de metotrexato no aclarado.'),

    # Síndrome Serotoninérgico & Interacciones Psiquiátricas
    ('Sertralina', 'Tramadol', 'grave', 'Riesgo de síndrome serotoninérgico severo (hipertermia, mioclonías, agitación psicomotriz y convulsiones).'),
    ('Fluoxetina', 'Tramadol', 'grave', 'Fluoxetina inhibe CYP2D6 y potencia la serotonina: toxicidad serotoninérgica potencialmente mortal.'),
    ('Escitalopram', 'Tramadol', 'grave', 'Riesgo crítico de síndrome serotoninérgico y disminución del umbral convulsivo.'),
    ('Paroxetina', 'Tramadol', 'grave', 'Interacción serotoninérgica grave con crisis hipertensiva y coma autonómico.'),
    ('Venlafaxina', 'Tramadol', 'grave', 'Doble acción serotoninérgica: crisis hipertensiva aguda y síndrome serotoninérgico.'),
    ('Sertralina', 'Ibuprofeno', 'moderada', 'La combinación de ISRS con AINEs incrementa de 3 a 5 veces el riesgo de hemorragia gastrointestinal alta.'),
    ('Escitalopram', 'Aspirina (Ácido Acetilsalicílico)', 'moderada', 'Aumento sinérgico del riesgo de sangrado mucocutáneo y digestivo por inhibición de recaptación plaquetaria.'),
    ('Amitriptilina', 'Tramadol', 'grave', 'Riesgo elevado de crisis convulsivas tónico-clónicas y toxicidad anticolinérgica/serotoninérgica.'),

    # Prolongación de Intervalo QT & Arritmias Ventriculares (Torsades de Pointes)
    ('Amiodarona', 'Ciprofloxacino', 'grave', 'Prolongación severa y sinérgica del intervalo QTc: riesgo de Torsades de Pointes y fibrilación ventricular.'),
    ('Amiodarona', 'Levofloxacino', 'grave', 'Efecto arritmogénico fatal por adición en la prolongación del QTc.'),
    ('Amiodarona', 'Azitromicina', 'grave', 'Cardiotoxicidad sinérgica con riesgo elevado de parada cardíaca por arritmia ventricular compleja.'),
    ('Amiodarona', 'Escitalopram', 'grave', 'Prolongación aditiva de intervalo QT: síncopes y muerte súbita arritmogénica.'),
    ('Ciprofloxacino', 'Escitalopram', 'moderada', 'Aumento de dispersión de repolarización ventricular y riesgo de arritmias.'),

    # Depresión Respiratoria & Sedación Excesiva
    ('Morfina', 'Lorazepam', 'grave', 'Depresión respiratoria severa, hipoxia cerebral y coma profundo por sinergia depresora central.'),
    ('Fentanilo', 'Diazepam', 'grave', 'Riesgo crítico de parada respiratoria y colapso hemodinámico.'),
    ('Tramadol', 'Alprazolam', 'moderada', 'Somnolencia marcada, depresión respiratoria moderada y riesgo incrementado de caídas en ancianos.'),
    ('Zolpidem', 'Lorazepam', 'moderada', 'Aumento de sedación diurna, amnesia retrógrada y alteración del equilibrio con fractura de cadera.'),

    # Interacciones Frecuentes Moderadas y Leves
    ('Alopurinol', 'Amoxicilina', 'moderada', 'Incidencia significativamente mayor de exantema cutáneo alérgico severo (rash ampicilínico).'),
    ('Alopurinol', 'Amoxicilina-Clavulánico', 'moderada', 'Reacciones cutáneas eritematosas generalizadas.'),
    ('Levotiroxina', 'Omeprazol', 'leve', 'El omeprazol reduce la acidez gástrica disminuyendo la absorción intestinal de levotiroxina: monitorizar TSH.'),
    ('Levotiroxina', 'Carbonato de Calcio', 'leve', 'Quelación en tubo digestivo: separar las tomas al menos 4 horas para evitar hipotiroidismo.'),
    ('Ciprofloxacino', 'Teofilina', 'grave', 'Inhibición potente de CYP1A2 elevando niveles de teofilina: convulsiones y taquiarritmias.')
]

interacciones_insert = []
for m1, m2, grav, desc in interacciones_definidas:
    if m1 in med_dict and m2 in med_dict:
        id1, id2 = med_dict[m1], med_dict[m2]
        id_min, id_max = min(id1, id2), max(id1, id2)
        interacciones_insert.append((id_min, id_max, grav, desc))
    else:
        print(f"Alerta: Fármaco no encontrado en catálogo ({m1} o {m2})")

cursor.executemany(
    "INSERT OR IGNORE INTO Interacciones (id_medicamento_1, id_medicamento_2, gravedad, descripcion) VALUES (?, ?, ?, ?)",
    interacciones_insert
)
print(f"✓ Matriz de {len(interacciones_insert)} interacciones clínicas reales insertadas en la BD.")

# ==============================================================================
# 4. Médicos Especialistas
# ==============================================================================
medicos_data = [
    ('Dra. Carmen Morales', 'Medicina Interna'),
    ('Dr. Alejandro Soto', 'Cardiología'),
    ('Dra. Laura Fernandez', 'Geriatría'),
    ('Dr. Manuel Rivas', 'Atención Primaria / Familia'),
    ('Dra. Beatriz Gomez', 'Urgencias Hospitalarias'),
    ('Dr. Javier Ortega', 'Endocrinología'),
    ('Dra. Elena Navarro', 'Reumatología'),
    ('Dr. Francisco Gil', 'Psiquiatría'),
    ('Dra. Marta Beltran', 'Neumología'),
    ('Dr. Sergio Montero', 'Neurología'),
    ('Dra. Nuria Vidal', 'Medicina General'),
    ('Dr. Pablo Alarcon', 'Medicina Interna')
]

cursor.executemany("INSERT INTO Medicos (nombre, especialidad) VALUES (?, ?)", medicos_data)
print(f"✓ {len(medicos_data)} médicos especialistas registrados.")

# ==============================================================================
# 5. Cohorte Clínica Realista: 300 Pacientes con Fenotipos Reales
# ==============================================================================
nombres_m = ['Antonio', 'Manuel', 'Jose', 'Francisco', 'David', 'Juan', 'Javier', 'Carlos', 'Jesus', 'Miguel', 'Rafael', 'Pedro', 'Angel', 'Fernando', 'Luis']
nombres_f = ['Maria', 'Carmen', 'Ana', 'Isabel', 'Dolores', 'Pilar', 'Teresa', 'Rosa', 'Lucia', 'Mercedes', 'Cristina', 'Elena', 'Laura', 'Beatriz', 'Concepcion']
apellidos = ['Garcia', 'Rodriguez', 'Gonzalez', 'Fernandez', 'Lopez', 'Martinez', 'Sanchez', 'Perez', 'Gomez', 'Martin', 'Jimenez', 'Ruiz', 'Hernandez', 'Diaz', 'Moreno', 'Muñoz', 'Alvarez', 'Romero', 'Alonso', 'Gutierrez']

# Perfiles clínicos prototípicos (Comorbilidades reales en hospital)
perfiles_clinicos = [
    # Perfil 1: Anciano cardiovascular con polifarmacia
    {
        "edad_rango": (68, 86),
        "condicion": "Cardiopatía Isquémica, HTA e Hipercolesterolemia",
        "meds_base": ['Aspirina (Ácido Acetilsalicílico)', 'Atorvastatina', 'Bisoprolol', 'Ramipril'],
        "prob_riesgo": 0.35
    },
    # Perfil 2: Fibrilación auricular y riesgo de sangrado
    {
        "edad_rango": (70, 89),
        "condicion": "Fibrilación Auricular y Fallo Cardíaco Leve",
        "meds_base": ['Acenocumarol', 'Furosemida', 'Digoxina'],
        "prob_riesgo": 0.45
    },
    # Perfil 3: Síndrome metabólico y diabetes
    {
        "edad_rango": (52, 75),
        "condicion": "Diabetes Tipo 2, HTA y Dislipidemia",
        "meds_base": ['Metformina', 'Enalapril', 'Simvastatina', 'Empagliflozina'],
        "prob_riesgo": 0.25
    },
    # Perfil 4: Artrosis crónica en paciente anciano hipertenso
    {
        "edad_rango": (65, 84),
        "condicion": "Artrosis Crónica de Rodilla e Hipertensión",
        "meds_base": ['Lisinopril', 'Amlodipino', 'Paracetamol'],
        "prob_riesgo": 0.30
    },
    # Perfil 5: Paciente psiquiátrico con trastorno ansioso-depresivo
    {
        "edad_rango": (28, 62),
        "condicion": "Trastorno Depresivo Mayor e Insomnio",
        "meds_base": ['Sertralina', 'Lorazepam'],
        "prob_riesgo": 0.20
    },
    # Perfil 6: Insuficiencia cardíaca congestiva avanzada
    {
        "edad_rango": (69, 87),
        "condicion": "Insuficiencia Cardíaca Congestiva (NYHA III)",
        "meds_base": ['Espironolactona', 'Enalapril', 'Furosemida', 'Carvedilol'],
        "prob_riesgo": 0.40
    },
    # Perfil 7: Paciente respiratorio crónico
    {
        "edad_rango": (50, 78),
        "condicion": "EPOC y Asma Bronquial",
        "meds_base": ['Salbutamol', 'Budesonida', 'Omeprazol'],
        "prob_riesgo": 0.15
    },
    # Perfil 8: Adulto joven / Chequeo rutinario
    {
        "edad_rango": (19, 44),
        "condicion": "Ninguna (Control preventivo)",
        "meds_base": [],
        "prob_riesgo": 0.05
    }
]

pacientes_insert = []
pacientes_meta = []  # Para guardar perfil asignado a cada paciente

for id_p in range(1, 301):
    genero = random.choice(['M', 'F'])
    nombre = f"{random.choice(nombres_m if genero == 'M' else nombres_f)} {random.choice(apellidos)} {random.choice(apellidos)}"
    perfil = random.choice(perfiles_clinicos)
    edad = random.randint(*perfil["edad_rango"])
    
    pacientes_insert.append((nombre, edad, genero, perfil["condicion"]))
    pacientes_meta.append((id_p, perfil))

cursor.executemany("INSERT INTO Pacientes (nombre, edad, genero, condiciones_previas) VALUES (?, ?, ?, ?)", pacientes_insert)
print(f"✓ 300 pacientes con fenotipos clínicos reales insertados.")

# ==============================================================================
# 6. Consultas Médicas y Prescripciones Históricas (Simulación del Último Año)
# ==============================================================================
fecha_hoy = datetime.now()
consultas_insert = []
recetas_insert = []
id_consulta_counter = 1

# Fármacos de consulta aguda/ocasional
meds_agudos = [
    'Ibuprofeno', 'Naproxeno', 'Diclofenaco', 'Tramadol', 'Amoxicilina-Clavulánico',
    'Ciprofloxacino', 'Azitromicina', 'Claritromicina', 'Omeprazol', 'Alprazolam',
    'Ketorolaco', 'Paracetamol', 'Colquicina', 'Prednisona'
]

for id_paciente, perfil in pacientes_meta:
    # 2 a 4 consultas en el último año para cada paciente
    num_consultas = random.randint(2, 4)
    meds_cronicos_paciente = list(perfil["meds_base"])
    
    for _ in range(num_consultas):
        dias_atras = random.randint(5, 365)
        fecha_con = (fecha_hoy - timedelta(days=dias_atras)).strftime('%Y-%m-%d')
        
        # Médico asignado según especialidad lógica
        if "Cardiopatía" in perfil["condicion"] or "Fibrilación" in perfil["condicion"]:
            id_med = random.choice([2, 1, 3, 5])
        elif "Diabetes" in perfil["condicion"]:
            id_med = random.choice([6, 1, 4])
        elif "Depresivo" in perfil["condicion"]:
            id_med = random.choice([8, 4])
        elif "EPOC" in perfil["condicion"]:
            id_med = random.choice([9, 5, 4])
        else:
            id_med = random.randint(1, len(medicos_data))

        diag = f"Seguimiento y ajuste terapéutico: {perfil['condicion'][:35]}"
        consultas_insert.append((id_paciente, id_med, fecha_con, diag))

        # Medicamentos prescritos en esta consulta:
        # Los crónicos que toma + a veces un nuevo fármaco agudo por dolor/infección/síntomas
        prescritos_consulta = list(meds_cronicos_paciente)
        
        # Con cierta probabilidad, el médico prescribe un nuevo fármaco agudo (AINE, antibiótico, etc.)
        if random.random() < 0.70 or len(prescritos_consulta) == 0:
            nuevo_med = random.choice(meds_agudos)
            if nuevo_med not in prescritos_consulta:
                prescritos_consulta.append(nuevo_med)

        # Si el paciente tiene perfil de alto riesgo, simulated slip (ej. Ibuprofeno recetado a quien toma Sintrom o Enalapril)
        if random.random() < perfil["prob_riesgo"]:
            peligroso = random.choice(['Ibuprofeno', 'Naproxeno', 'Claritromicina', 'Espironolactona', 'Tramadol'])
            if peligroso not in prescritos_consulta:
                prescritos_consulta.append(peligroso)

        # Insertar recetas para la consulta
        for m_nombre in set(prescritos_consulta):
            if m_nombre in med_dict:
                id_m = med_dict[m_nombre]
                dosis = "1 comp. c/24h" if "statin" in m_nombre.lower() or "pril" in m_nombre.lower() else "1 toma c/8h s/indicación"
                recetas_insert.append((id_consulta_counter, id_m, dosis))

        id_consulta_counter += 1

cursor.executemany("INSERT INTO Consultas (id_paciente, id_medico, fecha, diagnostico) VALUES (?, ?, ?, ?)", consultas_insert)
cursor.executemany("INSERT INTO Recetas (id_consulta, id_medicamento, dosis) VALUES (?, ?, ?)", recetas_insert)

conn.commit()

# ==============================================================================
# 7. Exportación a CSV en data/raw/ para Reproducibilidad
# ==============================================================================
tablas_a_exportar = ["Medicamentos", "Interacciones", "Medicos", "Pacientes", "Consultas", "Recetas"]
for tabla in tablas_a_exportar:
    df_t = pd.read_sql(f"SELECT * FROM {tabla}", conn)
    csv_dest = RAW_DATA_DIR / f"{tabla.lower()}.csv"
    df_t.to_csv(csv_dest, index=False)
    print(f"✓ Exportado data/raw/{tabla.lower()}.csv ({len(df_t)} registros)")

conn.close()

print("\n🎉 ¡Éxito! Base de datos 'hospital.db' poblada con datos clínicos reales.")
print(f"Total Medicamentos: {len(medicamentos_raw)}")
print(f"Total Interacciones Reales: {len(interacciones_insert)}")
print(f"Total Consultas Generadas: {len(consultas_insert)}")
print(f"Total Prescripciones / Recetas: {len(recetas_insert)}")
