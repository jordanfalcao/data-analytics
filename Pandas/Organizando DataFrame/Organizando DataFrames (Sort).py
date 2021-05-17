#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data


# In[3]:


# visualizando
list('321')


# In[9]:


# índice e colunas
df = pd.DataFrame(data, list('321'), list('ZYX'))
df


# In[10]:


# sort_index organiza o índice
df.sort_index(inplace = True)
df


# In[12]:


# axis = 1 para organizar as colunas
df.sort_index(inplace = True, axis = 1)
df


# In[13]:


# sort_values organiza pelo valor indicado, nesse caso valores de 'X'
df.sort_values(by = 'X', inplace = True)
df


# In[14]:


# sort_values organiza pelo valor indicado, nesse caso valores de '3'
df.sort_values(by = '3', inplace = True, axis = 1) # axis = 1, toma as colunas como referência
df


# In[ ]:




