"""Capacitación virtual Ágora Tech — sistemas SALTO y HikVision.

Muestra la capacitación (archivo HTML autocontenido) dentro de Streamlit.
Versión por defecto: corporativa. Para la versión interactiva use ?version=interactiva
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Capacitación Ágora Tech", page_icon="🔑", layout="wide",
                   initial_sidebar_state="collapsed")

# Ocultar el menú y los márgenes de Streamlit para que se vea solo la capacitación
st.markdown("""
<style>
  #MainMenu, header, footer {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  iframe {display: block;}
</style>
""", unsafe_allow_html=True)

ARCHIVOS = {
    "corporativa": "capacitacion_corporativa.html",
    "interactiva": "capacitacion_interactiva.html",
}
version = st.query_params.get("version", "corporativa")
archivo = ARCHIVOS.get(version, ARCHIVOS["corporativa"])

def leer(nombre: str) -> str:
    # Sin caché: así cada cambio subido a GitHub se ve de inmediato
    return (Path(__file__).parent / nombre).read_text(encoding="utf-8")

components.html(leer(archivo), height=900, scrolling=True)
