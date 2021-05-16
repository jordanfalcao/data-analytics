#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise II

# ## Tipo de Imóveis 

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[4]:


# cabeçalho
dados.head(10)


# In[6]:


# visualizando coluna 'Tipo' em forma de DataFrame
dados[['Tipo']]


# In[7]:


# possível quando a coluna tem apenas UM nome
dados.Tipo


# In[8]:


# armazenando numa variável
tipo_imovel = dados['Tipo']


# In[9]:


# tipos únicos 
tipo_imovel.unique()


# In[12]:


# pega o primeiro de cada tipo e remove os restantes
tipo_imovel.drop_duplicates() #remove mas não salva as alterações na variável


# In[13]:


# inplace True atribui a modificação à variável
tipo_imovel.drop_duplicates(inplace = True)
tipo_imovel


# ## Organizando a Visualização

# In[14]:


tipo_de_imovel = pd.DataFrame(tipo_imovel)


# In[15]:


tipo_de_imovel


# In[16]:


tipo_de_imovel.index


# In[18]:


range(len(tipo_de_imovel))


# In[20]:


# organizando o index
tipo_de_imovel.index = range(len(tipo_de_imovel))
tipo_de_imovel


# In[21]:


tipo_de_imovel.index


# In[22]:


# aterando o nome da coluna dos índices
tipo_de_imovel.columns.name = 'Id'
tipo_de_imovel


# In[ ]:




