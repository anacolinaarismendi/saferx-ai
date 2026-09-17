"""
Extracción de eventos adversos reales desde la API pública de OpenFDA (FAERS)
==============================================================================
Descarga reportes de reacciones adversas reales notificadas a la FDA para
fármacos clave involucrados en polifarmacia e interacciones medicamentosas.

Autor: Equipo SafeRx AI
"""

import json
import logging
from pathlib import Path
import time
from typing import Any, Dict, List, Optional
import urllib.parse
import requests
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "data" / "raw" / "openfda_adverse_events.csv"

# Principios activos clave a consultar en OpenFDA
DRUGS_TO_QUERY = [
    "warfarin",
    "aspirin",
    "ibuprofen",
    "lisinopril",
    "amiodarone",
    "clopidogrel",
    "simvastatin",
    "metformin",
    "ciprofloxacin",
    "sertraline",
    "tramadol",
    "omeprazole",
    "spironolactone",
    "methotrexate",
    "digoxin"
]

OPENFDA_URL = "https://api.fda.gov/drug/event.json"


def fetch_events_for_drug(drug_name: str, limit: int = 35) -> List[Dict[str, Any]]:
    """Descarga eventos adversos de OpenFDA para un fármaco dado."""
    query = f'patient.drug.openfda.generic_name:{drug_name}+AND+serious:1'
    url = f"{OPENFDA_URL}?search={query}&limit={limit}"
    headers = {
        "User-Agent": "SafeRxAI-Research/1.0 (Clinical Decision Support; Educational/Portfolio)"
    }
    
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("results", [])
        else:
            logger.warning("Respuesta %s para fármaco %s: %s", resp.status_code, drug_name, resp.text[:120])
            return []
    except Exception as exc:
        logger.error("Error consultando OpenFDA para %s: %s", drug_name, exc)
        return []


def parse_fda_record(record: Dict[str, Any], query_drug: str) -> Optional[Dict[str, Any]]:
    """Normaliza un reporte de la FDA en una fila tabular estandarizada."""
    patient = record.get("patient", {})
    if not patient:
        return None

    # Edad
    edad_raw = patient.get("patientonsetage")
    unit = str(patient.get("patientonsetageunit", "801"))  # 801 = años en MedDRA/ICH
    edad = None
    if edad_raw is not None:
        try:
            val = float(edad_raw)
            if unit == "801":  # Años
                edad = int(val)
            elif unit == "802":  # Meses
                edad = int(val / 12)
            elif unit == "800":  # Décadas
                edad = int(val * 10)
        except (ValueError, TypeError):
            pass

    # Género: 1 = Masculino, 2 = Femenino
    sex_code = str(patient.get("patientsex", ""))
    genero = "M" if sex_code == "1" else ("F" if sex_code == "2" else "Desconocido")

    # Medicamentos concomitantes
    drugs_list = patient.get("drug", [])
    meds_names = []
    for d in drugs_list:
        p_name = d.get("medicinalproduct")
        if p_name:
            meds_names.append(p_name.strip().title())

    if not meds_names:
        meds_names = [query_drug.capitalize()]

    # Reacciones adversas reportadas
    reactions_list = patient.get("reaction", [])
    rx_terms = [r.get("reactionmeddrapt") for r in reactions_list if r.get("reactionmeddrapt")]
    reaction_str = "; ".join(rx_terms[:3]) if rx_terms else "Adverse Event"

    # Desenlaces graves
    es_grave = 1 if str(record.get("serious")) == "1" else 0
    hospitalizacion = 1 if str(record.get("seriousnesshospitalization")) == "1" else 0
    riesgo_vital = 1 if str(record.get("seriousnesslifethreatening")) == "1" else 0
    muerte = 1 if str(record.get("seriousnessdeath")) == "1" else 0

    return {
        "report_id": record.get("safetyreportid"),
        "farmaco_buscado": query_drug.capitalize(),
        "edad": edad if (edad is not None and 0 <= edad <= 110) else None,
        "genero": genero,
        "num_medicamentos": len(meds_names),
        "medicamentos": "; ".join(meds_names[:6]),
        "reaccion_adversa": reaction_str,
        "es_grave": es_grave,
        "hospitalizacion": hospitalizacion,
        "riesgo_vital": riesgo_vital,
        "muerte": muerte,
        "fecha_recibido": record.get("receivedate")
    }


def main():
    logger.info("Iniciando extracción de datos reales desde OpenFDA FAERS...")
    all_parsed: List[Dict[str, Any]] = []

    for drug in DRUGS_TO_QUERY:
        logger.info("Consultando OpenFDA para fármaco: %s", drug)
        records = fetch_events_for_drug(drug, limit=35)
        count = 0
        for rec in records:
            parsed = parse_fda_record(rec, drug)
            if parsed:
                all_parsed.append(parsed)
                count += 1
        logger.info("Extraídos %d eventos válidos para %s", count, drug)
        time.sleep(0.25)  # Respetar rate limit de OpenFDA

    df = pd.DataFrame(all_parsed)
    logger.info("Total de reportes reales extraídos: %d", len(df))

    if not df.empty:
        mediana_edad = int(df["edad"].dropna().median()) if not df["edad"].dropna().empty else 65
        df["edad"] = df["edad"].fillna(mediana_edad).astype(int)
        
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(OUTPUT_FILE, index=False)
        logger.info("Datos reales de OpenFDA guardados en %s con éxito.", OUTPUT_FILE)
    else:
        logger.warning("No se obtuvieron registros de OpenFDA; verifique la conexión.")


if __name__ == "__main__":
    main()
