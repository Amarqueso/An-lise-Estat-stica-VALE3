# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Importar o arquivo csv
historico_vale_df = pd.read_csv("csv/historicovale.csv")

# Criar um novo dataframe somente com as colunas necessarias
vale_resumo = historico_vale_df[['DATA','FECHAMENTO']].copy()
vale_resumo.columns = ['Data','Fechamento']

# Substituir as vígulas por pontos na coluna Fechamento
vale_resumo['Fechamento'] = vale_resumo['Fechamento'].str.replace(',','.').astype(float)

# Exportar o dataframe para um novo arquivo csv
vale_resumo.to_csv('csv/VALE3_RESUMO.csv',index = False)