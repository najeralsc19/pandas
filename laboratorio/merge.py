import pandas as pd
import openpyxl
import unicodedata

#Funcion limpiar valores
def limpiar_valores(value):
    if isinstance(value, str):
        value = unicodedata.normalize('NFKD', value).encode('ascii', errors='ignore').decode('utf-8')
    return value
#archivo a
file_a = "E://files_pandas//lab//Requerimientos_lab.xlsx"
hoja_a = "HIDALGO"
requerimientos = pd.read_excel(file_a, sheet_name=hoja_a)
requerimientos.columns = requerimientos.columns.str.strip().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
requerimientos = requerimientos.map(limpiar_valores)
#selecciona las columnas a usar 
columnas = ['CLUES', 'Nombre de la Unidad', 'Estudio*', 'Min 2025', 'Max 2025']
req_acotado = requerimientos[columnas]

#archivo b
file_b = "E://files_pandas//lab//3.-Anexo T1 Requerimientos SMI.xlsx"
hoja_b = "Hidalgo"
aprobado = pd.read_excel(file_b, sheet_name=hoja_b)
aprobado.columns = aprobado.columns.str.strip().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
aprobado = aprobado.map(limpiar_valores)
#columnas a usar 
columnas_a = ['CLUES', 'Nombre de la Unidad', 'Estudio*', 'Min 2025', 'Max 2025']
aprobado_acot = aprobado[columnas_a]

#merge con las columnas 

df_combinado = pd.merge(
    req_acotado,
    aprobado_acot[['CLUES','Estudio*', 'Min 2025', 'Max 2025']],
    on=['CLUES', 'Estudio*'],
    how='left',
    suffixes=('','_aprobado')
)
#columnas calculadas

df_combinado['Diferencia_min'] = df_combinado['Min 2025'] - df_combinado['Min 2025_aprobado']
df_combinado['Diferencia_max'] = df_combinado['Max 2025'] - df_combinado['Max 2025_aprobado']



ruta_guardado = 'E://files_pandas//lab//datos_combinados.xlsx'
df_combinado.to_excel(ruta_guardado, index=False)

