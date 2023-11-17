import pandas as pd 

#Lee el archivo CSV 
df_educ_sup=pd.read_csv("20230714_Titulados_Ed_Superior_2022_WEB.csv",sep=";",header=0)

#print(df_educ_sup)
df_educ_sup=df_educ_sup[df_educ_sup["nivel_carrera_2"]=="Carreras Profesionales"]   #del dataframe filtro la columna =a carreras profesionales 

#df_count_carreras=df_educ_sup.groupby('nomb_titulo_obtenido')#.reset_index(name='Conteo')

print(df_educ_sup)
df_educ_sup.to_excel("carreras.xlsx")
#df_count_carreras.to_excel("resumen_educacion_superior.xlsx",index=False,sheet_name='res_carr')
