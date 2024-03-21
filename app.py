import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Crea un grafico")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir un histograma')
hist_button = st.button('Construir histograma') # crear un botón  


if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')    
    if hist_button: # al hacer clic en el botón
    # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
        fig = px.histogram(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
    
scatter_button = st.button('Construir grafico de dispersion') # crear un botón
if scatter_button: # al hacer clic en el botón
    # ecribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.scatter(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    