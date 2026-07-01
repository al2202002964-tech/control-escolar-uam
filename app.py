import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# Configuración visual de la aplicación móvil (Diseño centrado para simular app de celular)
st.set_page_config(page_title="Control Escolar UAM", page_icon="🏫", layout="centered")

# --- TÍTULO PRINCIPAL ---
st.title("🏫 Sistema de Administración de Bases de Datos")
st.subheader("Proyecto Control Escolar - UAM")

# Crear pestañas de navegación adaptables
tab1, tab2, tab3, tab4 = st.tabs(["📋 Iniciativa", "📺 Demostración", "📅 Cronograma", "💬 Comentarios"])

# --- PESTAÑA 1: INICIATIVA ---
with tab1:
    st.header("Descripción del Proyecto")
    st.write("""
    Este proyecto consiste en la creación de un sistema de administración de bases de datos centralizada 
    para el control escolar de la UAM, diseñado con el objetivo de almacenar, organizar y consultar 
    información académica de estudiantes, profesores, materias y calificaciones de manera eficiente y segura.
    """)
    
    st.markdown("### 🛠️ Características del Sistema (Técnica SMART):")
    st.markdown("- **Registro:** Control automatizado de alumnos y materias.")
    st.markdown("- **Control:** Gestión transparente de calificaciones.")
    st.markdown("- **Reportes:** Consultas académicas rápidas y generación de reportes.")

# --- PESTAÑA 2: DEMOSTRACIÓN (ENLACE DE YOUTUBE) ---
with tab2:
    st.header("Funcionamiento de la Plataforma")
    st.write("Reproduce el video demostrativo para conocer la interfaz y operación del sistema:")
    
    # Enlace actualizado de YouTube
    video_url = "https://youtu.be/S14FIITGbp0?si=tdB2F6qgpsBskefr"
    st.video(video_url)

# --- PESTAÑA 3: CRONOGRAMA COMPLETO (SEMANAS 1 A 12) ---
with tab3:
    st.header("📅 Calendario Completo del Proyecto")
    st.write("Línea de tiempo oficial del trimestre. Las semanas 1 a 8 ocurrieron antes del lunes de ayer:")

    # Base fija: Lunes de ayer (29 de Junio de 2026) es el inicio de la Semana 9
    lunes_semana_9 = datetime(2026, 6, 29)
    
    # Función para calcular los rangos de fechas (Lunes a Viernes) hacia atrás y hacia adelante
    def obtener_rango_semana(numero_semana):
        diferencia_semanas = numero_semana - 9
        inicio = lunes_semana_9 + timedelta(weeks=diferencia_semanas)
        fin = inicio + timedelta(days=4) # De Lunes a Viernes
        return f"{inicio.strftime('%d/%b')} al {fin.strftime('%d/%b')}"

    # Lista de actividades reales para las 12 semanas de un proyecto de Base de Datos
    actividades = [
        "Definición del problema y requerimientos del control escolar.", # Sem 1
        "Planteamiento de reglas de negocio y restricciones de la UAM.", # Sem 2
        "Diseño del Modelo Entidad-Relación preliminar (Diagrama MER).", # Sem 3
        "Revisión de llaves primarias, foráneas y relaciones complejas.", # Sem 4
        "Proceso de Normalización de tablas (Evitar redundancia: 1FN, 2FN, 3FN).", # Sem 5
        "Traducción del modelo conceptual al Modelo Relacional definitivo.", # Sem 6
        "Elección del motor de BD e instalación del entorno local.", # Sem 7
        "Escritura de scripts DDL (CREATE TABLE) y restricciones (CHECK, UNIQUE).", # Sem 8
        "Puesta en marcha del servidor local y carga masiva de datos de prueba.", # Sem 9 (Ayer)
        "Creación de Vistas, Triggers y asignación de Roles/Permisos de usuarios.", # Sem 10
        "Pruebas de estrés de consultas complejas (Subconsultas y JOINs).", # Sem 11
        "Optimización de índices, auditoría final y entrega del proyecto." # Sem 12
    ]

    # Determinar estados dinámicamente según tu lógica escolar
    estados = []
    for i in range(1, 13):
        if i < 9:
            estados.append("Completado ✅")
        elif i == 9:
            estados.append("En Curso 🛠️")
        else:
            estados.append("Pendiente ⏳")

    # Armar el DataFrame con las 12 semanas completas
    datos_cronograma = {
        "Semana": [f"Semana {i}" for i in range(1, 13)],
        "Fechas": [obtener_rango_semana(i) for i in range(1, 13)],
        "Actividad / Hito del Proyecto": actividades,
        "Estado": estados
    }
    
    df_cronograma = pd.DataFrame(datos_cronograma)

    # Función de estilos CSS para pintar el calendario de colores pastel estilo App móvil
    def asignar_colores_filas(row):
        num_sem = int(row["Semana"].split(" ")[1])
        if num_sem < 9:
            # Semanas pasadas (1-8): Verde pastel suave indicando éxito
            estilo = "background-color: #E8F5E9; color: #2E7D32;"
        elif num_sem == 9:
            # Semana actual (9): Amarillo/Naranja de atención con bordes notables
            estilo = "background-color: #FFFDE7; color: #E65100; font-weight: bold; border: 2px solid #F57F17;"
        else:
            # Semanas futuras (10-12): Gris limpio de planificación
            estilo = "background-color: #FAFAFA; color: #616161; font-style: italic;"
        return [estilo] * len(row)

    # Aplicar diseño
    df_estilizado = df_cronograma.style.apply(asignar_colores_filas, axis=1)

    # Renderizar la tabla interactiva adaptada al ancho del teléfono
    st.dataframe(df_estilizado, use_container_width=True, hide_index=True)

# --- PESTAÑA 4: CAJA DE COMENTARIOS ---
with tab4:
    st.header("Déjanos tus propuestas de mejora")
    
    archivo_comentarios = "comentarios.csv"
    
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
            
            if not os.path.isfile(archivo_comentarios):
                nuevo_comentario.to_csv(archivo_comentarios, index=False)
            else:
                nuevo_comentario.to_csv(archivo_comentarios, mode='a', header=False, index=False)
            st.success("¡Gracias! Tu comentario ha sido guardado.")

    st.subheader("💬 Comentarios anteriores:")
    if os.path.isfile(archivo_comentarios):
        df_comentarios = pd.read_csv(archivo_comentarios)
        st.dataframe(df_comentarios.iloc[::-1], use_container_width=True)
    else:
        st.info("Aún no hay comentarios. ¡Sé el primero en proponer una mejora!")