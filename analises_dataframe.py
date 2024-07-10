# Importar bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/VALE3_RESUMO.csv')

##1) Qual o preço médio das ações da Companhia Vale no período?

# Calculando preço médio.

preco_medio_acoes = df['Fechamento'].mean()

print(f'Preço médio das ações da companhia Vale no periodo: R$ {preco_medio_acoes:.2f}.')
print(f'No período de: {len(df['Data'])} dias.')

##2) Preços máximo e mínimos

# Calculando preço máximo

preco_max = df['Fechamento'].max()
data_max = df.loc[df['Fechamento'].idxmax(),'Data']

# Calculando preço mínimo

preco_min = df['Fechamento'].min()
data_min = df.loc[df['Fechamento'].idxmin(),'Data']

print(f'Preço máximo de R${preco_max:.2f} na data {data_max} e mínimo de R${preco_min:.2f} na data {data_min} das ações da companhia Vale.')
print(f'No perído de {df['Data'][len(df['Data'])-1]} à {df['Data'][0]}.')

##3) Se um investidor tivesse adquirido uma certa quantidade de ações da Vale em um certo dia do período, qual seria o valor total dos papéis em outro dia do investimento? O investidor teria lucro ou prejuízo? De quantos reais?

# Criando uma função para o cálculo da diferença de preço e se houve lucro ou prejuízo.

qtd_adquirida = int(input("Insira a quantidade de ações adquiridas: "))
print(f'Período de: {len(df['Data'])} dias.')
dia_compra = int(input("\nInsira o número do dia válido da compra a partir do primeiro: "))
dia_venda = int(input("\nInsira o número do dia válido da venda a partir do primeiro: "))

def calculo_difenca_preco():
    if dia_venda > dia_compra:
        compra_acoes = qtd_adquirida * df['Fechamento'][len(df['Data'])-dia_compra]
        venda_acoes = qtd_adquirida * df['Fechamento'][len(df['Data'])-dia_venda]
        diferenca_preco = venda_acoes - compra_acoes
        if diferenca_preco > 0:
            return print(f'O cliente teve um lucro de R${diferenca_preco:.2f}.')
        else:
            return print(f'O cliente teve um prejuízo de R${(-1)*diferenca_preco:.2f}.')
    elif dia_venda or dia_compra > len(df['Data']):
        print("Dia inválido.")

    else: print("Dia inválido.")
    
calculo_difenca_preco()

