#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# criando uma Series
data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
s


# In[3]:


# completa os null com 0
s.fillna(0)


# In[4]:


# completa o valor null com o anterior
s.fillna(method = 'ffill')


# In[5]:


# começa de baixo pra cima
s.fillna(method = 'bfill')


# In[6]:


# preenche com a média dos valores não nulos
s.fillna(s.mean())


# In[7]:


# preenche apenas 1 valor com o anterior
s.fillna(method = 'ffill', limit = 1) # limit = 1


# In[8]:


# podemos preencher um null com o de cima 
s1 = s.fillna(method = 'ffill', limit = 1)  # 'ffill'
s1


# In[9]:


# em sequencia preencha com o de baixo
s1.fillna(method = 'bfill', limit = 1)  # 'bfill'

