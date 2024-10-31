import pandas as pd 
import unicodedata


base = pd.read_csv("E://files_pandas//sisver//AGEEML_202410311056515.csv")

def acentos(value):
    if isinstance(value, str):
        value = unicodedata.normalize('NFKD', value).encode('ascii', errors='ignore').decode('utf-8')
        value = value.strip().upper()
    elif pd.isnull(value):
        value=''
    return value 