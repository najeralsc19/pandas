import pandas as pd
# Cargar los datos desde el archivo Excel
dengue = pd.read_excel("E://files_pandas//dengue//Dengue_Hgo.xlsx")

dengue.rename(columns={'CVE_LOC_RES': 'CVE_LOC', 'CVE_MPO_RES' : 'CVE_MUN'}, inplace=True)
print(dengue.columns)
 #Crear la tabla dinámica
pivot = dengue.pivot_table(values='CURP', index=['CVE_MUN', 'CVE_LOC'], aggfunc='count')
pivot = pivot.reset_index()
pivot = pivot.set_index('CVE_LOC')

pivot.to_excel("E://files_pandas//varios//pivote.xlsx")

#print(pivot.head())



#------------------------ df de localidades INEGI -------------------------

loc = pd.read_csv("E://files_pandas//varios//AGEEML_202410311056515.csv")
loc = loc[loc['CVE_ENT'] == 13]


merge = pd.merge(
    pivot,
    loc[['CVE_LOC', 'CVE_MUN','LAT_DECIMAL','LON_DECIMAL']],
    on=[['CVE_LOC', 'CVE_MUN']],
    how='left',
    suffixes=('','_loc')
)

print(merge.head())