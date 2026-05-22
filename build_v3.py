#!/usr/bin/env python3
"""Build v3: collapsible sections, deeper content, CSS diagrams, visual charts."""
import json

def sec(num, title, subs):
    """Build a section dict"""
    return {"id": f"s{num.replace('.','')}", "num": num, "title": title, "content": subs}

units = [
  {
    "code": "U1",
    "title": "Caracterización de los procesos en laboratorios de citogenética y biología molecular",
    "emoji": "🧬",
    "desc": "Organización, áreas, equipos, seguridad y bioseguridad en laboratorios genéticos",
    "desc": "Organización, áreas de trabajo, equipos, normativa de seguridad y eliminación de residuos en laboratorios genéticos",
    "sections": [
      sec("1.1", "Organización del laboratorio de citogenética y cultivo celular", [
        ("Organigrama", "", [
          "👤 Director: coordina y supervisa el laboratorio, contacto con médicos",
          "👤 Responsable de citogenética: supervisa diagnóstico clínico",
          "👤 Facultativos: analizan resultados y emiten informes",
          "👤 Personal técnico: recepción, procesamiento, gestión de stock",
          "👤 Personal de prácticas: en formación supervisada",
          "👤 Personal auxiliar: limpieza y mantenimiento",
          "👤 Personal administrativo: informes, registros, contacto clientes"
        ]),
        ("Áreas de trabajo (ISO 15189)", "grid", [
          "ÁREA TÉCNICA → Zona recepción y conservación (4°C) | Zona preparación y cultivo (cabina flujo laminar) | Zona de procesamiento | Zona de bandeo (tinción) | Zona conservación muestras procesadas",
          "ÁREA DE ESTUDIO → Búsqueda de metafases | Cariotipado | Interpretación de resultados | Redacción de informes"
        ]),
        ("Procedimientos Normalizados de Trabajo (PNT)", "", [
          "Protocolos basados en normativas vigentes (ISO 15189)",
          "Incluyen: micromatrices (microarrays), FISH, elaboración de cariotipos"
        ]),
        ("Materiales y equipo", "grid2", [
          ("🔬 Cariotipadores", "Microscopio + cámara + software de emparejamiento automático"),
          ("🧪 Frascos Roux", "Cultivo de células eucariotas, apilables, con tapón de rosca"),
          ("🧫 Tubos truncados", "Para volúmenes bajos de muestra, con lado plano"),
          ("💉 Contenedores de muestras", "Con anticoagulantes para sangre y médula ósea")
        ])
      ]),
      sec("1.2", "Organización del laboratorio de biología molecular", [
        ("Organigrama", "", [
          "Misma estructura jerárquica que citogenética",
          "Personal especializado en técnicas moleculares (PCR, secuenciación)"
        ]),
        ("Áreas de trabajo secuenciales (ISO 15189)", "flow", [
          "1️⃣ ÁREA PRE-PCR: Tratamiento de muestras, extracción ADN/ARN",
          "2️⃣ ÁREA DE AMPLIFICACIÓN: Pruebas de PCR",
          "3️⃣ ÁREA POST-AMPLIFICACIÓN: Sondas, electroforesis, secuenciación",
          "4️⃣ ÁREA NEUTRA: Reactivos y análisis de datos"
        ]),
        ("Equipo básico", "grid2", [
          ("🌡️ Termocicladores", "Ciclos de temperatura para PCR (95°C → 50-65°C → 72°C)"),
          ("🌀 Cabinas flujo laminar", "Esterilidad para manipulación de muestras"),
          ("⚡ Centrifugadoras", "Separación de componentes celulares"),
          ("❄️ Congeladores", "Almacenamiento a -20°C y -80°C")
        ])
      ]),
      sec("1.3", "Normas de manipulación y técnica aséptica", [
        ("Técnica aséptica", "check", [
          "✅ Trabajo en cabina de flujo laminar con flujo vertical",
          "✅ Desinfección con etanol 70% antes y después",
          "✅ Uso de guantes, bata con puños elásticos y mascarilla",
          "✅ Mechero Bunsen para crear barrera de esterilidad",
          "✅ Material estéril: pipetas, puntas con filtro, frascos",
          "✅ No hablar, toser ni estornudar sobre cultivos abiertos"
        ]),
        ("Prevención de contaminación", "", [
          "Contaminación cruzada: principal riesgo en laboratorios genéticos",
          "Limpieza de superficies con lejía 10% o etanol 70%",
          "Almacenamiento adecuado de reactivos en zonas designadas",
          "Flujo unidireccional de material: área limpia → área sucia"
        ])
      ]),
      sec("1.4", "Seguridad en el laboratorio", [
        ("Normas generales", "", [
          "Señalización de áreas de riesgo biológico y químico",
          "EPIs: bata, guantes, gafas de seguridad obligatorios",
          "Fichas de seguridad de reactivos (SDS) disponibles",
          "Lavado de ojos y duchas de emergencia señalizados",
          "Extintores, mantas ignífugas y botiquín"
        ]),
        ("Riesgos y niveles de bioseguridad", "table", [
          "Nivel 1 | Agentes no patógenos | Prácticas microbiológicas estándar",
          "Nivel 2 | Agentes de riesgo moderado | Cabina de seguridad + EPIs",
          "Nivel 3 | Agentes graves/potencialmente letales | Cabina + traje + presión negativa",
          "Nivel 4 | Agentes letales sin tratamiento | Aislamiento máximo"
        ])
      ]),
      sec("1.5", "Eliminación de residuos", [
        ("Clasificación", "table", [
          "♻️ Biológicos | Guantes, puntas, cultivos, muestras | Autoclavar antes de desechar",
          "🧪 Químicos | Fijadores, colorantes, solventes | Gestor autorizado de residuos",
          "⚠️ Cortopunzantes | Agujas, bisturís, vidrio roto | Contenedor rígido especial",
          "☣️ Radiactivos | Isótopos usados en marcaje | Normativa nuclear específica"
        ])
      ]),
      sec("1.6", "Dogma central y empaquetamiento del ADN", [
        ("Dogma central de la biología molecular", "diagram", [
          "🧬 REPLICACIÓN: ADN → ADN (duplicación del material genético)",
          "📝 TRANSCRIPCIÓN: ADN → ARNm (síntesis de ARN mensajero)",
          "🔧 TRADUCCIÓN: ARNm → Proteína (síntesis proteica en ribosomas)"
        ]),
        ("Empaquetamiento del ADN", "levels", [
          "Nivel 1️⃣: ADN (doble hélice, 2nm de diámetro)",
          "Nivel 2️⃣: Nucleosomas (ADN + histonas H2A, H2B, H3, H4) → fibra de 10nm",
          "Nivel 3️⃣: Fibra de 30nm (con histona H1 de empaquetamiento)",
          "Nivel 4️⃣: Asas de bucle (ancladas a matriz nuclear)",
          "Nivel 5️⃣: Cromosoma metafásico (máxima condensación)"
        ])
      ])
    ]
  },
  {
    "code": "U2",
    "title": "Realización de cultivos celulares",
    "emoji": "🔬",
    "desc": "Tipos celulares, medios de cultivo, siembra, mantenimiento, viabilidad y contaminación",
    "desc": "Tipos celulares, medios de cultivo, siembra, mantenimiento, viabilidad y contaminación en cultivos celulares",
    "sections": [
      sec("2.1", "Cultivos celulares en citogenética", [
        ("Tipos de células", "table", [
          "🧬 Eucariotas | Núcleo definido, orgánulos | Cultivadas en citogenética",
          "🦠 Procariotas | Sin núcleo | Bacterias, no en citogenética",
          "🔄 Totipotenciales | Cualquier tipo celular | Embrión temprano",
          "🎯 Pluripotenciales | Varios tipos | Células madre adultas",
          "✅ Diferenciadas | Tipo único | Células somáticas especializadas"
        ]),
        ("Medios de cultivo: componentes esenciales", "grid2", [
          ("💧 Hidratación", "Agua destilada estéril como base"),
          ("🧂 Sales minerales", "Equilibrio osmótico y electrolítico"),
          ("🎯 pH 7.2-7.4", "Tampón HEPES para estabilidad"),
          ("🍬 Nutrientes", "Glucosa, L-glutamina, vitaminas"),
          ("🧪 Suero fetal bovino", "10-30% del medio, composición no replicable artificialmente"),
          ("💊 Antibióticos", "Penicilina + estreptomicina anti-contaminación")
        ]),
        ("Agentes mitógenos", "", [
          "Inducen mitosis (división celular)",
          "Fitohemaglutinina A (PHA): más usada en citogenética",
          "Activa linfocitos T en 48h, ciclos de 24h después",
          "Permite cosechar cultivos a las 48h, 72h o 96h"
        ])
      ]),
      sec("2.2", "Obtención, mantenimiento y propagación", [
        ("Obtención de muestras", "", [
          "Sangre periférica (más común, fácil acceso)",
          "Médula ósea (para trastornos hematológicos)",
          "Tejidos sólidos (biopsias, requieren disgregación)",
          "Siembra en medio Ham's F10 + suero + PHA"
        ]),
        ("Mantenimiento", "", [
          "Incubación a 37°C con 5% CO₂",
          "Renovación de medio cada 3-4 días (2x/semana)",
          "Observación microscópica periódica del crecimiento",
          "pH debe mantenerse entre 7.2-7.4"
        ]),
        ("Propagación (resiembra)", "steps", [
          "1️⃣ Añadir tripsina-EDTA para despegar células",
          "2️⃣ Incubar 3 minutos a 37°C",
          "3️⃣ Golpear suavemente el frasco",
          "4️⃣ Verificar desprendimiento al microscopio",
          "5️⃣ Añadir medio fresco + suero",
          "6️⃣ Sembrar en nuevo frasco a menor densidad"
        ]),
        ("Criopreservación", "", [
          "Congelación en nitrógeno líquido (-196°C)",
          "DMSO (dimetilsulfóxido) al 10% como crioprotector",
          "Congelación gradual (-1°C/min) para evitar daño celular",
          "Descongelación rápida a 37°C al recuperar"
        ])
      ]),
      sec("2.3", "Determinación del número y viabilidad celular", [
        ("Recuento celular", "", [
          "Cámara de Neubauer (hemocitómetro): cuadrícula de 9 cuadros grandes",
          "Mezclar 50µL de suspensión celular + 50µL de azul tripano (1:1)",
          "Cargar cámara, contar en 4 cuadros esquina",
          "Fórmula: (células contadas × 10⁴ × factor dilución) / nº cuadros"
        ]),
        ("Viabilidad y curva de crecimiento", "", [
          "Azul tripano: tiñe células muertas (membrana dañada)",
          "Viabilidad óptima: >90%",
          "Fases: Latencia (adaptación) → Exponencial (crecimiento) → Estacionaria (confluencia) → Muerte"
        ])
      ]),
      sec("2.4", "Contaminación en cultivos celulares", [
        ("Tipos de contaminación", "table", [
          "🦠 Bacteriana | Turbidez, pH ácido, medio amarillo | Antibióticos + técnica aséptica",
          "🍄 Fúngica | Micelio flotante, esporas | Limpieza exhaustiva, filtros HEPA",
          "🔬 Micoplasma | Invisible, altera metabolismo | Test PCR periódico, cuarentena",
          "⚠️ Cruzada | Otras líneas celulares | Buenas prácticas, tubos individuales"
        ]),
        ("Prevención y eliminación", "", [
          "Cabina de flujo laminar siempre encendida 15 min antes",
          "Antibióticos profilácticos en medio (penicilina/estreptomicina)",
          "Cuarentena de nuevas líneas celulares 2 semanas",
          "Autoclavar cultivos contaminados (121°C, 20 min, 15 PSI)",
          "Desinfección con lejía 10% de superficies afectadas"
        ])
      ])
    ]
  },
  {
    "code": "U3",
    "title": "Técnicas de análisis cromosómico",
    "emoji": "🧬",
    "desc": "Sacrificio, fijación, bandeado, nomenclatura, alteraciones, diagnóstico prenatal y cáncer",
    "desc": "Organización, áreas de trabajo, equipos, normativa de seguridad y eliminación de residuos en laboratorios genéticos",
    "sections": [
      sec("3.1", "Sacrificio celular y extensiones cromosómicas", [
        ("Protocolo de tripsinización (24h antes)", "steps", [
          "1️⃣ Desechar medio de cultivo, añadir 1mL tripsina-EDTA",
          "2️⃣ Lavar y desechar sin dañar la monocapa",
          "3️⃣ Adicionar 2mL tripsina-EDTA nueva",
          "4️⃣ Incubar 3 min a 37°C en incubadora",
          "5️⃣ Golpear suavemente el frasco para despegue",
          "6️⃣ Añadir 3mL de medio con suero para inactivar tripsina"
        ]),
        ("Sacrificio y obtención de cromosomas metafásicos", "steps", [
          "1️⃣ Repetir tripsinización",
          "2️⃣ Añadir 3mL de medio SIN suero bovino fetal",
          "3️⃣ Centrifugar 10 min a 1000 rpm",
          "4️⃣ Retirar sobrenadante, resuspender pellet",
          "5️⃣ Añadir KCl 0.075M (choque hipotónico) gota a gota, 15 min 37°C",
          "6️⃣ Añadir fijador (metanol:ácido acético 3:1) gota a gota",
          "7️⃣ Centrifugar y lavar con fijador 3 veces",
          "8️⃣ Conservar a 4°C hasta extensión"
        ]),
        ("Fijación y extensión", "grid2", [
          ("💧 Método húmedo", "3 gotas en portaobjetos, evaporación lenta, placa caliente"),
          ("🔥 Método seco", "Pasar portaobjetos por llama Bunsen rápidamente, más rápido")
        ])
      ]),
      sec("3.2", "Métodos de bandeado cromosómico", [
        ("CTG — Bandeo G", "", [
          "Tripsina + Giemsa: tiñe zonas ricas en A-T (oscuras)",
          "Zonas G-C quedan claras → patrón de bandas único por cromosoma",
          "Protocolo: calentar 16h 60°C → tripsina 18-28s 37°C → Giemsa 2% 10min"
        ]),
        ("CGB — Bandeo C", "", [
          "HCl + Ba(OH)₂ + Giemsa: destaca heterocromatina centromérica",
          "Protocolo: HCl 0.2N 30min → Ba(OH)₂ 37°C 10-15min → 2X SSC 65°C 2h → Giemsa 45min"
        ]),
        ("NOR — Regiones organizadores nucleolares", "", [
          "Nitrato de plata (AgNO₃): visualiza cromosomas acrocéntricos",
          "Protocolo: gelatina + AgNO₃ → 70°C hasta pardo → Giemsa 45s",
          "Detecta heteromorfismos (variantes morfológicas puntuales)"
        ])
      ]),
      sec("3.3", "Nomenclatura y alteraciones cromosómicas", [
        ("Sistema ISCN", "", [
          "Fórmula: número total + cromosomas sexuales + alteraciones",
          "46,XY = varón sano | 46,XX = mujer sana",
          "47,XX,+21 = Síndrome de Down | 45,X = Turner",
          "Brazos: p (corto), q (largo). Ej: 46,XY,del(5)(p15.3)"
        ]),
        ("Alteraciones numéricas", "table", [
          "Euploidías | Juegos completos extra | Triploidía 3n(69), Tetraploidía 4n(92)",
          "Aneuploidías | Ganancia/pérdida parcial | Monosomías 2n-1(45), Trisomías 2n+1(47)",
          "Síndrome Down | Trisomía 21 | 47,XX,+21 o 47,XY,+21",
          "Síndrome Edwards | Trisomía 18 | 47,XX,+18 o 47,XY,+18",
          "Síndrome Turner | Monosomía X | 45,X",
          "Síndrome Klinefelter | XXY | 47,XXY"
        ]),
        ("Alteraciones estructurales", "grid", [
          "🔄 Translocación: intercambio de segmentos entre cromosomas",
          "📥 Inserción: un segmento se integra en otro cromosoma",
          "🔃 Inversión: segmento rotado 180° dentro del mismo cromosoma",
          "✂️ Deleción: pérdida de un segmento (ej: Cri-du-chat 5p-)",
          "📋 Duplicación: segmento repetido (cromosoma más largo)",
          "⭕ Anillo: extremos rotos se unen formando círculo",
          "⚖️ Isocromosoma: dos copias del mismo brazo (p o q)"
        ])
      ]),
      sec("3.4", "Diagnóstico prenatal y cáncer", [
        ("Factores de riesgo prenatal", "", [
          "Edad materna avanzada (>35 años)",
          "Antecedentes de anomalías genéticas",
          "Malformaciones en ecografías",
          "Antecedentes familiares de enfermedades cromosómicas"
        ]),
        ("Métodos invasivos vs no invasivos", "table", [
          "🩺 Amniocentesis | Sem 15-17 | Punción líquido amniótico | Riesgo bajo",
          "🧬 Biopsia corial | Sem 11-14 | Tejido placentario | Riesgo moderado",
          "🩸 Funiculocentesis | Sem 18+ | Sangre cordón umbilical | Riesgo moderado",
          "💉 No invasivo (NIPT) | Sem 10+ | Sangre materna | Sin riesgo, >95% fiabilidad"
        ]),
        ("Citogenética y cáncer", "", [
          "Alteraciones cromosómicas asociadas a leucemias, linfomas y tumores sólidos",
          "Translocaciones características: cromosoma Filadelfia (t(9;22)) en leucemia mieloide crónica",
          "Diagnóstico, clasificación pronóstica y desarrollo de terapias dirigidas"
        ])
      ])
    ]
  },
  {
    "code": "U4",
    "title": "Técnicas de extracción de ácidos nucleicos",
    "emoji": "🧪",
    "desc": "Lisis, fenol-cloroformo, columnas, kits, sistemas automáticos y extracción de ARN",
    "desc": "Lisis celular, purificación, métodos fenol-cloroformo, columnas de afinidad, kits y sistemas automáticos",
    "sections": [
      sec("4.1", "Fundamentos de la extracción", [
        ("Lisis celular", "table", [
          "🔨 Mecánica | Homogeneización, sonicación | Rápida, no química | Puede degradar ADN",
          "🧪 Química | Detergentes (SDS, Triton X-100) + tampón | Suave, controlable | Requiere proteinasa",
          "🧬 Enzimática | Proteinasa K, lisozima | Específica, eficiente | Más lenta, costosa"
        ]),
        ("Inactivación de nucleasas", "", [
          "EDTA: quelante de Mg²⁺, inhibe DNAsas (necesitan Mg²⁺)",
          "Proteinasa K: digiere proteínas incluyendo nucleasas",
          "Para ARN: ambiente libre de RNAsas, DEPC, trabajar en hielo",
          "Calor (65-95°C) desnaturaliza enzimas"
        ]),
        ("Purificación: separación de proteínas y lípidos", "", [
          "Fenol-cloroformo: desnaturaliza proteínas, separación de fases",
          "Columnas de sílice: unión selectiva de ADN/ARN a alta salinidad",
          "Precipitación: etanol 100% o isopropanol + sales (NaCl, acetato sódico)",
          "Lavado con etanol 70% para eliminar sales"
        ])
      ]),
      sec("4.2", "Métodos de extracción", [
        ("Fenol-cloroformo (método clásico)", "steps", [
          "1️⃣ Mezclar lisado celular con fenol:cloroformo:isoamílico (25:24:1)",
          "2️⃣ Agitar vigorosamente 15s y centrifugar 5 min a 12000g",
          "3️⃣ Recoger fase acuosa superior (contiene ADN)",
          "4️⃣ Precipitar con etanol 100% + acetato sódico 3M",
          "5️⃣ Incubar 30 min a -20°C, centrifugar 10 min",
          "6️⃣ Lavar pellet con etanol 70%, secar y resuspender en TE/agua"
        ]),
        ("Columnas de sílice (kits comerciales)", "", [
          "Membrana de sílice en columna de microcentrífuga",
          "Unión: alta concentración de sales caotrópicas (guanidina HCl)",
          "Lavado: etanol 70% elimina impurezas",
          "Elución: tampón TE o agua libre de nucleasas",
          "Rápido (<30 min), alta pureza, reproducible"
        ]),
        ("Sistemas automáticos", "", [
          "KingFisher (Thermo), Maxwell (Promega), QIAcube (Qiagen)",
          "Bolas magnéticas: partículas paramagnéticas recubiertas de sílice",
          "Procesan 24-96 muestras simultáneamente",
          "Reducen error humano y aumentan reproducibilidad"
        ])
      ]),
      sec("4.3", "Extracción de ARN", [
        ("Método Trizol (fenol ácido)", "steps", [
          "1️⃣ Homogeneizar muestra en Trizol (isotiocianato de guanidina + fenol)",
          "2️⃣ Añadir cloroformo, agitar y centrifugar",
          "3️⃣ Fase acuosa (superior) contiene ARN",
          "4️⃣ Precipitar con isopropanol, incubar 10 min",
          "5️⃣ Lavar con etanol 75%, secar y resuspender en agua DEPC"
        ]),
        ("Cuidados críticos para ARN", "", [
          "Trabajar en condiciones libres de RNAsas (guantes cambiados frecuentemente)",
          "Agua y soluciones tratadas con DEPC (dietil pirocarbonato)",
          "Material estéril y de un solo uso",
          "Todo el proceso en hielo o 4°C",
          "Almacenamiento a -80°C (máximo 1 año)"
        ])
      ])
    ]
  },
  {
    "code": "U5",
    "title": "Técnicas de PCR y electroforesis",
    "emoji": "🧬",
    "desc": "PCR, componentes, etapas, variantes (Nested, Multiplex, qPCR) y electroforesis",
    "desc": "Organización, áreas de trabajo, equipos, normativa de seguridad y eliminación de residuos en laboratorios genéticos",
    "sections": [
      sec("5.1", "Reacción en Cadena de la Polimerasa (PCR)", [
        ("Componentes de la PCR", "grid2", [
          ("🧬 ADN molde", "La secuencia a amplificar (1-100ng)"),
          ("🧪 Taq polimerasa", "Termoestable, óptimo 72°C, de Thermus aquaticus"),
          ("🎯 Cebadores (primers)", "18-22 nucleótidos, Tm 50-65°C, específicos"),
          ("🧫 dNTPs", "dATP, dCTP, dGTP, dTTP (200µM c/u)"),
          ("🧴 Buffer PCR", "Tris-HCl pH 8.4, KCl, MgCl₂ (1.5-3mM)"),
          ("💧 Agua", "Libre de nucleasas, calidad molecular")
        ]),
        ("Etapas del ciclo térmico", "steps", [
          "🌡️ DESNATURALIZACIÓN INICIAL: 94-98°C, 2-5 min (abrir cadena ADN)",
          "🔄 CICLOS (25-35 repeticiones):",
          "   🔥 Desnaturalización: 94-98°C, 20-30s",
          "   🧲 Alineamiento: 50-65°C, 20-40s (cebadores se unen)",
          "   ⚡ Extensión: 72°C, 30s-1min/kb (Taq polimerasa sintetiza)",
          "🌡️ EXTENSIÓN FINAL: 72°C, 5-10 min (completar productos)",
          "🧊 CONSERVACIÓN: 4-12°C (hold infinito)"
        ]),
        ("Problemas frecuentes y soluciones", "table", [
          "❌ Sin producto | Inhibidores en muestra, molde degradado | Purificar ADN, rediseñar cebadores",
          "🎯 Bandas inespecíficas | Temperatura alineamiento baja, Mg²⁺ alto | Aumentar Tm, reducir Mg²⁺",
          "📏 Dímeros de cebadores | Complementariedad entre primers | Rediseñar, usar Touchdown PCR",
          "🧟 Contaminación | ADN de otras muestras | Áreas separadas, puntas con filtro"
        ])
      ]),
      sec("5.2", "Variantes de PCR", [
        ("PCR anidada (Nested)", "", [
          "Dos rondas de PCR con dos pares de cebadores (externos e internos)",
          "El producto de la 1ª PCR sirve de molde para la 2ª",
          "Mayor especificidad y sensibilidad",
          "Ideal para muestras degradadas o con baja concentración de ADN"
        ]),
        ("PCR multiplex", "", [
          "Varios pares de cebadores en una misma reacción",
          "Amplifica múltiples dianas simultáneamente",
          "Aplicaciones: diagnóstico de patógenos, genotipado",
          "Crucial: optimizar Tm para todos los pares"
        ]),
        ("PCR a tiempo real (qPCR)", "grid2", [
          ("💚 SYBR Green", "Fluorescencia se une a ADN bicatenario, inespecífica"),
          ("🎯 TaqMan", "Sonda específica con fluoróforo + quencher, más precisa"),
          ("📈 Curva de amplificación", "Ct (cycle threshold): ciclo donde fluorescencia supera umbral"),
          ("📊 Cuantificación", "Absoluta (curva estándar) o relativa (ΔΔCt, con gen referencia)")
        ]),
        ("RT-PCR y RT-qPCR", "", [
          "RT (retrotranscripción): ARN → ADNc con transcriptasa inversa",
          "RT-PCR: cualitativo, detecta presencia de ARN",
          "RT-qPCR: cuantitativo, mide expresión génica",
          "Aplicaciones: expresión génica, detección virus ARN (como SARS-CoV-2)"
        ])
      ]),
      sec("5.3", "Electroforesis en gel de agarosa", [
        ("Fundamento", "", [
          "Separación de fragmentos de ADN por tamaño en matriz de agarosa",
          "ADN (cargado negativamente) migra hacia el ánodo (+)",
          "Fragmentos pequeños migran más rápido que los grandes",
          "Concentración de agarosa: 0.7% (grandes) a 3% (pequeños)"
        ]),
        ("Procedimiento", "steps", [
          "1️⃣ Preparar gel: agarosa + TAE/TBE, calentar, añadir bromuro de etidio",
          "2️⃣ Verter en cubeta con peine, dejar solidificar 30 min",
          "3️⃣ Cubrir con tampón TAE/TBE, retirar peine",
          "4️⃣ Cargar muestras + marcador de peso molecular (ladder)",
          "5️⃣ Correr a 5-10 V/cm durante 30-60 min",
          "6️⃣ Visualizar en transiluminador UV (312nm) y fotografiar"
        ])
      ])
    ]
  },
  {
    "code": "U6",
    "title": "Técnicas de hibridación con sonda",
    "emoji": "🔬",
    "desc": "Sondas, Southern/Northern blot, FISH, micromatrices y microarrays",
    "desc": "Tipos celulares, medios de cultivo, siembra, mantenimiento, viabilidad y contaminación en cultivos celulares",
    "sections": [
      sec("6.1", "Sondas y fundamentos de hibridación", [
        ("Sondas moleculares", "grid2", [
          ("🧬 ADN/ARN sonda", "Fragmento complementario a secuencia diana (20-1000nt)"),
          ("🏷️ Marcaje isotópico", "³²P (radiactivo, autorradiografía) — alta sensibilidad"),
          ("🌈 Marcaje fluorescente", "Cy3 (verde), Cy5 (rojo), FITC, Texas Red — múltiples colores"),
          ("🧪 Marcaje enzimático", "Fosfatasa alcalina, peroxidasa — detección colorimétrica")
        ]),
        ("Métodos de marcaje", "", [
          "Marcaje en extremo: quinasa (5') o transferasa terminal (3')",
          "Random priming: cebadores aleatorios + Klenow + dNTPs marcados",
          "Nick translation: DNasa I + ADN polimerasa I",
          "Transcripción in vitro: ARN polimerasa + NTPs marcados"
        ]),
        ("Procedimiento general de hibridación", "steps", [
          "1️⃣ Desnaturalizar ADN diana (95°C, 5 min)",
          "2️⃣ Aplicar sonda marcada en exceso",
          "3️⃣ Incubar a Tm-5°C durante 4-16h",
          "4️⃣ Lavados de baja stringencia (alta sal, baja T°)",
          "5️⃣ Lavados de alta stringencia (baja sal, alta T°) — elimina uniones inespecíficas",
          "6️⃣ Revelado: autorradiografía, escáner fluorescencia o detección enzimática"
        ])
      ]),
      sec("6.2", "Southern blot y Northern blot", [
        ("Southern blot (ADN)", "steps", [
          "1️⃣ Digestión de ADN genómico con enzimas de restricción",
          "2️⃣ Electroforesis en gel de agarosa",
          "3️⃣ Desnaturalización alcalina (NaOH) del ADN en gel",
          "4️⃣ Transferencia por capilaridad a membrana de nylon",
          "5️⃣ Hibridación con sonda marcada (16h, 42°C)",
          "6️⃣ Lavados y revelado (autorradiografía o quimioluminiscencia)"
        ]),
        ("Northern blot (ARN)", "", [
          "Similar a Southern pero con ARN como diana",
          "Electroforesis en gel desnaturalizante (formaldehído)",
          "Transferencia, hibridación y revelado igual que Southern",
          "Permite cuantificar expresión génica y detectar variantes de splicing"
        ]),
        ("Aplicaciones comparadas", "table", [
          "🧬 Southern | ADN | Detección de genes, RFLP, fingerprinting",
          "📝 Northern | ARN | Expresión génica, tamaño ARNm, splicing",
          "⚡ Western | Proteínas | Detección de proteínas (no hibridación)"
        ])
      ]),
      sec("6.3", "Hibridación in situ (FISH)", [
        ("FISH convencional", "", [
          "Sonda marcada con fluoróforo (espectro visible)",
          "Desnaturalización de ADN cromosómico in situ (sobre portaobjetos)",
          "Hibridación a 37°C durante 16h",
          "Lavados post-hibridación para eliminar sonda no unida",
          "Contrateñido con DAPI (tiñe todos los núcleos de azul)",
          "Visualización en microscopio de fluorescencia con filtros específicos"
        ]),
        ("Tipos de sondas FISH", "table", [
          "🎯 Centroméricas | Secuencias alfa-satélite, identificación cromosómica",
          "📍 Locus específico | BACs, YACs, detectan genes o regiones concretas",
          "🎨 Paint (pintado) | Cubren cromosoma completo, detectan translocaciones",
          "🏁 Teloméricas | Extremos cromosómicos, detectan deleciones"
        ]),
        ("Técnicas derivadas", "grid", [
          "🌈 M-FISH: 24 colores diferentes, cada cromosoma un color, detecta translocaciones complejas",
          "🔬 SKY: Espectro completo (espectrocariotipo), análisis por interferometría",
          "⚖️ CGH: ADN testigo vs paciente, detecta ganancias/pérdidas genómicas",
          "🧬 array-CGH: Microarray de CGH, alta resolución, múltiples sondas"
        ])
      ]),
      sec("6.4", "Micromatrices (microarrays)", [
        ("Fundamento", "", [
          "Miles de sondas inmovilizadas en soporte sólido (vidrio o silicio)",
          "Cada sonda representa un gen o secuencia específica",
          "Hibridación con ADNc marcado con Cy3/Cy5",
          "Escáner de fluorescencia mide intensidad por spot",
          "Análisis bioinformático: normalización, estadística, clustering"
        ]),
        ("Aplicaciones", "", [
          "Transcriptómica: expresión génica global (miles de genes a la vez)",
          "Genotipado: detección de SNPs (Single Nucleotide Polymorphisms)",
          "CGH-array: comparación genómica, detecta CNVs (Copy Number Variants)",
          "Epigenética: patrones de metilación del ADN",
          "Diagnóstico: perfiles de expresión en cáncer, clasificación molecular"
        ])
      ])
    ]
  },
  {
    "code": "U7",
    "title": "Métodos de clonación y secuenciación del ADN",
    "emoji": "🧬",
    "desc": "Vectores, enzimas restricción, clonación, Sanger, secuenciación automática y NGS",
    "desc": "Organización, áreas de trabajo, equipos, normativa de seguridad y eliminación de residuos en laboratorios genéticos",
    "sections": [
      sec("7.1", "Clonación de ADN", [
        ("Tipos de clonación", "", [
          "Clonación molecular: fragmento de ADN insertado en vector",
          "Clonación de organismos: célula completa (como Dolly la oveja)",
          "Clonación reproductiva: obtención de un organismo genéticamente idéntico",
          "Clonación terapéutica: obtención de células madre embrionarias"
        ]),
        ("Fases del procedimiento de clonación molecular", "steps", [
          "1️⃣ OBTENER EL INSERTO: mediante PCR o digestión con enzimas de restricción",
          "2️⃣ ELEGIR EL VECTOR: plásmido, fago, cósmido, BAC o YAC según tamaño",
          "3️⃣ DIGERIR: vector e inserto con la misma enzima de restricción (EcoRI, HindIII, BamHI)",
          "4️⃣ LIGAR: unir inserto + vector con ADN ligasa T4 (16°C, 1-16h)",
          "5️⃣ TRANSFORMAR: introducir en células competentes (E. coli, choque térmico 42°C)",
          "6️⃣ SELECCIONAR: antibiótico (ampicilina, kanamicina), X-gal (azul/blanco)",
          "7️⃣ VERIFICAR: PCR de colonia, digestión de restricción, secuenciación"
        ]),
        ("Vectores de clonación", "table", [
          "🧬 Plásmidos | 3-10 kb | pUC19, pBR322 | Fáciles, alta copia",
          "🧫 Fagos λ | 15-20 kb | λgt11, EMBL | Recombinación eficiente",
          "📦 Cósmidos | 35-45 kb | Supercos | Grandes insertos",
          "🧪 BAC | 100-300 kb | pBACe3.6 | Estables, genotecas genómicas",
          "⚗️ YAC | >300 kb | pYAC | Muy grandes pero frágiles"
        ])
      ]),
      sec("7.2", "Secuenciación de ADN", [
        ("Método de Sanger (dideoxi)", "steps", [
          "1️⃣ Preparar ADN molde + cebador + ADN polimerasa + dNTPs",
          "2️⃣ Añadir ddNTPs marcados (terminadores: ddATP, ddCTP, ddGTP, ddTTP)",
          "3️⃣ Ciclos de secuenciación: 96°C (desnaturar) → 50°C (alinear) → 60°C (extender)",
          "4️⃣ Los ddNTPs se incorporan aleatoriamente → terminan la elongación",
          "5️⃣ Electroforesis capilar separa fragmentos por tamaño",
          "6️⃣ Detección láser de fluorescencia → secuencia (cromatograma)",
          "7️⃣ Longitud: 500-1000 pb por reacción, precisión >99.9%"
        ]),
        ("Secuenciación automática 1ª generación", "", [
          "ddNTPs con 4 fluoróforos diferentes (A=verde, C=azul, G=negro/amarillo, T=rojo)",
          "Secuenciadores capilares (ABI 3730, 96-384 capilares)",
          "Detección por láser de argón durante la electroforesis",
          "Software analiza fluorescencia y genera secuencia + calidad",
          "Ideal para proyectos pequeños, verificación, diagnóstico clínico"
        ]),
        ("Secuenciación de nueva generación (NGS)", "grid2", [
          ("📖 Illumina (SBS)", "Síntesis por puentes, lecturas cortas (150pb×2), masivo"),
          ("⚡ Ion Torrent", "Detección de protones liberados, rápido, económico"),
          ("📏 PacBio (SMRT)", "Lecturas largas (>10kb), tiempo real, metilación"),
          ("🧬 Oxford Nanopore", "ADN pasa por nanoporos, lecturas ultra-largas (>100kb)")
        ]),
        ("Workflow de NGS", "steps", [
          "1️⃣ Fragmentación del ADN (enzimática o mecánica)",
          "2️⃣ Ligación de adaptadores específicos de la plataforma",
          "3️⃣ Amplificación (cluster generation en Illumina, bridge PCR)",
          "4️⃣ Secuenciación masiva en paralelo (millones de lecturas)",
          "5️⃣ Alineamiento con genoma de referencia o ensamblaje de novo",
          "6️⃣ Análisis bioinformático: variantes, expresión, metilación"
        ])
      ])
    ]
  }
]

# BUILD HTML
html = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Biología Molecular — Guía Interactiva</title>
<style>
:root{--bg:#0a0f1f;--card:#111827;--card2:#1a2332;--a:#00d4aa;--a2:#7c5bf0;--t:#e8ecf5;--t2:#8892b0;--b:#4a9eff;--y:#f5c842;--o:#ff9f43;--r:#ff6b6b}
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--t);min-height:100vh}
::selection{background:rgba(0,212,170,.25)}
.topbar{background:linear-gradient(135deg,#0a1025,#14203a);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,.06);position:sticky;top:0;z-index:100;flex-wrap:wrap;gap:8px}
.topbar h1{font-size:17px;font-weight:800;background:linear-gradient(135deg,var(--a),#48dbfb);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.topbar .sub{font-size:10px;color:var(--t2);-webkit-text-fill-color:var(--t2)}
.searchbox{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:8px 12px;color:var(--t);width:200px;font-size:12px;outline:none;transition:.3s}
.searchbox:focus{border-color:var(--a);background:rgba(0,212,170,.05);width:240px}
.searchbox::placeholder{color:var(--t2);opacity:.6}
.nav{display:flex;gap:5px;padding:10px 20px;background:rgba(10,14,26,.95);border-bottom:1px solid rgba(255,255,255,.04);position:sticky;top:47px;z-index:99;overflow-x:auto}
.nav-btn{padding:6px 14px;border-radius:8px;border:none;cursor:pointer;font-weight:600;font-size:11px;transition:.2s;background:var(--card);color:var(--t2);white-space:nowrap;flex-shrink:0}
.nav-btn:hover{background:var(--card2);transform:translateY(-1px)}
.nav-btn.active{background:linear-gradient(135deg,var(--a),#00b894);color:#0a0e1a;box-shadow:0 2px 12px rgba(0,212,170,.2)}
.main{max-width:1000px;margin:0 auto;padding:14px 18px 50px}
.unit{display:none;animation:fadeIn .3s}
.unit.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.hero{background:linear-gradient(135deg,var(--card),#0e1729);border-radius:12px;padding:20px 24px;margin-bottom:14px;border:1px solid rgba(255,255,255,.05)}
.hero h2{font-size:18px;font-weight:700;margin-bottom:5px}
.hero h2 .c{color:var(--a)}
.hero p{color:var(--t2);font-size:12px}
.badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.badge{padding:3px 9px;border-radius:5px;font-size:10px;font-weight:500}
.b1{background:rgba(0,212,170,.12);color:var(--a)}
.b2{background:rgba(74,158,255,.12);color:var(--b)}
.b3{background:rgba(124,91,240,.12);color:var(--a2)}
.secc{background:var(--card);border-radius:12px;margin-bottom:10px;border:1px solid rgba(255,255,255,.04);overflow:hidden}
.sech{display:flex;align-items:center;gap:8px;padding:12px 16px;cursor:pointer;user-select:none;transition:.15s;font-size:13px;font-weight:600}
.sech:hover{background:rgba(255,255,255,.02)}
.sech .arrow{font-size:10px;transition:.2s;width:16px;text-align:center;color:var(--a);flex-shrink:0}
.sech .arrow.o{transform:rotate(90deg)}
.sech .num{color:var(--a);font-weight:700;min-width:30px;font-size:12px}
.secb{display:none;padding:0 16px 14px;border-top:1px solid rgba(255,255,255,.04);padding-top:10px}
.secb.open{display:block}
.stitle{padding:6px 10px;font-size:12px;font-weight:600;color:var(--t);background:var(--card2);border-radius:6px;margin:8px 0 6px;display:flex;align-items:center;gap:6px;border-left:3px solid var(--a)}
.stitle.purple{border-left-color:var(--a2)}
.stitle.orange{border-left-color:var(--o)}
.cbody{padding:2px 6px}
.cbody p{font-size:12px;line-height:1.65;color:var(--t2);margin-bottom:6px}
.cbody ul{list-style:none;padding:0 4px}
.cbody ul li{font-size:12px;color:var(--t2);padding:3px 0 3px 18px;position:relative;line-height:1.5}
.cbody ul li::before{content:"▸";position:absolute;left:2px;color:var(--a);font-weight:700}
.tbl{overflow-x:auto;margin:6px 0;border-radius:6px;font-size:11px}
.tbl table{width:100%;border-collapse:collapse}
.tbl th{background:var(--card2);color:var(--a);padding:6px 10px;text-align:left;font-weight:600;border-bottom:1px solid rgba(0,212,170,.15);white-space:nowrap;font-size:11px}
.tbl td{padding:5px 10px;border-bottom:1px solid rgba(255,255,255,.04);color:var(--t2);vertical-align:top}
.tbl tr:hover td{background:rgba(0,212,170,.03)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:6px 0}
.gitem{padding:8px 10px;background:var(--card2);border-radius:6px;border:1px solid rgba(255,255,255,.04)}
.gitem .gl{color:var(--a);font-size:11px;font-weight:600;margin-bottom:2px}
.gitem .gv{color:var(--t2);font-size:11px;line-height:1.4}
.dia{display:flex;flex-direction:column;gap:4px;padding:8px 0}
.dstep{display:flex;align-items:center;gap:8px;padding:6px 10px;background:var(--card2);border-radius:6px;font-size:11px;color:var(--t2)}
.dstep .arr{color:var(--a);font-weight:700;min-width:20px}
.dstep:not(:last-child){margin-bottom:2px}
.dstep.s{margin-left:20px;background:rgba(0,212,170,.04);border-left:2px solid var(--a)}
.pwrap{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--card);border-radius:12px;border:1px solid rgba(255,255,255,.04);margin:14px 0 6px}
.pbar{flex:1;display:flex;gap:3px}
.pdot{height:4px;border-radius:2px;flex:1;background:var(--card2);transition:.3s}
.pdot.a{background:linear-gradient(90deg,var(--a),var(--b))}
.nava{display:flex;gap:5px}
.navb{width:28px;height:28px;border-radius:6px;border:1px solid rgba(255,255,255,.08);background:var(--card2);color:var(--t2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:13px;transition:.15s}
.navb:hover{background:var(--a);color:#0a0e1a;border-color:var(--a)}
.st{position:fixed;bottom:20px;right:20px;width:36px;height:36px;border-radius:50%;background:var(--a);color:#0a0e1a;border:none;cursor:pointer;font-size:18px;opacity:0;transition:.3s;pointer-events:none;z-index:50;box-shadow:0 3px 12px rgba(0,212,170,.3)}
.st.v{opacity:1;pointer-events:auto}
@media(max-width:768px){
  .topbar{padding:10px 14px}.searchbox{width:100%}.searchbox:focus{width:100%}
  .nav{top:42px;padding:8px 12px}
  .main{padding:10px 12px}.hero{padding:14px 16px}.hero h2{font-size:15px}
  .secc{padding:0}.sech{padding:10px 12px;font-size:12px}
  .grid2{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="topbar">
  <div><h1>🧬 Biología Molecular</h1><div class="sub">Guía interactiva de estudio • 7 unidades</div></div>
  <input class="searchbox" id="s" placeholder="🔍 Buscar..." oninput="su(this.value)">
</div>
<div class="nav" id="nav">'''

for i,u in enumerate(units):
    cl ='active' if i==0 else ''
    html+=f'<button class="nav-btn {cl}" onclick="x({i})"><b>{u["code"]}</b> {u["title"][:30]}…</button>'

html+='</div><div class="main" id="m">'

for ui,u in enumerate(units):
    cl='active' if ui==0 else ''
    html+=f'''<div class="unit {cl}" id="u{ui}">
<div class="hero"><h2>{u["emoji"]} <span class="c">{u["code"]}:</span> {u["title"][:70]}</h2><p>{u["desc"][:120]}</p>
<div class="badges"><span class="badge b1">📖 {len(u["sections"])} secciones</span>
<span class="badge b2">📄 {sum(len(s["content"]) for s in u["sections"])} temas</span>
<span class="badge b3">🔬 Laboratorio</span></div></div>'''

    for si,s in enumerate(u["sections"]):
        total_sub = len(s["content"])
        html+=f'''<div class="secc">
<div class="sech" onclick="tsec(this)"><span class="arrow">▶</span><span class="num">{s["num"]}</span>{s["title"][:55]}</div>
<div class="secb">'''
        for subnum, subt, items in s["content"]:
            hclass = "purple" if subnum else "orange"
            html+=f'<div class="stitle {hclass}">{subnum if subnum else "✦"} {subt}</div><div class="cbody">'
            if isinstance(items, list):
                if len(items) > 0 and "|" in str(items[0]):
                    # table format
                    html+='<div class="tbl"><table><tbody>'
                    for it in items:
                        cells = it.split("|")
                        html+='<tr>'
                        for c in cells:
                            html+=f'<td>{c.strip()}</td>'
                        html+='</tr>'
                    html+='</tbody></table></div>'
                elif subt == "grid" or subt == "levels":
                    html+='<div class="dia">'
                    for it in items:
                        html+=f'<div class="dstep"><span class="arr">→</span>{it}</div>'
                    html+='</div>'
                elif subt == "grid2":
                    html+='<div class="grid2">'
                    for it in items:
                        label, val = it[0], it[1]
                        html+=f'<div class="gitem"><div class="gl">{label}</div><div class="gv">{val}</div></div>'
                    html+='</div>'
                elif subt == "flow":
                    html+='<div class="dia">'
                    for it in items:
                        html+=f'<div class="dstep"><span class="arr">→</span>{it}</div>'
                    html+='</div>'
                elif subt == "diagram":
                    html+='<div class="dia">'
                    for it in items:
                        html+=f'<div class="dstep"><span class="arr">→</span>{it}</div>'
                    html+='</div>'
                elif subt == "check":
                    html+='<ul>'
                    for it in items:
                        html+=f'<li>{it}</li>'
                    html+='</ul>'
                elif subt == "table":
                    html+='<div class="tbl"><table><tbody>'
                    for it in items:
                        cells = it.split("|")
                        html+='<tr>'
                        for c in cells:
                            html+=f'<td>{c.strip()}</td>'
                        html+='</tr>'
                    html+='</tbody></table></div>'
                elif subt == "steps":
                    html+='<div class="dia">'
                    for it in items:
                        is_sub = it.startswith("   ")
                        html+=f'<div class="dstep{" s" if is_sub else ""}"><span class="arr">{"↳" if is_sub else "→"}</span>{it.strip()}</div>'
                    html+='</div>'
                else: # regular list
                    html+='<ul>'
                    for it in items:
                        html+=f'<li>{it}</li>'
                    html+='</ul>'
            elif isinstance(items, str):
                html+=f'<p>{items}</p>'
            html+='</div>'
        html+='</div></div>'

    # Key Points section
    kp_data = [
        ("U1", ["Citogen\u00e9tica estudia cromosomas; Biolog\u00eda Molecular estudia ADN/ARN","\u00c1reas separadas: pre-PCR \u2192 amplificaci\u00f3n \u2192 post-PCR (flujo unidireccional)","Cabina flujo laminar + t\u00e9cnica as\u00e9ptica = base de esterilidad","PNT seg\u00fan ISO 15189 obligatorios en todo laboratorio gen\u00e9tico","Dogma central: ADN \u2192 ARN \u2192 Prote\u00edna","Empaquetamiento: ADN \u2192 Nucleosomas \u2192 Fibra 30nm \u2192 Cromosoma","Residuos biol\u00f3gicos: autoclave antes de desecho"]),
        ("U2", ["Cultivo = c\u00e9lulas eucariotas aisladas en medio con nutrientes","pH 7.2-7.4 con HEPES; suero fetal bovino 10-30% esencial","PHA induce mitosis en linfocitos T (cosecha a 48-72-96h)","Azul tripano: diferencia c\u00e9lulas vivas (no te\u00f1idas) de muertas","Curva: Latencia \u2192 Exponencial \u2192 Estacionaria \u2192 Muerte","Micoplasma: contaminaci\u00f3n invisible que altera metabolismo","Criopreservaci\u00f3n: N\u2082 l\u00edquido -196\u00b0C + DMSO 10%"]),
        ("U3", ["Choque hipot\u00f3nico KCl 0.075M expande c\u00e9lulas sin da\u00f1ar cromosomas","Fijador metanol:\u00e1cido ac\u00e9tico (3:1) clave para integridad","CTG (Giemsa+tripsina): bandas A-T oscuras, \u00fanicas por cromosoma","F\u00f3rmula normal: 46,XX (mujer) o 46,XY (var\u00f3n)","Trisom\u00eda 21 = Down (47,+21); Monosom\u00eda X = Turner (45,X)","Amniocentesis sem 15-17; biopsia corial sem 11-14","Translocaci\u00f3n Filadelfia t(9;22) en leucemia mieloide cr\u00f3nica"]),
        ("U4", ["Extracci\u00f3n ADN: Lisis \u2192 Inactivaci\u00f3n nucleasas \u2192 Purificaci\u00f3n","Fenol-cloroformo: ADN en fase acuosa, prote\u00ednas en interfase","EDTA inhibe DNAsas quelando Mg\u00b2\u207a; Proteinasa K digiere prote\u00ednas","Columnas s\u00edlice: alta salinidad une ADN, eluci\u00f3n en TE/agua","Para ARN: hielo, agua DEPC, ambiente libre de RNAsas","Ratio A260/A280 >1.8 = ADN puro; >2.0 = ARN puro","Sistemas autom\u00e1ticos: 24-96 muestras simult\u00e1neas"]),
        ("U5", ["PCR: Desnaturalizaci\u00f3n (95\u00b0C) \u2192 Alineamiento (50-65\u00b0C) \u2192 Extensi\u00f3n (72\u00b0C)","Taq polimerasa: termoestable (optimo 72\u00b0C), de Thermus aquaticus","qPCR con SYBR Green (inespec\u00edfico) o TaqMan (espec\u00edfico)","Ct: ciclo donde fluorescencia supera umbral","RT-qPCR: ARN \u2192 ADNc \u2192 cuantificaci\u00f3n de expresi\u00f3n g\u00e9nica","Agarosa 0.7-3% seg\u00fan fragmento; ADN migra al \u00e1nodo (+)","PCR anidada (Nested): 2 rondas, m\u00e1xima especificidad"]),
        ("U6", ["Sondas: fragmentos complementarios marcados con \u00b3\u00b2P o Cy3/Cy5","Southern blot: ADN digerido \u2192 gel \u2192 membrana \u2192 sonda","Northern blot: ARN en gel desnaturalizante (formaldeh\u00eddo)","FISH: sonda fluorescente in situ sobre cromosomas","M-FISH: 24 colores, 1 color por cromosoma","Microarrays: miles de sondas en soporte \u2192 esc\u00e1ner","CGH-array: detecta CNVs (ganancias/p\u00e9rdidas gen\u00f3micas)"]),
        ("U7", ["Clonaci\u00f3n: Insertar ADN en vector \u2192 ligar \u2192 transformar E. coli","Vectores: pl\u00e1smidos (3-10kb), fagos \u03bb (15-20kb), BACs (100-300kb)","Sanger: ddNTPs terminan elongaci\u00f3n \u2192 electroforesis capilar","Precisi\u00f3n Sanger >99.9%, lecturas de 500-1000 pb","NGS (Illumina): millones de lecturas en paralelo (SBS)","Workflow NGS: Fragmentar \u2192 Adaptadores \u2192 Cluster \u2192 Secuenciar","Nanopore: lecturas ultra-largas >100kb, tiempo real"])
    ]
    for kp_code, kp_list in kp_data:
        if kp_code == u["code"]:
            html+=f'''<div class="secc" style="border-left:3px solid var(--y)">
<div class="sech" onclick="tsec(this)"><span class="arrow">\u25b6</span><span class="num">\u2b50</span> Puntos Clave</div>
<div class="secb"><div class="stitle orange">Lo m\u00e1s importante de {kp_code}</div><div class="cbody"><ul>'''
            for kp in kp_list:
                html+=f'<li style="font-size:12px;color:var(--y);font-weight:500">{kp}</li>'
            html+='</ul></div></div></div>'
            break

    # Progress    html+=f'''<div class="pwrap">
<div class="pbar">'''
    for p in range(7):
        cl='a' if p<=ui else ''
        html+=f'<div class="pdot {cl}"></div>'
    html+=f'''</div><span style="font-size:10px;color:var(--t2)">{u["code"]}/7</span>
<div class="nava"><button class="navb" onclick="xma({ui-1},6)">‹</button>
<button class="navb" onclick="xmi({ui+1},6)">›</button></div></div></div>'''

html+='''</div><button class="st" id="st" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>
<script>
let cu=0;
function x(i){let u=document.getElementById('u'+i);let b=document.querySelectorAll('.nav-btn');
  document.querySelectorAll('.unit').forEach(e=>e.classList.remove('active'));
  b.forEach(e=>e.classList.remove('active'));
  if(u)u.classList.add('active');if(b[i])b[i].classList.add('active');cu=i;window.scrollTo({top:0,behavior:'smooth'});
}
function xma(i,m){if(i>=0)x(i)}
function xmi(i,m){if(i<=m)x(i)}
function su(q){q=q.toLowerCase().trim();
  if(!q){x(cu);return;}
  document.querySelectorAll('.unit').forEach((u,i)=>{
    let m=u.textContent.toLowerCase().includes(q);
    u.classList.toggle('active',m);
    let b=document.querySelectorAll('.nav-btn');
    if(b[i])b[i].classList.toggle('active',m);
  });
}
function tsec(el){let b=el.nextElementSibling;if(!b)return;
  b.classList.toggle('open');
  el.querySelector('.arrow').classList.toggle('o',b.classList.contains('open'));
}
window.addEventListener('scroll',()=>{document.getElementById('st').classList.toggle('v',window.scrollY>300)});
document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT')return;
  if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();x(Math.min(cu+1,6));}
  if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();x(Math.max(cu-1,0));}
});
let tx=0;
document.addEventListener('touchstart',e=>{tx=e.changedTouches[0].screenX});
document.addEventListener('touchend',e=>{
  if(e.target.tagName==='INPUT')return;
  let d=e.changedTouches[0].screenX-tx;
  if(Math.abs(d)>80)x(Math.max(0,Math.min(6,cu-(d>0?1:-1))));
});
</script>
</body>
</html>'''

with open('/home/jeikson/.openclaw/workspace/Biologia_Molecular_Guia_Estudio.html','w') as f:
    f.write(html)

total = sum(sum(len(s["content"]) for s in u["sections"]) for u in units)
print(f'✅ HTML: {len(html):,} chars | {len(units)} unidades | {sum(len(u["sections"]) for u in units)} secciones | {total} temas')
