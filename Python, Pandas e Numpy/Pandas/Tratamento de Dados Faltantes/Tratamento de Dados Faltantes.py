#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise V

# ## Tratamento de Dados Faltantes

# In[2]:


import pandas as pd


# In[3]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[5]:


dados.head(10)


# In[6]:


# retorna boolean 
dados.isnull()


# In[8]:


# oposto do isnull(), também retorna boolean
dados.notnull()


# In[9]:


dados.info()


# In[11]:


# apenas os 9 registros com 'Valor' null
dados[dados['Valor'].isnull()]


# In[13]:


# dropna() elimina os valores nulos
A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace = True)
B = dados.shape[0]
A - B


# In[15]:


# vazio, pois eliminamos os nulos
dados[dados['Valor'].isnull()]


# ## Tratamento de Dados Faltantes (continuação)

# In[16]:


dados[dados['Condominio'].isnull()].shape[0]


# In[17]:


# todos Apartamento que tem Condominio null
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())


# In[18]:


# elimina os valores nulos
A = dados.shape[0]
dados = dados[~selecao]  # o oposto da seleção feita
B = dados.shape[0]
A - B


# In[19]:


dados[dados['Condominio'].isnull()].shape[0]


# In[26]:


# preenche os valores null através de um dict
dados = dados.fillna({'Condominio': 0, 'IPTU': 0})


# In[27]:


dados[dados['Condominio'].isnull()].shape[0]


# In[28]:


dados[dados['IPTU'].isnull()].shape[0]


# In[29]:


dados.info()


# In[30]:


# atualizando o arquivo
dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)


# In[ ]:




