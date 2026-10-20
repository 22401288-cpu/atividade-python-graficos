import plotly.express as tly
import pandas as pd

tb = pd.read_csv('graficos/dados_barras.csv')
bb = pd.read_csv('graficos/dados_boxplot.csv')

fig = tly.bar(tb, x="categoria", y="vendas_medias", color= "regiao", title = "Grafico barras", text_auto=True) 
fig.show()

fig = tly.bar(bb, x="departamento", y="salario", title = "Bloxplot", text_auto=True) 
fig.show()