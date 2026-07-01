import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuración visual de la aplicación móvil (Diseño centrado para simular app de celular)
st.set_page_config(page_title="Control Escolar UAM", page_icon="🏫", layout="centered")

# --- TÍTULO PRINCIPAL ---
st.title("🏫 Sistema de Administración de Bases de Datos")
st.subheader("Proyecto Control Escolar - UAM")

# Crear pestañas de navegación adaptables a pantallas táctiles
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
    st.markdown("- **Registro:** Control automatizado de alumnos y materias.")
    st.markdown("- **Control:** Gestión transparente de calificaciones.")
    st.markdown("- **Reportes:** Consultas académicas rápidas y generación de reportes.")
    st.markdown("- **____________________________________________________________________________________________________________________")
    st.markdown("- **La importancia del servicio es primordial para la comunidad de los alumnos de la Universidad Autonoma Metropolitana")


# --- PESTAÑA 2: DESARROLLO DE LA PLATAFORMA---
with tab2:
    st.header("El enfoque principal del proyecto es desarrollarse conforme la metodologia PRINCE")
    st.write("Reproduce el video demostrativo para conocer la interfaz y operación del sistema:")
    
    # Intenta cargar tu video local 'Sistema_UAM.mp4'
    nombre_video = "Sistema_UAM.mp4"
    
    if os.path.isfile(nombre_video):
        video_local = open(nombre_video, "rb")
        st.video(video_local.read())
    else:
        st.error(f"⚠️ No se encontró el archivo '{nombre_video}' dentro de la carpeta. Asegúrate de copiarlo al lado de este código.")

# --- PESTAÑA 3: CRONOGRAMA ---
with tab3:
    st.header("Línea de Tiempo del Proyecto (4 Meses)")
    cronograma_data = {
        "Mes": ["Mes 1", "Mes 2", "Mes 3", "Mes 4"],
        "Actividad Planeada": [
            "Investigación y diseño de la base de datos.",
            "Desarrollo del sistema.",
            "Implementación de consultas y reportes.",
            "Pruebas de base de datos y corrección de errores."
        ]
    }
    df_cronograma = pd.DataFrame(cronograma_data)
    st.table(df_cronograma)

# --- PESTAÑA 4: CAJA DE COMENTARIOS ---
with tab4:
    st.header("Déjanos tus propuestas de mejora")
    
    archivo_comentarios = "comentarios.csv"
    
    # Formulario interactivo responsivo
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
            
            # Guardar comentario de forma local en formato CSV
            if not os.path.isfile(archivo_comentarios):
                nuevo_comentario.to_csv(archivo_comentarios, index=False)
            else:
                nuevo_comentario.to_csv(archivo_comentarios, mode='a', header=False, index=False)
            st.success("¡Gracias! Tu comentario ha sido guardado.")

    # Mostrar el historial de comentarios guardados
    st.subheader("💬 Comentarios anteriores:")
    if os.path.isfile(archivo_comentarios):
        df_comentarios = pd.read_csv(archivo_comentarios)
        st.dataframe(df_comentarios.iloc[::-1], use_container_width=True)
    else:
        st.info("Aún no hay comentarios. ¡Sé el primero en proponer una mejora!")