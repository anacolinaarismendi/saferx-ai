PRAGMA foreign_keys = ON;

-- Tabla de Pacientes
CREATE TABLE IF NOT EXISTS Pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER CHECK (edad >= 0 AND edad <= 120),
    genero TEXT,
    condiciones_previas TEXT
);

-- Tabla de Médicos
CREATE TABLE IF NOT EXISTS Medicos (
    id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    especialidad TEXT
);

-- Tabla del Catálogo de Medicamentos
CREATE TABLE IF NOT EXISTS Medicamentos (
    id_medicamento INTEGER PRIMARY KEY AUTOINCREMENT,
    principio_activo TEXT NOT NULL,
    nombre_comercial TEXT,
    UNIQUE (principio_activo, nombre_comercial)
);

-- Tabla de Consultas (Une al médico con el paciente en una fecha)
CREATE TABLE IF NOT EXISTS Consultas (
    id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER NOT NULL,
    id_medico INTEGER NOT NULL,
    fecha DATE NOT NULL,
    diagnostico TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Pacientes(id_paciente) ON DELETE CASCADE,
    FOREIGN KEY (id_medico) REFERENCES Medicos(id_medico) ON DELETE RESTRICT
);

-- Tabla de Recetas (Qué medicamentos se recetaron en cada consulta)
CREATE TABLE IF NOT EXISTS Recetas (
    id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_consulta INTEGER NOT NULL,
    id_medicamento INTEGER NOT NULL,
    dosis TEXT,
    FOREIGN KEY (id_consulta) REFERENCES Consultas(id_consulta) ON DELETE CASCADE,
    FOREIGN KEY (id_medicamento) REFERENCES Medicamentos(id_medicamento) ON DELETE RESTRICT,
    UNIQUE (id_consulta, id_medicamento)
);

-- NUEVA: Catálogo de interacciones conocidas entre principios activos
-- Sin esto, no hay forma de que la IA "sepa" qué combinaciones son peligrosas
CREATE TABLE IF NOT EXISTS Interacciones (
    id_interaccion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_medicamento_1 INTEGER NOT NULL,
    id_medicamento_2 INTEGER NOT NULL,
    gravedad TEXT CHECK (gravedad IN ('leve', 'moderada', 'grave')),
    descripcion TEXT,
    FOREIGN KEY (id_medicamento_1) REFERENCES Medicamentos(id_medicamento),
    FOREIGN KEY (id_medicamento_2) REFERENCES Medicamentos(id_medicamento),
    CHECK (id_medicamento_1 < id_medicamento_2),  -- evita pares duplicados/invertidos
    UNIQUE (id_medicamento_1, id_medicamento_2)
);

-- Índices para acelerar las búsquedas de interacciones
CREATE INDEX IF NOT EXISTS idx_consultas_paciente ON Consultas(id_paciente);
CREATE INDEX IF NOT EXISTS idx_consultas_medico ON Consultas(id_medico);
CREATE INDEX IF NOT EXISTS idx_recetas_consulta ON Recetas(id_consulta);
CREATE INDEX IF NOT EXISTS idx_recetas_medicamento ON Recetas(id_medicamento);
CREATE INDEX IF NOT EXISTS idx_interacciones_medicamento_1 ON Interacciones(id_medicamento_1);
CREATE INDEX IF NOT EXISTS idx_interacciones_medicamento_2 ON Interacciones(id_medicamento_2);