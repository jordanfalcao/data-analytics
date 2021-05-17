#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd


# # Series

# In[52]:


data = [1, 2, 3, 4, 5]


# In[53]:


# criando uma Series com a pandas
s = pd.Series(data)


# In[54]:


s


# In[55]:


# criando index
indice = ['Linha' + str(i) for i in range(5)]


# In[56]:


indice


# In[57]:


# atribuindo à variável
s = pd.Series(data, index = indice)


# In[58]:


s


# In[59]:


# criando Series a partir de um dict
dados = {'Linha' + str(i) : i + 1 for i in range(5)}


# In[60]:


dados


# In[61]:


# a partir do dict
s1 = pd.Series(dados)
s1


# In[62]:


s2 = s1 + 2


# In[63]:


s2


# In[64]:


# podemos fazer operação com as Series de mesmo índice
s3 = s2 + s1
s3


# # DataFrame

# In[65]:


d1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]


# In[66]:


d1


# In[67]:


# criando DataFrame a partir da lista
df = pd.DataFrame(d1)
df


# In[68]:


# criando index paras linhas
ind = ['Linha' + str(i) for i in range(3)]
ind


# In[69]:


df = pd.DataFrame(d1, index = ind)


# In[70]:


df


# In[71]:


# criando index paras colunas
ind1 = ['Coluna' + str(i) for i in range(3)]
ind1


# In[72]:


df = pd.DataFrame(d1, index = ind, columns = ind1)
df


# In[73]:


# criando DataFrame a partir de dict
data1 = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}


# In[74]:


data1


# In[75]:


df1 = pd.DataFrame(data1)
df1


# In[76]:


# criando DF a partir de tuplas
d2 = [(1, 2, 3),
      (4, 5, 6),
      (7, 8, 9)]
d2


# In[77]:


df2 = pd.DataFrame(d2, index = ind, columns = ind1)
df2


# In[78]:


df[df > 0] = 'A'
df


# In[79]:


df1[df1 > 0] = 'B'
df1


# In[80]:


df2[df2 > 0] = 'C'
df2


# In[81]:


# concatenando a partir das COLUNAS
df4 = pd.concat([df, df1, df2])
df4


# In[82]:


# concatenando a partir das LINHAS
df5 = pd.concat([df, df1, df2], axis = 1)
df5


# In[ ]:




