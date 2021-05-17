#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise III

# ## Imóveis Residenciais

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[3]:


dados.head(10)


# In[4]:


# lista sem valores duplicados
list(dados['Tipo'].drop_duplicates())


# In[5]:


# apenas os imóveis residenciais
residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']


# In[6]:


residencial


# In[8]:


# isin() retorna True ou False de acordo com o parâmetro
selecao = dados['Tipo'].isin(residencial)


# In[9]:


selecao


# In[10]:


dados_residencial = dados[selecao]


# In[11]:


dados_residencial


# In[12]:


# nota-se que temos apenas o tipo da lista residencial
list(dados_residencial['Tipo'].drop_duplicates())


# In[13]:


dados_residencial.shape


# In[14]:


dados.shape


# In[15]:


# reorganizando o índice
dados_residencial.index = range(dados_residencial.shape[0])


# In[16]:


dados_residencial


# ## Exportando o novo DataFrame criado

# In[17]:


dados_residencial.to_csv('dados/aluguel_residencial.csv', sep = ';')


# In[18]:


# desta maneira também exportamos os índice, como visto abaixo
dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')
dados_residencial_2


# In[19]:


# desta maneira não exportamos o índice
dados_residencial.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)


# In[20]:


# desta maneira também exportamos os índice, como visto abaixo
dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')
dados_residencial_2


# In[ ]:




