import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.header("Insights en Ventas de Coches: Un Análisis Exploratorio")

# Leer los datos
car_data = pd.read_csv(
    r'C:\Users\BETY_\Downloads\Analisis de datos\Sprint 6 Herramientas de desarrollo de software\Proyecto_final\analisis_exploratorio\vehicles_us.csv'
)

# Botones para construir gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:  # Al hacer clic en el botón de histograma
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Histograma de Odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button:  # Al hacer clic en el botón de gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Gráfico de Dispersión: Odometer vs Price")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

# Usar casillas de verificación
st.write("Selecciona el tipo de gráfico que deseas construir:")
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # Si la casilla de verificación está seleccionada
    st.write('Construyendo un histograma para la columna odómetro')
    fig_hist_checkbox = px.histogram(
        car_data, x="odometer", title="Histograma de Odometer")
    st.plotly_chart(fig_hist_checkbox, use_container_width=True)

if build_scatter:  # Si la casilla de verificación está seleccionada
    st.write('Construyendo un gráfico de dispersión para la columna odómetro y precio')
    fig_scatter_checkbox = px.scatter(
        car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Price")
    st.plotly_chart(fig_scatter_checkbox, use_container_width=True)
