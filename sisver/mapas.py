import pandas as pd
import folium
from folium.plugins import MarkerCluster
import geopandas as gpd

# Cargar el archivo Excel
data = pd.read_excel("E://files_pandas//sisver//Unidades.xlsx")

# Seleccionar columnas necesarias
data = data[['NOMBRE DE LA UNIDAD', 'LATITUD', 'LONGITUD']]

# Convertir las columnas de latitud y longitud a numérico
data['LATITUD'] = pd.to_numeric(data['LATITUD'], errors='coerce')
data['LONGITUD'] = pd.to_numeric(data['LONGITUD'], errors='coerce')

# Eliminar filas con valores NaN en las coordenadas
data = data.dropna(subset=['LATITUD', 'LONGITUD'])


gdf = gpd.read_file("E://files_pandas//sisver//muni_2018gw//muni_2018gw.shp")
municipio = gdf[gdf['NOM_MUN'] == 'Pachuca de Soto']

# Crear el mapa centrado en la ubicación media de los datos
mapa = folium.Map(location=[data['LATITUD'].mean(), data['LONGITUD'].mean()], zoom_start=12)

# Añadir capa de clúster
marker_cluster = MarkerCluster().add_to(mapa)

# Añadir puntos y círculos al mapa dentro de la capa de clúster
for _, row in data.iterrows():
    folium.Marker(
        location=[row['LATITUD'], row['LONGITUD']],
        popup=row['NOMBRE DE LA UNIDAD']
    ).add_to(marker_cluster)
    
    folium.Circle(
        location=[row['LATITUD'], row['LONGITUD']],
        radius=500,  # en metros, puedes ajustar según lo necesites
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(mapa)


folium.GeoJson(municipio).add_to(mapa)
# Guardar el mapa en un archivo HTML
mapa.save('E://files_pandas//sisver//mapa_localidades.html')

# Mostrar mensaje de éxito
print("El mapa se ha guardado exitosamente en 'mapa_localidades.html'")
