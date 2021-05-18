#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


# cria uma lista
'l1 l2 l3 l4'.split()


# In[2]:


data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())


# In[4]:


df


# In[5]:


# apenas uma coluna
df['c1']


# In[6]:


type(df['c1'])


# In[7]:


# mais de uma coluna, na ordem desejada
df[['c3','c1']]


# In[8]:


type(df[['c3','c1']])


# In[9]:


df[:]


# In[11]:


# intervalo fechado, intervalo aberto
df[1:3]


# In[14]:


# seleção de colunas e linhas
df[1:][['c3','c1']]


# In[16]:


df


# In[15]:


# .loc
df.loc['l3']


# In[19]:


df.loc[['l3', 'l2']]


# In[20]:


# valor específico
df.loc['l1', 'c2']


# In[22]:


# seleciona pelo índice numérico
df.iloc[0, 1]


# In[23]:


# linhas e colunas específicas
df.loc[['l3', 'l1'], ['c4', 'c1']]


# In[25]:


# linhas e colunas específicas com iloc
df.iloc[[2, 0], [3, 0]]


# In[ ]:




