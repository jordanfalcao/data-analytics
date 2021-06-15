#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise IV

# ## Seleções e Frequências

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[4]:


dados.head(10)


# In[14]:


# Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = dados['Tipo'] == 'Apartamento'
n = dados[selecao].shape[0]  # quantidade de vezes
n   


# In[15]:


# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao1 = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n1 = dados[selecao1].shape[0]
n1


# In[17]:


# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
selecao2 = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n2 = dados[selecao2].shape[0]
n2


# In[20]:


# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao3 = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n3 = dados[selecao3].shape[0]
n3


# In[ ]:




