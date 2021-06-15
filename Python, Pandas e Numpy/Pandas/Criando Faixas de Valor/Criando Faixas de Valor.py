#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados.head(10)


# In[3]:


# 1 e 2 quartos
# 3 e 4 quartos
# 5 e 6 quartos
# 7 ou mais quartos

classes = [0, 2, 4, 6, 100]


# In[6]:


# pd.cut() segmenta e classifica valores em bins discretas
quartos = pd.cut(dados['Quartos'], classes)
quartos       # cria uma Series categorizada


# In[10]:


# frequência, '(' abertos e ']' fechado
pd.value_counts(quartos)


# In[12]:


rotulos = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']


# In[13]:


# informando os rotulos
quartos = pd.cut(dados['Quartos'], classes, labels = rotulos)


# In[14]:


pd.value_counts(quartos)


# In[15]:


# incluindo o menor valor
quartos = pd.cut(dados['Quartos'], classes, labels = rotulos, include_lowest = True)


# In[16]:


# com a diferença no 1º intervalo, notamos que existem imóveis com 0 quartos
pd.value_counts(quartos)

