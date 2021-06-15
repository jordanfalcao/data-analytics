#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VI

# ## Criando Novas Variáveis 

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[3]:


dados.head(10)


# In[4]:


# criando uma nova coluna com o gasto mensal
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']


# In[5]:


dados.head(10)


# In[12]:


# valor do aluguel por m²
dados['Valor_m2'] = dados['Valor'] / dados['Area']


# In[13]:


dados.head(10)


# In[14]:


# duas casas decimais
dados['Valor_m2'] = dados['Valor_m2'].round(2)


# In[15]:


dados.head(10)


# In[16]:


# valor total por m²
dados['Valor_Bruto_m2'] = (dados['Valor Bruto'] / dados['Area']).round(2) 


# In[17]:


dados.head(10)


# In[22]:


casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']


# In[23]:


# apply() aplica uma função para cada item do DF
# cria nova coluna com 'Casa' ou 'Apartamento'
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')


# In[26]:


dados.head(20)


# ## Excluindo Variáveis

# In[28]:


dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor_m2', 'Valor Bruto', 'Valor_Bruto_m2']])


# In[29]:


dados_aux


# In[30]:


# del
del dados_aux['Valor Bruto']
dados_aux


# In[31]:


# usando pop, apga e retorna a variável
dados_aux.pop('Valor_Bruto_m2')


# In[32]:


dados_aux.head(10)


# In[35]:


# .drop podemos passar mais de um dado
dados.drop(['Valor Bruto', 'Valor_Bruto_m2'], axis = 1, inplace = True) # axis = 1 exclui coluna


# In[36]:


dados.head(10)


# In[37]:


# sobrescrevendo arquivo csv
dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)

