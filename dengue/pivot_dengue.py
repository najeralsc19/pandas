import pandas as pd
# Cargar los datos desde el archivo Excel
dengue = pd.read_excel("E://files_pandas//dengue//Dengue_Hgo.xlsx")
dengue.rename(columns={'CVE_MPO_RES': 'CVE_MUN'}, inplace=True)
# Crear la tabla dinámica
pivot = dengue.pivot_table(values='CURP', index='CVE_MUN', aggfunc='count')
pivot = pivot.reset_index()



#------------------------ df de localidades INEGI -------------------------

loc = pd.read_csv("E://files_pandas//varios//AGEEML_202410311056515.csv")
loc = loc[loc['CVE_ENT'] == 13]


#print(loc.columns)


#----------------------MERGE----------------------------------------------

data = pd.merge(
    pivot,
    loc[['CVE_MUN','LAT_DECIMAL','LON_DECIMAL']],
    on=['CVE_MUN'],
    how='left',
    suffixes=('','_loc')
)   


data.to_excel("E://files_pandas//varios//nvo.xlsx")