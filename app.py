import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header("Insights en Ventas de Coches: Un Análisis Exploratorio")

# Cargar los datos desde el archivo CSV
car_data = pd.read_csv(
    r'C:\Users\BETY_\Downloads\Analisis de datos\Sprint 6 Herramientas de desarrollo de software\Proyecto_final\analisis_exploratorio\vehicles_us.csv'
)

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

# Si la casilla de verificación del histograma está seleccionada
if build_histogram:
    # Mostrar mensaje de creación de histograma
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma usando Plotly
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

# Si la casilla de verificación del gráfico de dispersión está seleccionada
if build_scatter:
    # Mostrar mensaje de creación de gráfico de dispersión
    st.write('Creación de un gráfico de dispersión de precio vs. odómetro')
    
    # Crear el gráfico de dispersión usando Plotly
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro")
    
    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)
