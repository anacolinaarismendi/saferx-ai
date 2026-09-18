export type Language = "es" | "en" | "de";

export interface Translations {
  nav: {
    problem: string;
    solution: string;
    compliance: string;
    target: string;
    contact: string;
  };
  hero: {
    badge: string;
    titleStart: string;
    titleHighlight: string;
    titleEnd: string;
    subtitle: string;
    ctaPrimary: string;
    ctaSecondary: string;
    stat1Number: string;
    stat1Label: string;
    stat2Number: string;
    stat2Label: string;
    stat3Number: string;
    stat3Label: string;
  };
  problem: {
    tag: string;
    title: string;
    subtitle: string;
    card1: {
      tag: string;
      title: string;
      desc: string;
      metric: string;
    };
    card2: {
      tag: string;
      title: string;
      desc: string;
      metric: string;
    };
    card3: {
      tag: string;
      title: string;
      desc: string;
      metric: string;
    };
  };
  solution: {
    tag: string;
    title: string;
    subtitle: string;
    benefit1Title: string;
    benefit1Desc: string;
    benefit2Title: string;
    benefit2Desc: string;
    benefit3Title: string;
    benefit3Desc: string;
    mockup: {
      headerBadge: string;
      patientName: string;
      patientAge: string;
      ehrSystem: string;
      activeRxLabel: string;
      activeDrug1: string;
      activeDrug1Dose: string;
      newRxLabel: string;
      searchPlaceholder: string;
      prescribingDrug: string;
      prescribingDose: string;
      alertBadge: string;
      alertTitle: string;
      alertDesc1: string;
      alertDrugTaken: string;
      alertDesc2: string;
      alertDrugNew: string;
      alertDesc3: string;
      actionCancel: string;
      actionAlternatives: string;
      statusSafe: string;
    };
  };
  compliance: {
    tag: string;
    title: string;
    subtitle: string;
    hipaaTitle: string;
    hipaaDesc: string;
    gdprTitle: string;
    gdprDesc: string;
    fdaEmaTitle: string;
    fdaEmaDesc: string;
    fhirTitle: string;
    fhirDesc: string;
  };
  target: {
    tag: string;
    title: string;
    subtitle: string;
    primaryCare: {
      title: string;
      role: string;
      desc: string;
      feature: string;
    };
    emergency: {
      title: string;
      role: string;
      desc: string;
      feature: string;
    };
    directors: {
      title: string;
      role: string;
      desc: string;
      feature: string;
    };
  };
  footer: {
    tagline: string;
    ctaCardTitle: string;
    ctaCardSubtitle: string;
    contactBtn: string;
    rights: string;
    privacy: string;
    terms: string;
    security: string;
  };
}

export const translations: Record<Language, Translations> = {
  es: {
    nav: {
      problem: "El Problema",
      solution: "Solución",
      compliance: "Seguridad & Regulación",
      target: "Para Quién",
      contact: "Solicitar Demo",
    },
    hero: {
      badge: "Plataforma HealthTech #1 en Seguridad Farmacológica",
      titleStart: "Seguridad farmacológica",
      titleHighlight: "instantánea",
      titleEnd: "en tu consulta.",
      subtitle:
        "Reduce errores médicos y ahorra tiempo con alertas de interacción basadas en evidencia oficial, sin interrumpir el flujo clínico de trabajo.",
      ctaPrimary: "Solicitar Demo Gratuita",
      ctaSecondary: "Ver EHR Simulado",
      stat1Number: "99.8%",
      stat1Label: "Precisión de detección clínica",
      stat2Number: "< 150ms",
      stat2Label: "Latencia de verificación API",
      stat3Number: "0",
      stat3Label: "Interrupción al flujo del médico",
    },
    problem: {
      tag: "El Reto Clínico Actual",
      title: "Prescribir sin asistencia en tiempo real es un riesgo inasumible",
      subtitle:
        "La sobrecarga asistencial combinada con la complejidad farmacológica moderna desborda las capacidades humanas en consulta.",
      card1: {
        tag: "Sobrecarga Asistencial",
        title: "Falta de Tiempo Crónica",
        desc: "Cruzar a mano las interacciones de 5 o más medicamentos en los 15 minutos estándar de consulta es humanamente inviable.",
        metric: "15 min promedio por consulta",
      },
      card2: {
        tag: "Riesgo Epidemiológico",
        title: "Epidemia de Polifarmacia",
        desc: "Más del 60% de los pacientes crónicos mayores toman 5 o más fármacos simultáneamente, elevando el riesgo de sinergias letales.",
        metric: "x4 riesgo con cada nuevo fármaco",
      },
      card3: {
        tag: "Impacto Legal y Financiero",
        title: "Exposición a Demandas",
        desc: "Las reacciones adversas prevenibles provocan costes millonarios en indemnizaciones y encarecen agresivamente los seguros de responsabilidad civil.",
        metric: "+35% incremento en pólizas médicas",
      },
    },
    solution: {
      tag: "Nuestra Tecnología",
      title: "Inteligencia clínica integrada al historial electrónico (EHR)",
      subtitle:
        "SafeRx AI opera como un centinela silencioso en segundo plano. Se conecta vía API/FHIR a cualquier EHR sin cambiar tus hábitos de prescripción.",
      benefit1Title: "Detección instantánea en milisegundos",
      benefit1Desc:
        "Analiza el historial farmacológico completo del paciente antes de firmar la receta digital.",
      benefit2Title: "Evidencia oficial actualizada al día",
      benefit2Desc:
        "Conectado a bases de datos regulatorias internacionales (AEMPS, FDA, EMA y fichas técnicas oficiales).",
      benefit3Title: "Cero fatiga de alarmas",
      benefit3Desc:
        "Algoritmos que filtran alertas irrelevantes y solo notifican interacciones con riesgo de desenlace severo.",
      mockup: {
        headerBadge: "EHR Simulator - Entorno Médico Activo",
        patientName: "Juan Pérez Gómez",
        patientAge: "68 años",
        ehrSystem: "CliniSys HealthCare v4.8",
        activeRxLabel: "Medicación Activa en Ficha:",
        activeDrug1: "Aspirina (Ácido Acetilsalicílico)",
        activeDrug1Dose: "100 mg / 24h",
        newRxLabel: "Prescribir Nuevo Fármaco:",
        searchPlaceholder: "Buscando fármaco en vademécum...",
        prescribingDrug: "Warfarina Sódica",
        prescribingDose: "5 mg vía oral",
        alertBadge: "CRÍTICA • Nivel 1",
        alertTitle: "¡ALERTA GRAVE! RIESGO DE HEMORRAGIA SEVERA",
        alertDesc1: "El paciente ya se encuentra bajo tratamiento con",
        alertDrugTaken: "Aspirina",
        alertDesc2: ". La administración concomitante con",
        alertDrugNew: "Warfarina",
        alertDesc3:
          "potencia el efecto anticoagulante y multiplica el riesgo de hemorragia gastrointestinal o intracraneal severa.",
        actionCancel: "Descartar Prescripción",
        actionAlternatives: "Consultar Fármacos Alternativos",
        statusSafe: "Bloqueo preventivo de seguridad activo",
      },
    },
    compliance: {
      tag: "Estándares & Confianza",
      title: "Seguridad y cumplimiento clínico de grado hospitalario",
      subtitle:
        "Construido bajo los marcos regulatorios internacionales más exigentes para la protección de datos de salud y fiabilidad clínica.",
      hipaaTitle: "HIPAA Compliant",
      hipaaDesc: "Cifrado de extremo a extremo (AES-256) y anonimización de identificadores de salud protegidos.",
      gdprTitle: "Reglamento RGPD / UE",
      gdprDesc: "Servidores alojados en la Unión Europea con soberanía de datos y estricto consentimiento informado.",
      fdaEmaTitle: "Evidencia FDA & EMA",
      fdaEmaDesc: "Modelos calibrados únicamente con evidencia farmacológica validada por agencias reguladoras oficiales.",
      fhirTitle: "Interoperabilidad FHIR / HL7",
      fhirDesc: "Integración nativa con sistemas hospitalarios existentes mediante conectores estandarizados HL7 FHIR R4.",
    },
    target: {
      tag: "Casos de Uso",
      title: "Diseñado para la primera línea y líderes médicos",
      subtitle:
        "Herramientas especializadas para cada nivel de toma de decisiones en el ecosistema sanitario.",
      primaryCare: {
        title: "Atención Primaria",
        role: "Médicos de Familia & Generalistas",
        desc: "Revisión sistemática de pacientes polimedicados crónicos sin perder minutos valiosos en vademécums manuales.",
        feature: "Alertas directas en la consulta de 15 minutos",
      },
      emergency: {
        title: "Urgencias y UCI",
        role: "Médicos de Urgencias Hospitalarias",
        desc: "Seguridad inmediata en decisiones críticas y de choque donde el tiempo de reacción es cuestión de segundos.",
        feature: "Respuesta en <150ms con triaje de gravedad",
      },
      directors: {
        title: "Dirección Médica",
        role: "Directores Médicos & Gestores Clínicos",
        desc: "Monitorización de métricas de calidad asistencial, reducción de eventos adversos prevenibles y blindaje legal.",
        feature: "Dashboard de analítica e indicadores de riesgo",
      },
    },
    footer: {
      tagline:
        "SafeRx AI: Transformando la seguridad farmacológica mediante inteligencia artificial clínica. Protege a tus pacientes, protege tu práctica.",
      ctaCardTitle: "¿Listo para blindar tu práctica clínica?",
      ctaCardSubtitle:
        "Solicita una demostración personalizada con uno de nuestros especialistas clínicos.",
      contactBtn: "demo@saferx.ai",
      rights: "© 2026 FritzeFriends. Todos los derechos reservados.",
      privacy: "Política de Privacidad",
      terms: "Términos de Servicio",
      security: "Seguridad & Compliance",
    },
  },
  en: {
    nav: {
      problem: "The Problem",
      solution: "Solution",
      compliance: "Security & Standards",
      target: "Who It's For",
      contact: "Request Demo",
    },
    hero: {
      badge: "#1 Clinical AI Platform for Pharmacological Safety",
      titleStart: "Instant pharmacological",
      titleHighlight: "safety",
      titleEnd: "in your clinical practice.",
      subtitle:
        "Reduce medical errors and save precious time with drug interaction alerts grounded in official regulatory evidence, without interrupting doctor workflow.",
      ctaPrimary: "Request Free Demo",
      ctaSecondary: "Explore Simulated EHR",
      stat1Number: "99.8%",
      stat1Label: "Clinical detection accuracy",
      stat2Number: "< 150ms",
      stat2Label: "Real-time API latency",
      stat3Number: "0",
      stat3Label: "Workflow disruption",
    },
    problem: {
      tag: "The Clinical Challenge",
      title: "Prescribing without real-time AI assistance is an unacceptable risk",
      subtitle:
        "High patient volume coupled with skyrocketing pharmacological complexity exceeds manual cross-referencing capabilities.",
      card1: {
        tag: "Time Deficit",
        title: "Chronic Lack of Time",
        desc: "Manually checking interactions for 5+ medications within standard 15-minute consultations is mathematically unfeasible.",
        metric: "15 min avg consultation length",
      },
      card2: {
        tag: "Epidemiological Risk",
        title: "Polypharmacy Epidemic",
        desc: "Over 60% of elderly chronic patients take 5 or more daily drugs, exponentially multiplying the probability of fatal adverse synergies.",
        metric: "4x adverse risk with each new drug",
      },
      card3: {
        tag: "Financial & Legal Exposure",
        title: "Malpractice Liability",
        desc: "Preventable adverse drug events spark multimillion-dollar lawsuits and dramatically inflate clinical malpractice insurance premiums.",
        metric: "+35% annual liability premium hike",
      },
    },
    solution: {
      tag: "Our Technology",
      title: "Clinical intelligence embedded directly into your EHR",
      subtitle:
        "SafeRx AI operates as a silent sentinel in the background. It connects via REST/FHIR APIs to any Electronic Health Record without altering clinician habits.",
      benefit1Title: "Sub-second interaction detection",
      benefit1Desc:
        "Instantly scrutinizes the patient's entire active medication list before the electronic prescription is submitted.",
      benefit2Title: "Regulatory-grade official evidence",
      benefit2Desc:
        "Powered by validated, up-to-date global pharmacological monographs (FDA, EMA, AEMPS).",
      benefit3Title: "Zero alert fatigue",
      benefit3Desc:
        "Proprietary filtering discards clinically negligible interactions, escalating only life-threatening combination risks.",
      mockup: {
        headerBadge: "EHR Simulator - Active Medical Environment",
        patientName: "John Doe",
        patientAge: "68 y/o",
        ehrSystem: "CliniSys HealthCare v4.8",
        activeRxLabel: "Active Patient Medications:",
        activeDrug1: "Aspirin (Acetylsalicylic Acid)",
        activeDrug1Dose: "100 mg / 24h",
        newRxLabel: "Prescribing New Medication:",
        searchPlaceholder: "Searching clinical pharmacopeia...",
        prescribingDrug: "Warfarin Sodium",
        prescribingDose: "5 mg oral tablet",
        alertBadge: "CRITICAL • Level 1",
        alertTitle: "CRITICAL ALERT! SEVERE HEMORRHAGE RISK",
        alertDesc1: "Patient is currently undergoing active therapy with",
        alertDrugTaken: "Aspirin",
        alertDesc2: ". Concomitant administration of",
        alertDrugNew: "Warfarin",
        alertDesc3:
          "synergistically intensifies anticoagulant potency, creating extreme danger of massive gastrointestinal or intracranial bleeding.",
        actionCancel: "Discard Prescription",
        actionAlternatives: "View Safer Clinical Alternatives",
        statusSafe: "Preventive safety safeguard triggered",
      },
    },
    compliance: {
      tag: "Standards & Trust",
      title: "Hospital-grade clinical security and regulatory compliance",
      subtitle:
        "Engineered strictly to satisfy the highest international standards for medical data protection and diagnostic reliability.",
      hipaaTitle: "HIPAA Compliant",
      hipaaDesc: "End-to-end encryption (AES-256) with automated de-identification of protected health information (PHI).",
      gdprTitle: "GDPR & EU Standards",
      gdprDesc: "European sovereign cloud hosting ensuring full clinical data protection and user rights.",
      fdaEmaTitle: "FDA & EMA Evidence",
      fdaEmaDesc: "Models calibrated exclusively on verified pharmacological monographs and authoritative clinical trials.",
      fhirTitle: "FHIR / HL7 Interoperability",
      fhirDesc: "Native bi-directional connectivity with legacy hospital systems via modern HL7 FHIR R4 specifications.",
    },
    target: {
      tag: "Use Cases",
      title: "Tailored for frontline practitioners and healthcare leaders",
      subtitle:
        "Specialized clinical decision-support modules designed for distinct medical touchpoints.",
      primaryCare: {
        title: "Primary Care",
        role: "Family & General Practitioners",
        desc: "Perform comprehensive medication therapy reviews for chronic poly-medicated patients in seconds.",
        feature: "Instant guardrails within 15-minute consultations",
      },
      emergency: {
        title: "Emergency & ICU",
        role: "Emergency Physicians & Intensivists",
        desc: "Instantaneous drug-safety clearance in acute, high-pressure resuscitation environments.",
        feature: "<150ms triage response for time-critical care",
      },
      directors: {
        title: "Medical Leadership",
        role: "Chief Medical Officers & Clinical Directors",
        desc: "Elevate patient safety KPIs, diminish preventable adverse events, and fortify institutional liability defense.",
        feature: "Real-time safety analytics & compliance audit trail",
      },
    },
    footer: {
      tagline:
        "SafeRx AI: Revolutionizing medication safety through clinical artificial intelligence. Safeguard your patients, protect your medical practice.",
      ctaCardTitle: "Ready to protect your clinical practice?",
      ctaCardSubtitle:
        "Schedule a custom live demonstration with our clinical informatics team.",
      contactBtn: "demo@saferx.ai",
      rights: "© 2026 FritzeFriends. All rights reserved.",
      privacy: "Privacy Policy",
      terms: "Terms of Service",
      security: "Security & Compliance",
    },
  },
  de: {
    nav: {
      problem: "Das Problem",
      solution: "Lösung",
      compliance: "Sicherheit & Standards",
      target: "Zielgruppe",
      contact: "Demo anfordern",
    },
    hero: {
      badge: "Nr. 1 KI-Plattform für klinische Arzneimittelsicherheit",
      titleStart: "Sofortige pharmakologische",
      titleHighlight: "Sicherheit",
      titleEnd: "in Ihrer Arztpraxis.",
      subtitle:
        "Reduzieren Sie Behandlungsfehler und sparen Sie wertvolle Zeit mit evidenzbasierten Interaktionswarnungen direkt in Ihrem EHR-System.",
      ctaPrimary: "Kostenlose Demo anfordern",
      ctaSecondary: "EHR-Simulation ansehen",
      stat1Number: "99.8%",
      stat1Label: "Klinische Erkennungsgenauigkeit",
      stat2Number: "< 150ms",
      stat2Label: "API-Prüfung in Echtzeit",
      stat3Number: "0",
      stat3Label: "Unterbrechung des Arbeitsablaufs",
    },
    problem: {
      tag: "Die klinische Herausforderung",
      title: "Verschreiben ohne Echtzeit-Assistenz ist ein unkalkulierbares Risiko",
      subtitle:
        "Hohe Patientenzahlen und komplexe Pharmakotherapien übersteigen die Möglichkeiten manueller Kontrollen im Praxisalltag.",
      card1: {
        tag: "Zeitmangel",
        title: "Chronische Zeitnot",
        desc: "Die manuelle Überprüfung von 5 oder mehr Medikamenten in einer 15-minütigen Sprechstunde ist praktisch unmöglich.",
        metric: "15 Min. durchschnittliche Behandlungszeit",
      },
      card2: {
        tag: "Epidemiologisches Risiko",
        title: "Polypharmazie-Welle",
        desc: "Über 60% der älteren chronisch kranken Patienten nehmen täglich 5 oder mehr Medikamente ein, was das Risiko toxischer Wechselwirkungen potenziert.",
        metric: "4-faches Risiko mit jedem Zusatzwirkstoff",
      },
      card3: {
        tag: "Haftung & Kosten",
        title: "Juristische Haftungsrisiken",
        desc: "Vermeidbare unerwünschte Arzneimittelwirkungen führen zu Schadensersatzforderungen und verteuern die Arzthaftpflichtversicherungen erheblich.",
        metric: "+35% Kostenanstieg bei Haftpflichtpolicen",
      },
    },
    solution: {
      tag: "Unsere Technologie",
      title: "Klinische Intelligenz direkt in Ihrer elektronischen Patientenakte",
      subtitle:
        "SafeRx AI agiert als unaufdringlicher Wächter im Hintergrund. Die Lösung lässt sich über REST/FHIR-Schnittstellen nahtlos in jedes Praxisverwaltungssystem einbinden.",
      benefit1Title: "Prüfung in Millisekunden",
      benefit1Desc:
        "Gleicht den gesamten Medikationsplan des Patienten vor der digitalen Rezeptfreigabe blitzschnell ab.",
      benefit2Title: "Behördlich validierte Evidenz",
      benefit2Desc:
        "Gestützt auf geprüfte Datenbanken von EMA, FDA und nationalen Arzneimittelbehörden.",
      benefit3Title: "Keine Alarmmüdigkeit",
      benefit3Desc:
        "Intelligente Filterung verhindert unnötige Meldungen und warnt ausschließlich bei schwerwiegenden Gefährdungen.",
      mockup: {
        headerBadge: "EHR-Simulator - Aktive Praxisumgebung",
        patientName: "Max Mustermann",
        patientAge: "68 Jahre",
        ehrSystem: "CliniSys HealthCare v4.8",
        activeRxLabel: "Bestehende Dauermedikation:",
        activeDrug1: "Aspirin (Acetylsalicylsäure)",
        activeDrug1Dose: "100 mg / 24h",
        newRxLabel: "Neues Medikament verschreiben:",
        searchPlaceholder: "Suche in der Arzneimitteldatenbank...",
        prescribingDrug: "Warfarin-Natrium",
        prescribingDose: "5 mg Filmtablette",
        alertBadge: "KRITISCH • Stufe 1",
        alertTitle: "KRITISCHE WARNUNG! HOHE BLUTUNGSGEFAHR",
        alertDesc1: "Der Patient nimmt bereits",
        alertDrugTaken: "Aspirin",
        alertDesc2: "ein. Die gleichzeitige Gabe von",
        alertDrugNew: "Warfarin",
        alertDesc3:
          "verstärkt die gerinnungshemmende Wirkung massiv und führt zu einem extrem hohen Risiko lebensbedrohlicher gastrointestinaler oder intrakranieller Blutungen.",
        actionCancel: "Verschreibung abbrechen",
        actionAlternatives: "Sicherere Alternativen anzeigen",
        statusSafe: "Präventive Sicherheitsblockade aktiv",
      },
    },
    compliance: {
      tag: "Sicherheit & Vertrauen",
      title: "Klinische Sicherheit auf Krankenhausniveau",
      subtitle:
        "Entwickelt nach den strengsten europäischen und internationalen Vorgaben für Gesundheitsdaten und Patientensicherheit.",
      hipaaTitle: "HIPAA-Konform",
      hipaaDesc: "Vollständige Ende-zu-Ende-Verschlüsselung (AES-256) und automatische Anonymisierung aller Patientendaten.",
      gdprTitle: "DSGVO-Konformität",
      gdprDesc: "Hosting in nach ISO-27001 zertifizierten europäischen Rechenzentren unter voller Beachtung der DSGVO.",
      fdaEmaTitle: "EMA- & FDA-Evidenz",
      fdaEmaDesc: "Algorithmen stützen sich ausschließlich auf behördlich freigegebene Fachinformationen.",
      fhirTitle: "HL7 FHIR R4 Interoperabilität",
      fhirDesc: "Standardisierte Schnittstellen zur problemlosen Anbindung an bestehende Krankenhaus- und Praxissysteme.",
    },
    target: {
      tag: "Anwendungsbereiche",
      title: "Entwickelt für die medizinische Frontlinie und Führungskräfte",
      subtitle:
        "Maßgeschneiderte Unterstützung für fundierte klinische Entscheidungen auf allen Ebenen.",
      primaryCare: {
        title: "Allgemeinmedizin",
        role: "Hausärzte & Internisten",
        desc: "Sichere Betreuung polymedikierter chronischer Patienten ohne zeitraubendes Nachschlagen in externen Handbüchern.",
        feature: "Sofortiger Sicherheitscheck im 15-Minuten-Takt",
      },
      emergency: {
        title: "Notaufnahme & Intensiv",
        role: "Notfallmediziner & Anästhesisten",
        desc: "Verlässliche Entscheidungsfindung unter extremem Zeitdruck bei akuten Notfallpatienten.",
        feature: "Reaktionszeit <150ms mit Dringlichkeits-Triage",
      },
      directors: {
        title: "Ärztliche Leitung",
        role: "Chefärzte & Qualitätsmanager",
        desc: "Steigerung der Patientensicherheit, Minimierung von Medikationsfehlern und Verringerung haftungsrechtlicher Risiken.",
        feature: "Zentrales Qualitäts-Dashboard mit Audit-Funktion",
      },
    },
    footer: {
      tagline:
        "SafeRx AI: Patientensicherheit neu definiert durch klinische künstliche Intelligenz. Schützen Sie Ihre Patienten und Ihre Praxis.",
      ctaCardTitle: "Bereit für mehr Arzneimittelsicherheit?",
      ctaCardSubtitle:
        "Vereinbaren Sie eine persönliche Online-Demonstration mit unseren Fachberatern.",
      contactBtn: "demo@saferx.ai",
      rights: "© 2026 FritzeFriends. Alle Rechte vorbehalten.",
      privacy: "Datenschutzrichtlinie",
      terms: "Nutzungsbedingungen",
      security: "Sicherheitsstandards",
    },
  },
};
