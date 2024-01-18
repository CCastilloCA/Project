import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.checkbox('Mostrar Histograma')  # casilla de verificación para histograma
scatter_button = st.checkbox('Mostrar Gráfico de Dispersión')  # casilla de verificación para gráfico de dispersión

if hist_button:  # si se selecciona la casilla de verificación de histograma
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:  # si se selecciona la casilla de verificación de gráfico de dispersión
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year", y="price", color="fuel")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)