import sqlite3
import random
from datetime import datetime, timedelta
import os

# 1. Asegurarnos de que estamos en la carpeta correcta
db_path = 'database/hospital.db'
schema_path = 'database/schema.sql'

print("Iniciando la generación de datos...")

# FIX: crear la carpeta 'database' si no existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# FIX: borrar la base de datos anterior para garantizar una ejecución limpia
# (evita errores de "tabla ya existe" y datos duplicados en Médicos/Pacientes/Consultas/Recetas)
if os.path.exists(db_path):
    os.remove(db_path)

# 2. Conectar a la base de datos (creará el archivo hospital.db)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 3. Leer y ejecutar el archivo schema.sql
with open(schema_path, 'r', encoding='utf-8') as f:
    schema_sql = f.read()
    cursor.executescript(schema_sql)

print("Esquema creado con éxito.")

# 4. Insertar Medicamentos
medicamentos = [
    ('Ibuprofeno', 'Advil'),              # ID 1
    ('Aspirina', 'Aspirina Bayer'),       # ID 2
    ('Warfarina', 'Aldocumar'),           # ID 3 (Anticoagulante fuerte)
    ('Amoxicilina', 'Clamoxyl'),          # ID 4
    ('Omeprazol', 'Omeoprazol Genérico'), # ID 5
    ('Lisinopril', 'Zestril')             # ID 6
]
cursor.executemany("INSERT OR IGNORE INTO Medicamentos (principio_activo, nombre_comercial) VALUES (?, ?)", medicamentos)

# 5. Insertar Interacciones (¡La clave para nuestra IA!)
interacciones = [
    (1, 2, 'moderada', 'Aumento del riesgo de sangrado gastrointestinal.'),
    (2, 3, 'grave', 'Riesgo altísimo de hemorragia severa. Evitar combinación.'),
    (1, 6, 'grave', 'Riesgo de toxicidad renal e hipertensión no controlada.')
]
cursor.executemany("INSERT OR IGNORE INTO Interacciones (id_medicamento_1, id_medicamento_2, gravedad, descripcion) VALUES (?, ?, ?, ?)", interacciones)

# 6. Crear Médicos
nombres_medicos = ['Dra. Martinez', 'Dr. Gomez', 'Dra. Silva', 'Dr. Lopez', 'Dra. Fernandez']
especialidades = ['Medicina General', 'Urgencias', 'Geriatría']
medicos_data = [(nombre, random.choice(especialidades)) for nombre in nombres_medicos]
cursor.executemany("INSERT INTO Medicos (nombre, especialidad) VALUES (?, ?)", medicos_data)

# 7. Crear 150 Pacientes
nombres_base = ['Ana', 'Carlos', 'Luis', 'Maria', 'Jose', 'Lucia', 'Jorge', 'Elena', 'Miguel', 'Sara']
apellidos_base = ['Perez', 'Garcia', 'Ruiz', 'Diaz', 'Sanz', 'Torres', 'Ramirez', 'Flores']
pacientes_data = []

for _ in range(150):
    nombre = f"{random.choice(nombres_base)} {random.choice(apellidos_base)}"
    edad = random.randint(18, 85)
    genero = random.choice(['M', 'F'])
    pacientes_data.append((nombre, edad, genero, 'Ninguna' if edad < 50 else 'Hipertensión'))

cursor.executemany("INSERT INTO Pacientes (nombre, edad, genero, condiciones_previas) VALUES (?, ?, ?, ?)", pacientes_data)

# 8. Crear Consultas y Recetas históricas (Simulando el último año)
fecha_actual = datetime.now()
consultas_data = []
recetas_data = []
id_consulta_counter = 1

for id_paciente in range(1, 151):
    num_consultas = random.randint(1, 3)
    for _ in range(num_consultas):
        id_medico = random.randint(1, 5)
        dias_atras = random.randint(1, 365)
        fecha_consulta = (fecha_actual - timedelta(days=dias_atras)).strftime('%Y-%m-%d')

        consultas_data.append((id_paciente, id_medico, fecha_consulta, 'Consulta rutinaria'))

        num_medicamentos = random.randint(1, 2)
        meds_recetados = random.sample(range(1, 7), num_medicamentos)

        for med in meds_recetados:
            recetas_data.append((id_consulta_counter, med, '1 pastilla cada 8 horas'))

        id_consulta_counter += 1

cursor.executemany("INSERT INTO Consultas (id_paciente, id_medico, fecha, diagnostico) VALUES (?, ?, ?, ?)", consultas_data)
cursor.executemany("INSERT INTO Recetas (id_consulta, id_medicamento, dosis) VALUES (?, ?, ?)", recetas_data)

# Guardar los cambios y cerrar
conn.commit()
conn.close()

print("¡Éxito! Base de datos 'hospital.db' creada y poblada con médicos, pacientes y recetas ficticias.")
