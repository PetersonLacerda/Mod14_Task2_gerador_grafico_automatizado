import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sns.set()

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
  if opcao == 'nada':
    pd.pivot_table(df, values= value, index= index, aggfunc= func).plot(figsize=[18, 6])
  elif opcao == 'unstack':
    pd.pivot_table(df, values= value, index= index, aggfunc= func).unstack().plot(figsize=[18, 6])
  elif opcao == 'sort':
    pd.pivot_table(df, values= value, index= index, aggfunc= func).sort_values(value).plot(figsize=[18, 6])
  plt.ylabel(ylabel)
  plt.xlabel(xlabel)    
  return None

mes = sys.argv[1]
print ("Mês de referência:",mes)

sinasc = pd.read_csv('./input/SINASC_RO_2019_'+mes+'.csv')

max_data = sinasc.DTNASC.max()[:7]
print(max_data)

os.makedirs('./output/figs/'+max_data, exist_ok=True)

plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')
plt.savefig('./output/figs/'+max_data+'/media idade mae por data.png')

plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'peso bebê', 'escolaridade mãe', 'sort')
plt.savefig('./output/figs/'+max_data+'/peso por escolaridade mae.png')

plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data+'/media idade da mae por sexo.png')

plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data+'/media peso do bebe por sexo.png')

plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano', 'escoladidade mae', 'sort')
plt.savefig('./output/figs/'+max_data+'/peso mediano por escolaridade da mae.png')

plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio', 'gestacao', 'sort')
plt.savefig('./output/figs/'+max_data+'/media apgar1 por gestacao.png')