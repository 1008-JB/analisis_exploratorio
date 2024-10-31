import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.header("Insights en Ventas de Coches: Un Análisis Exploratorio")

# Leer los datos
car_data = pd.read_csv(
    r'C:\Users\BETY_\Downloads\Analisis de datos\Sprint 6 Herramientas de desarrollo de software\Proyecto_final\analisis_exploratorio\vehicles_us.csv'
)

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico de histograma interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión para el precio frente al odómetro')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    
    # Mostrar el gráfico de dispersión interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
