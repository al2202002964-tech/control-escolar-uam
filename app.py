import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Control Escolar UAM", page_icon="🏫", layout="centered")

# --- TÍTULO PRINCIPAL ---
st.title("🏫 Sistema de Administración de Bases de Datos")
st.subheader("Proyecto Control Escolar - UAM")

# Crear pestañas de navegación para organizar la app
tab1, tab2, tab3, tab4 = st.tabs(["📋 Iniciativa", "📺 Demostración", "📅 Cronograma", "💬 Comentarios"])

# --- PESTAÑA 1: INICIATIVA ---
with tab1:
    st.header("Descripción del Proyecto")
    st.write("""
    Este proyecto consiste en la creación de un sistema de administración de bases de datos centralizada 
    para el control escolar de la UAM, diseñado con el objetivo de almacenar, organizar y consultar 
    información académica de estudiantes, profesores, materias y calificaciones de manera eficiente y segura.
    """)
    
    st.markdown("### 🛠️ Características del Sistema:")
    st.markdown("- **Registro:** Alumnos y materias.")
    st.markdown("- **Control:** Gestión de calificaciones.")
    st.markdown("- **Reportes:** Consultas académicas y generación de reportes automáticos.")

# --- PESTAÑA 2: DEMOSTRACIÓN ---
with tab2:
    st.header("Funcionamiento de la Plataforma")
    st.write("Mira el video demostrativo sobre cómo opera el sistema de control escolar:")
    
    # Aquí pegas el enlace de tu video (por ahora tiene uno de ejemplo)
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    st.video(video_url)

# --- PESTAÑA 3: CRONOGRAMA ---
with tab3:
    st.header("Línea de Tiempo del Proyecto (4 Meses)")
    cronograma_data = {
        "Mes": ["Mes 1", "Mes 2", "Mes 3", "Mes 4"],
        "Actividad Planeada": [
            "Investigación y diseño de la base de datos.",
            "Desarrollo del sistema.",
            "Implementación de consultas y reportes.",
            "Pruebas y corrección de errores."
        ]
    }
    df_cronograma = pd.DataFrame(cronograma_data)
    st.table(df_cronograma)

# --- PESTAÑA 4: CAJA DE COMENTARIOS (Guardado local y 100% gratis) ---
with tab4:
    st.header("Dejanos tus propuestas de mejora")
    
    # Nombre del archivo local donde se guardarán las opiniones
    archivo_comentarios = "comentarios.csv"
    
    # Formulario de entrada
    with st.form("formulario_feedback", clear_on_submit=True):
        nombre = st.text_input("Tu Nombre:")
        mejora = st.text_area("Propuesta de mejora para la plataforma:")
        boton_enviar = st.form_submit_button("Enviar Comentario")
        
        if boton_enviar and nombre and mejora:
            nuevo_comentario = pd.DataFrame({
                "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
                "Nombre": [nombre],
                "Propuesta": [mejora]
            })
            # Guardar en el archivo CSV de forma local
            if not os.path.isfile(archivo_comentarios):
                nuevo_comentario.to_csv(archivo_comentarios, index=False)
            else:
                nuevo_comentario.to_csv(archivo_comentarios, mode='a', header=False, index=False)
            st.success("¡Gracias! Tu comentario ha sido guardado.")

    # Mostrar comentarios guardados
    st.subheader("💬 Comentarios anteriores:")
    if os.path.isfile(archivo_comentarios):
        df_comentarios = pd.read_csv(archivo_comentarios)
        # Mostrar del más nuevo al más viejo
        st.dataframe(df_comentarios.iloc[::-1], use_container_width=True)
    else:
        st.info("Aún no hay comentarios. ¡Sé el primero!")