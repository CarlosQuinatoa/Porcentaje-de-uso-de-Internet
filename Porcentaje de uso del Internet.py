#Porcentaje de Uso del Internet
"""
Integrantes:
    Carlos Quinatoa
    Christian Gutierrez
    Laura Castañeda
    Andrea Pruna
    Kevin Oña
"""
#Importar librería
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

#Crear dataframes de interés, 
"""Crear df_countries que contiene las etiquetas por países
    df_index contiene los valores dle indidce elegido
"""
df_index= pd.read_excel('API_IT.NET.USER.ZS_DS2_es_excel_v2_6300530.xls',sheet_name= "Data",skiprows= 3)
print(df_index)
df_countries= pd.read_excel('API_IT.NET.USER.ZS_DS2_es_excel_v2_6300530.xls',sheet_name= "Metadata - Countries")
df_index.columns
df_countries.columns
#Filtrar datos para América Latina
america_latina = df_countries[df_countries["Region"] == "América Latina y el Caribe (excluido altos ingresos)"]
print(america_latina)
#Número de paises en América Latina
len(america_latina)

la_index=america_latina.merge(df_index,on= ["Country Name" , "Country Code"],how = "left")
print(la_index)

#Cálculo de le media
la_index['2020'].mean()

""" ANÁLISIS
Según los datos proporcionados por el Banco Mundial, el promedio
de la población que utiliza Internet en los 23 países de América Latina 
es del 67.74%. Considerando que cada país tiene su propia composición demográfica, 
económica, social y cultural, lo que significa que la incidencia del Internet puede variar 
significativamente de un país a otro (Peñaloza, 2015).

"""


#Gráfico de la evolcuión del indice a lo largo del tiempo
"""Crear variable de años para calular el promedio de cada año.
"""
anio=la_index.drop(columns=['Country Name', 'Country Code', 'Region', 'Income_Group',
       'Indicator Name', 'Indicator Code', '1960', '1961', '1962', '1963',
       '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972',
       '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981',
       '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989'])
print(anio)
prom_la=anio.mean()
print(prom_la)

#Gráfico de evolución
plt.plot(prom_la.index, prom_la.values, marker='o', linestyle='-')

# Añadir etiquetas y título
plt.xlabel('Año')
plt.ylabel('Promedio')
plt.title('Promedio por año')
plt.xticks(rotation=90)
# Mostrar la gráfica
plt.show()

""" ANÁLISIS
A finales de la década de los 90 la incidencia del uso del internet en América latina 
no tuvo un impacto significativo en la población, mientras que en promedio a partir 
del año 2000 la evolución del uso del internet ha tenido un crecimiento exponencial 
que ha sido impulsado por:
    -Expansión de la infraestructura de telecomunicaciones
    -Disminución del costo de los dispositivos
    -Mayor acceso a la educación
    -Políticas públicas de promoción de las TIC

"""


#Mapa de correlación 
la_index.columns
df_filtrado = la_index[['2018', '2019', '2020', '2021', '2022']]
print(df_filtrado)

matriz_correlacion = df_filtrado.corr()
# Usa seaborn para crear un mapa de calor
sns.heatmap(matriz_correlacion, annot=True, cmap="YlGnBu")
plt.title('Mapa de Correlación')
plt.show()


""" ANÁLISIS
La alta correlación entre el uso de Internet en los últimos cinco años sugiere 
una tendencia estable de crecimiento en el acceso y uso de Internet a lo largo del tiempo.
Esto es reflejado en la gráfica de evolución, mostrando una relación estrecha y 
predecible entre el porcentaje de personas que usan Internet de un año a otro.

Entre el año 2020 y 2021 tienen un coeficiente de correlación de 0.99 lo que sugiere una 
fuerte relación positiva y casi perfecta entre estos dos años en cuanto al uso de Internet, 
argumentando que se da por eventos o circunstancias que afectan ambos años como 
la pandemia de COVID-19 (Becerra, 2021).

"""

"""
REFERENCIAS

Peñaloza, H. A. B. (2015). Determinantes del acceso al Internet: 
evidencia de los hogares del Ecuador. Entramado, 11(2), 12-19. 
https://doi.org/10.18041/entramado.2015v11n2.22205

Becerra, B. X. (2021, 10 diciembre). Consumo de internet en el mundo aumentó 19,5% 
durante la pandemia de Covid-19. Diario La República. 
https://www.larepublica.co/consumo/consumo-de-internet-en-el-mundo-aumento-19-5-durante-la-pandemia-de-covid-19-3274945


"""