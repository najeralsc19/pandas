import pandas as pd
import os
import unicodedata

# Ruta al archivo de Excel original
file = os.path.join("E://files_pandas//dengue//DENGUE141024.xlsx")
sheet_n = "DENGUE141024"  # Nombre de la pestaña

def clasificar_quinquenio(edad):
    if pd.isna(edad):
        return "Desconocido"
    quinquenio_inicio = (edad // 5) * 5
    quinquenio_fin = quinquenio_inicio + 4
    return f"{quinquenio_inicio}-{quinquenio_fin}"

def limpiar_valores(value):
    if isinstance(value, str):
        value = unicodedata.normalize('NFKD', value).encode('ascii', errors='ignore').decode('utf-8')
        value = value.strip()
    elif pd.isnull(value): 
        # Sustituir null por un espacio en blanco 
        value = ''
    return value

try:
    # Cargar los datos en un DataFrame
    necesidades = pd.read_excel(file, sheet_name=sheet_n)
    
    # Limpiar espacios en los nombres de las columnas
    necesidades.columns = [col.strip() for col in necesidades.columns]
    
    # Seleccionar columnas específicas
    columnas_n = ["FOL_ID", "IDE_ID", "CVE_INF", "VEC_ID", "IDE_NOM", "IDE_APE_PAT", "IDE_APE_MAT", "RFC", "CURP", "IDE_FEC_NAC", "CVE_EDO_NAC", "DES_EDO_NAC", "CVE_MPO_NAC", "DES_MPO_NAC", "IDE_SEX", "IDE_EDA_ANO", "IDE_EDA_MES", "IDE_EDA_DIA", "DES_CAL", "IDE_CAL", "NUM_INT", "NUM_EXT", "IDE_COL", "CVE_EDO_RES", "DES_EDO_RES", "CVE_JUR_RES", "DES_JUR_RES", "CVE_MPO_RES", "DES_MPO_RES", "CVE_LOC_RES", "DES_LOC_RES", "IDE_TEL", "IDE_CALLE1", "IDE_CP", "ES_INDIGENA", "LENGUA_INDIGENA", "CUAL_LENGUA", "DES_CUAL_LENGUA", "CVE_OCUPACION", "DES_OCUPACION", "ESTATUS_CASO", "EXPEDIENTE", "CVE_EDO_TRABAJO", "CVE_UNI_MED_NOTIF", "DES_UNI_MED_NOTIF", "CVE_EDO_UNIDAD", "DES_EDO_UNIDAD", "DES_JUR_UNIDAD", "DES_MPO_UNIDAD", "DES_INS_UNIDAD", "FEC_NOTIF_DGE", "DES_DIAG_FINAL", "FEC_INI_SIGNOS_SINT", "SEM", "EMBARAZO", "SEM_GEST"]
    df_necesidades = necesidades[columnas_n]
    
    df_necesidades = df_necesidades.map(limpiar_valores)
 
    # Agregar una columna con los quinquenios
    df_necesidades['Quinquenios'] = df_necesidades['IDE_EDA_ANO'].apply(clasificar_quinquenio)
    
    # Filtrar filas donde "DES_INS_UNIDAD" es igual a "IMSS_OPD"
    #df_nuevo = df_necesidades[df_necesidades["DES_INS_UNIDAD"] == "IMSS_OPD"]
    df_necesidades = df_necesidades[df_necesidades["DES_INS_UNIDAD"].str.strip().isin(["IMSS_OPD", "SSA"])]
    
    # Mostrar datos después del filtrado
    print("Datos después del filtrado:")
    print(df_necesidades.head(10))
    
    # Guardar el DataFrame combinado en un archivo Excel
    ruta_guardado = os.path.join("E://files_pandas//dengue//nuevo_archivo.xlsx")
    df_necesidades.to_excel(ruta_guardado, index=False)
    print(f"El archivo se ha guardado exitosamente en '{ruta_guardado}'")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
