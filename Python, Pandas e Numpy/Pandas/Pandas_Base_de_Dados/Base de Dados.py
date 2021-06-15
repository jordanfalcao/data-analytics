#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise I

# ## Importando a Base de Dados

# In[12]:


import pandas as pd


# In[13]:


# lendo arquivo csv com a pandas
pd.read_csv("dados/aluguel.csv", sep = ';')


# In[14]:


# armazenando numa variável
dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[15]:


# cabeçalho
dados.head()


# In[16]:


# tipo da variável dados DataFrame
type(dados)


# In[17]:


# informações
dados.info()


# In[18]:


# cabeçalho com as 10 primeiras linhas
dados.head(10)


# ## Informações Gerais sobre a Base de Dados

# In[22]:


# tipos de dados das variáveis
dados.dtypes


# In[26]:


# colocar no formato DataFrame, columns especifica nome das colunas
tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])


# In[27]:


# inserindo nome
tipos_de_dados.columns.name = 'Variáveis'


# In[28]:


tipos_de_dados


# In[29]:


# linhas e columas (tupla)
dados.shape


# In[30]:


dados.shape[0]


# In[31]:


dados.shape[1]


# In[33]:


# print com o .format
print('A base de dados apresenta {} registros (imóveis) e {} variáveis.'.format(dados.shape[0], dados.shape[1]))


# In[ ]:




