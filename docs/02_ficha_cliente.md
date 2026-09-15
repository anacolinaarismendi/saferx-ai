# Fase 2: Ficha del Cliente

## 1. Datos Generales de la Empresa
* **Nombre:** Grupo Hospitalario San José.
* **Sector:** Salud y Asistencia Médica Privada
* **Actividad:** Red de clínicas de atención primaria y urgencias.
* **Tamaño:** Mediano-Grande (3 hospitales regionales y 12 clínicas locales).
* **Número de empleados:** 250 médicos en plantilla, 400 enfermeros y 150 administrativos.
* **Número de pacientes:** Atienden unas 3,000 consultas diarias (aprox. 1 millón al año).
* **Servicios principales:** Urgencias 24h, Medicina General, Pediatría y Geriatría.

## 2. Modelo de Negocio y Procesos
* **Modelo de negocio:** Ingresos por consultas privadas y acuerdos con aseguradoras de salud (pagan por volumen y eficiencia).
* **Proceso principal afectado:** La prescripción de recetas médicas al final de la consulta.
* **Sistema actual:** Utilizan un software de historial clínico antiguo (EHR) que guarda las notas del médico, pero no tiene inteligencia. Si un médico quiere revisar si dos medicamentos interactúan, debe abrir una pestaña nueva en Google o mirar un manual físico (Vademécum).

## 3. Situación Actual y Problemas
* **El Problema Principal:** Los pacientes mayores (geriatría) toman de media entre 4 y 7 medicamentos distintos (polifarmacia). Cruzar las interacciones de 5 medicamentos a mano es matemáticamente complejo e inviable en los 15 minutos que dura una consulta.
* **Consecuencias / Necesidades:**
  * **Pérdida de tiempo:** Los médicos pierden entre 3 y 5 minutos por paciente solo verificando compatibilidades.
  * **Riesgo y Pérdida económica:** El año pasado tuvieron 12 incidentes graves de reacciones adversas por mezclas de medicamentos. Esto provocó 3 demandas legales que hicieron que el seguro de "mala praxis" de la clínica subiera un 15% este año.
  * **Necesidad:** Necesitan un sistema que lea automáticamente lo que el médico está recetando y avise *solo* si hay un riesgo real, sin hacerles perder tiempo.

  ## 4. Modelo de Datos Inicial

  ```mermaid
  erDiagram
    PACIENTES ||--o{ CONSULTAS : "tiene"
    MEDICOS ||--o{ CONSULTAS : "atiende"
    CONSULTAS ||--o{ RECETAS : "genera"
    MEDICAMENTOS ||--o{ RECETAS : "se incluye en"

    PACIENTES {
      int id_paciente PK
      string nombre
      int edad
      string genero
      string condiciones_previas
    }
    MEDICOS {
      int id_medico PK
      string nombre
      string especialidad
    }
    MEDICAMENTOS {
      int id_medicamento PK
      string principio_activo
      string nombre_comercial
    }
    CONSULTAS {
      int id_consulta PK
      int id_paciente FK
      int id_medico FK
      date fecha
      string diagnostico
    }
    RECETAS {
      int id_receta PK
      int id_consulta FK
      int id_medicamento FK
      string dosis
    }
  ```

  