#from dengue.config_pandas import *
import pandas as pd
import openpyxl
import unicodedata
#cargar el archivo al data frame directamente
df = pd.read_excel("E://files_pandas//dengue//DENGUE141024.xlsx")
#Funcion limpiar valores
def limpiar_valores(value):
    if isinstance(value, str):
        value = unicodedata.normalize('NFKD', value).encode('ascii', errors='ignore').decode('utf-8')
        value = value.strip()
    elif pd.isnull(value): 
        # Sustituir null por un espacio en blanco 
        value = ''
    return value
#aplicas la funcion al data frame
df = df.map(limpiar_valores)

#crear nuevo data frame con las columnas especificas 
df_filtrado = df[["FOL_ID", "IDE_ID", "CVE_INF", "VEC_ID", "IDE_NOM", "IDE_APE_PAT", "IDE_APE_MAT", "RFC", "CURP", "IDE_FEC_NAC", "CVE_EDO_NAC","DES_EDO_NAC", "CVE_MPO_NAC", "DES_MPO_NAC", "IDE_SEX", "IDE_EDA_ANO", "IDE_EDA_MES", "IDE_EDA_DIA", "DES_CAL", "IDE_CAL", "NUM_INT", "NUM_EXT", "IDE_COL", "CVE_EDO_RES", "DES_EDO_RES", "CVE_JUR_RES", "DES_JUR_RES", "CVE_MPO_RES", "DES_MPO_RES", "CVE_LOC_RES", "DES_LOC_RES", "IDE_TEL", "IDE_CALLE1", "IDE_CP", "ES_INDIGENA", "LENGUA_INDIGENA", "CUAL_LENGUA", "DES_CUAL_LENGUA", "CVE_OCUPACION", "DES_OCUPACION", "ESTATUS_CASO", "EXPEDIENTE", "CVE_EDO_TRABAJO", "CVE_UNI_MED_NOTIF", "DES_UNI_MED_NOTIF", "CVE_EDO_UNIDAD", "DES_EDO_UNIDAD", "DES_JUR_UNIDAD", "DES_MPO_UNIDAD", "DES_INS_UNIDAD", "FEC_NOTIF_DGE", "DES_DIAG_FINAL", "FEC_INI_SIGNOS_SINT", "SEM", "EMBARAZO", "SEM_GEST"]]
#filtrar el data frame nuevo validando el valor de la celda DES_INS_UNIDAD
df_filtrado = df_filtrado[(df_filtrado["DES_INS_UNIDAD"]=="IMSS_OPD")]

print(df_filtrado.head())




