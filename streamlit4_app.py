import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Auditoría TI", layout="wide")
st.title("🧩 Evaluación de Auditoría de Servicios de TI")

# Definir preguntas y dominios directamente (lista de diccionarios)
preguntas = [
    {"Dominio": "Seguridad", "Pregunta": "¿Se implementan políticas de acceso seguras?"},
    {"Dominio": "Seguridad", "Pregunta": "¿Se realizan auditorías periódicas de seguridad?"},
    {"Dominio": "Infraestructura", "Pregunta": "¿La infraestructura TI está actualizada?"},
    {"Dominio": "Infraestructura", "Pregunta": "¿Se realizan backups frecuentes?"},
    {"Dominio": "Soporte", "Pregunta": "¿El equipo de soporte responde en tiempos adecuados?"},
    {"Dominio": "Soporte", "Pregunta": "¿Se documentan correctamente los incidentes?"},
]

st.markdown("---")
st.subheader("📋 Responde las preguntas:")

respuestas = []
for idx, item in enumerate(preguntas):
    puntuacion = st.slider(
        f"**{item['Dominio']}** - {item['Pregunta']}",
        min_value=1, max_value=5, value=3, step=1,
        key=f"slider_{idx}"
    )
    respuestas.append({
        "Dominio": item["Dominio"],
        "Pregunta": item["Pregunta"],
        "Respuesta": puntuacion
    })

if st.button("📊 Generar Informe"):
    df_resp = pd.DataFrame(respuestas)

    # Calcular promedio por dominio
    resumen = df_resp.groupby("Dominio")["Respuesta"].mean().reset_index()
    resumen.columns = ["Dominio", "Promedio"]
    
    st.markdown("### 🔎 Promedios por dominio")
    st.dataframe(resumen, use_container_width=True)

    # Selección tipo de gráfico
    chart_type = st.selectbox("Selecciona tipo de gráfico", ["Radar (Polar)", "Barras"])

    if chart_type == "Radar (Polar)":
        fig = px.line_polar(
            resumen,
            r='Promedio',
            theta='Dominio',
            line_close=True,
            range_r=[0, 5],
            title="Evaluación por Dominio",
            markers=True
        )
    else:
        fig = px.bar(
            resumen,
            x='Dominio',
            y='Promedio',
            title="Evaluación por Dominio",
            range_y=[0, 5],
            text_auto=True,
            color='Promedio',
            color_continuous_scale='Viridis'
        )
    st.plotly_chart(fig, use_container_width=True)

    # Indicadores tipo semáforo + interpretación
    st.markdown("### 🚦 Interpretación por dominio")
    for _, row in resumen.iterrows():
        promedio = row["Promedio"]
        dominio = row["Dominio"]

        if promedio < 2.1:
            st.error(f"🔴 {dominio}: Riesgo Alto ({promedio:.2f}) - Urgente mejora")
        elif promedio < 3.6:
            st.warning(f"🟡 {dominio}: Riesgo Medio ({promedio:.2f}) - Mejorar procesos")
        else:
            st.success(f"🟢 {dominio}: Cumplimiento Bueno ({promedio:.2f}) - Buen nivel")
