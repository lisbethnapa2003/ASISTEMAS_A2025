
import streamlit as st

st.set_page_config(page_title="Auditoría de Servicios de TI", layout="wide")
st.title("Auditoría de Servicios de TI - Evaluación")

preguntas = [
    ("Mejora Continua", "¿Existe un proceso formal y documentado para identificar, registrar y priorizar oportunidades de mejora en los servicios de TI?"),
    ("Mejora Continua", "¿Se utilizan métricas y reportes de manera consistente para medir el progreso y demostrar el éxito de las iniciativas de mejora?"),
    ("Mejora Continua", "¿La cultura organizacional fomenta activamente la participación de todo el personal en las actividades de mejora continua?"),
    
    ("Control de Cambios", "¿La organización sigue un procedimiento formal para la gestión de todos los cambios de TI, incluyendo la evaluación de riesgos, el impacto y la autorización?"),
    ("Control de Cambios", "¿Se comunican eficazmente los cambios planificados y ejecutados a todas las partes interesadas relevantes para minimizar interrupciones?"),
    ("Control de Cambios", "¿Existe una clara distinción y un manejo adecuado para los diferentes tipos de cambio (estándar, normal y de emergencia)?"),

    ("Gestión de Incidentes", "¿Todos los incidentes son registrados, clasificados y priorizados de forma consistente según su impacto y urgencia?"),
    ("Gestión de Incidentes", "¿Se cuenta con un proceso documentado para la resolución de incidentes, incluyendo escalamiento, con el objetivo de restaurar el servicio dentro de los SLAs acordados?"),
    ("Gestión de Incidentes", "¿Se mantiene a los usuarios informados de manera proactiva sobre el estado y la resolución de sus incidentes?"),

    ("Gestión de Problemas", "¿Se lleva a cabo un análisis estructurado para identificar las causas raíz de los incidentes recurrentes o de alto impacto?"),
    ("Gestión de Problemas", "¿Se documentan y gestionan eficazmente las soluciones temporales (workarounds) y los errores conocidos (known errors)?"),
    ("Gestión de Problemas", "¿Se implementan soluciones permanentes para los problemas con el fin de prevenir la recurrencia de incidentes?"),

    ("Gestión de Solicitudes de Servicio", "¿Se dispone de un catálogo de servicios claro y accesible para que los usuarios puedan realizar solicitudes de servicio predefinidas?"),
    ("Gestión de Solicitudes de Servicio", "¿El proceso para cumplir con las solicitudes de servicio está estandarizado y, en la medida de lo posible, automatizado para garantizar eficiencia?"),
    ("Gestión de Solicitudes de Servicio", "¿Se establecen y comunican a los usuarios los tiempos esperados para el cumplimiento de cada tipo de solicitud de servicio?"),

    ("Mesa de Servicio", "¿La Mesa de Servicio actúa como un punto único de contacto (SPOC) eficaz y bien conocido para todas las consultas y reportes de los usuarios?"),
    ("Mesa de Servicio", "¿El personal de la Mesa de Servicio posee las habilidades (técnicas y de comunicación) y las herramientas necesarias para resolver un alto porcentaje de las solicitudes en el primer contacto?"),
    ("Mesa de Servicio", "¿Se mide y analiza de forma regular la satisfacción del usuario con el soporte proporcionado por la Mesa de Servicio para identificar áreas de mejora?"),

    ("Gestión de Nivel de Servicio", "¿Se han negociado, documentado y acordado formalmente los Acuerdos de Nivel de Servicio (SLA) con los clientes, basándose en los resultados de negocio?"),
    ("Gestión de Nivel de Servicio", "¿Se monitorea de manera continua el desempeño de los servicios y se compara con las metas establecidas en los SLAs?"),
    ("Gestión de Nivel de Servicio", "¿Se realizan revisiones periódicas de los SLAs con los clientes para asegurar que sigan siendo relevantes y que se esté entregando el valor esperado?")
]

opciones = [
    "1- No cumple",
    "2- Cumple parcialmente",
    "3- Cumple en gran medida",
    "4- Cumple totalmente",
    "5- Cumple y supera expectativas"
]

respuestas = {}

# Agrupar por dominio y mostrar
dominio_actual = None
for dominio, pregunta in preguntas:
    if dominio != dominio_actual:
        st.subheader(dominio)
        dominio_actual = dominio
    seleccion = st.radio(pregunta, opciones, key=pregunta)
    respuestas[pregunta] = seleccion

if st.button("Enviar"):
    st.success("Respuestas registradas con éxito. Aquí están tus resultados:")
    for pregunta, respuesta in respuestas.items():
        st.write(f"🔹 **{pregunta}** → _{respuesta}_")
