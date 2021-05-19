#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VII

# ## Criando Agrupamentos

# In[66]:


import pandas as pd


# In[67]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[68]:


dados.head(10)


# In[69]:


# média da coluna
dados['Valor'].mean()


# In[70]:


# apenas alguns bairros
bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados2 = dados[selecao]


# In[71]:


dados2


# In[72]:


dados2['Bairro'].drop_duplicates()


# In[94]:


grupo_bairro = dados2.groupby('Bairro')


# In[74]:


type(grupo_bairro)


# In[75]:


# propriedade .groups, é um dict key são os bairros, value são os índices correspondentes 
grupo_bairro.groups


# In[76]:


# print das keys
for bairro, dados in grupo_bairro:
    print(bairro)


# In[77]:


# print dos values
for bairro, data in grupo_bairro:
    print(data)


# In[78]:


# um DataFrame para cada bairro
for bairro, data in grupo_bairro:
    print(type(data))


# In[79]:


# média de condominio por bairro
for bairro, data in grupo_bairro:
    print('{} - {}'.format(bairro, data.Valor.mean()))


# In[80]:


# podemos extrair a média de maneira mais simples:
grupo_bairro['Valor'].mean()


# In[81]:


# mais de uma variável por bairro
grupo_bairro[['Valor', 'Condominio']].mean().round(2)


# ## Estatísticas Descritivas

# In[82]:


# .describe() apresenta um conjunto de estatísticas descritivas
grupo_bairro['Valor'].describe().round(2)


# In[83]:


# .agg ou .aggregate, conjunto de estatísticas de interesse
# podemos renomear os nomes das colunas  com .rename()
grupo_bairro['Valor'].agg(['min', 'max', 'sum', 'count', 'median', 'nunique']).rename(columns = {'min': 'Mínimo', 'sum': 'Soma'})


# In[90]:


# nova biblioteca e algumas configurações

#mostra figura ficar estática na tela, necessário no Jupyter
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
plt.rc('figure', figsize = (16, 8))  # tamanho da figura


# In[109]:


# notamos um problema no desvio padrão de Botafogo
fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')
fig.set_ylabel('Desvio Padrão')
fig.set_title('Desvio Padrão por Bairro', {'fontsize': 20})


# In[108]:


# média
fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 20})


# In[110]:


# mediana
fig = grupo_bairro['Valor'].median().plot.bar(color = 'blue')
fig.set_ylabel('Mediana')
fig.set_title('Mediana por Bairro', {'fontsize': 20})


# In[111]:


# máximo
fig = grupo_bairro['Valor'].max().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Máximo do Aluguel por Bairro', {'fontsize': 20})


# In[ ]:




