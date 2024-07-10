# Importar bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/VALE3_RESUMO.csv')

##4) Criando um gráfico de linha que plote os dados do papéis da Vale ao longo do período.

# Converter a coluna Data para o formato datetime
df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y")

# Criar gráfico
plt.figure(figsize=(12,6))
plt.plot(df['Data'],df['Fechamento'])
plt.title('Preço de fechamento da VALE3 ao longo do período')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend()
plt.grid(True)
plt.show()