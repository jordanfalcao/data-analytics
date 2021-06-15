#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


s = pd.Series(list('sadsaddsgkjasdsds'))
s


# In[7]:


# valores únicos 
s.unique()


# In[8]:


# conta quanto cada variável (aplicável p/ Series)
s.value_counts()


# In[9]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[14]:


# valores únicos da coluna 'Tipo' (aplicável p/ Series)
dados.Tipo.unique()


# In[17]:


# contador
dados.Tipo.value_counts()

