import pandas as pd
import unicodedata
import matplotlib.pyplot as plt

# Función para limpiar valores
def limpiar_valores(value):
    if isinstance(value, str):
        value = unicodedata.normalize('NFKD', value).encode('ascii', errors='ignore').decode('utf-8')
        value = value.strip()
    elif pd.isnull(value):
        # Sustituir null por un espacio en blanco
        value = ''
    return value

# Función para clasificar en quinquenios
def clasificar(edad):
    if pd.isna(edad):
        return "desconocido"
    inicio = (edad // 5) * 5
    fin = inicio + 4
    return f'{inicio}-{fin}'

# Cargar el archivo Excel y limpiar valores
df = pd.read_excel("E://files_pandas//dengue//DENGUE141024.xlsx")
df = df.applymap(limpiar_valores)

# Filtrar valores específicos
df = df[df["DES_INS_UNIDAD"].str.strip().isin(["IMSS_OPD", "SSA"])]

# Seleccionar columnas necesarias
columnas = ["IDE_SEX", "IDE_EDA_ANO"]
df_edades = df[columnas]

# Agregar columna de quinquenios
df_edades['Quinquenio'] = df_edades['IDE_EDA_ANO'].apply(clasificar)

# Agrupar por quinquenio y contar valores
agrupado = df_edades.groupby('Quinquenio')['IDE_EDA_ANO'].count().reset_index(name='Count')


# Ordenar el DataFrame por la columna "Quinquenio" de menor a mayor 
agrupado['Quinquenio'] = pd.Categorical(agrupado['Quinquenio'], ordered=True, categories=sorted(agrupado['Quinquenio'].unique(), key=lambda x: int(x.split('-')[0]) if x != 'desconocido' else float('inf'))) 
agrupado = agrupado.sort_values('Quinquenio')

colors = plt.cm.tab20(range(len(agrupado)))


#Crear el gráfico 
plt.figure(figsize=(10, 6)) 
plt.bar(agrupado['Quinquenio'], agrupado['Count'], color=colors) 
plt.xlabel('Quinquenio') 
plt.ylabel('Count') 
plt.title('Distribución de edades por quinquenios') 
plt.xticks(rotation=90) 
plt.show()


