#importar librerias
import streamlit as st 
import pandas as pd 
import plotly.express as px 

#iportar datos 
car_data = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv')

# Título principal
st.header('Explorador de Vehículos')

# Mostrar información del dataset
st.subheader('Información de los Autos')
st.write('**Columnas disponibles:**')
st.write(list(car_data.columns))

# Mostrar las primeras 5 filas
st.write('**Primeras 5 filas de información:**')
st.dataframe(car_data.head())

# Explorar los datos para configurar los filtros
st.subheader('Configuración de Filtros')

# Mostrar rangos de las variables numéricas
st.write('**Rangos de las variables:**')
st.write(f'Precio: ${car_data["price"].min():,.0f} - ${car_data["price"].max():,.0f}')
st.write(f'Año: {car_data["model_year"].min():.0f} - {car_data["model_year"].max():.0f}')
st.write(f'Kilometraje: {car_data["odometer"].min():,.0f} - {car_data["odometer"].max():,.0f} millas')
st.write(f'Cilindros: {car_data["cylinders"].min():.0f} - {car_data["cylinders"].max():.0f}')

# Sección de filtros interactivos
st.subheader('Filtros de Datos')

# Filtro por rango de precios
price_range = st.slider(
'Selecciona el rango de precios',
min_value=int(car_data['price'].min()),
max_value=int(car_data['price'].max()),
value=(int(car_data['price'].min()), int(car_data['price'].max()))
)

# Filtro por años
year_range = st.slider(
'Selecciona el rango de años',
min_value=int(car_data['model_year'].min()),
max_value=int(car_data['model_year'].max()),
value=(int(car_data['model_year'].min()), int(car_data['model_year'].max()))
)

# Aplicar filtros a los datos
filtered_data = car_data[
(car_data['price'] >= price_range[0]) & 
(car_data['price'] <= price_range[1]) &
(car_data['model_year'] >= year_range[0]) & 
(car_data['model_year'] <= year_range[1])
]

# Mostrar cuántos vehículos quedan después del filtro
st.write(f'**Vehículos mostrados: {len(filtered_data)} de {len(car_data)}**')
# Checkbox para histograma
build_histogram = st.checkbox('Mostrar histograma de precios')
if build_histogram:
        st.write('Distribución de precios de los vehículos')
        fig_hist = px.histogram(filtered_data, x="price", title="Distribución de Precios")
        st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Mostrar relación precio vs kilometraje')
if build_scatter:
        st.write('Relación entre precio y kilometraje')
        fig_scatter = px.scatter(filtered_data, x="odometer", y="price", title="Precio vs Kilometraje")
        st.plotly_chart(fig_scatter, use_container_width=True)