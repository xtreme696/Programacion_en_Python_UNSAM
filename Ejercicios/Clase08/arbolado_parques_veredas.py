# arbolado_parques_veredas.py
import pandas as pd
# import seaborn as sns


# Datasets originales
df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')
df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

# Datasets nuevos
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][['diametro', 'altura_tot']].copy()
df_tipas_parques = df_tipas_parques.rename(columns={'altura_tot': 'altura'})
df_tipas_parques['ambiente'] = 'parque'

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][['diametro_altura_pecho', 'altura_arbol']].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura'})
df_tipas_veredas['ambiente'] = 'vereda'

# Datasets concatenados
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques], ignore_index=True)


# TENGO ERRORES DEL IDE PARA EL TRABAJO CON SEABORN
# ModuleNotFoundError: No module named 'seaborn'
# Intenté instalar el módulo pero funciona desde la terminal y no desde el spyder, incluso después de reiniciar