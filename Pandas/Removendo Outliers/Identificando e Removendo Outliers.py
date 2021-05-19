#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise VIII

# ## Identificando e Removendo Outliers

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[2]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')


# In[6]:


# boxplot da matplotlib, boxplot de uma coluna do DF
plt.boxplot(dados['Valor'])


# In[9]:


# outra maneira, muitos outliers, péssima visualização
dados.boxplot(['Valor'])


# In[10]:


# visualizando os dados provavelmente errados
dados[dados['Valor'] > 500000]


# In[11]:


# Series
valor = dados['Valor']


# In[13]:


# calculando quartis e intervalo interquartil
q1 = valor.quantile(.25)
q3 = valor.quantile(.75)
iiq = q3 - q1
limite_inf = q1 - 1.5 * iiq
limite_sup = q3 + 1.5 * iiq


# In[15]:


# limitando o 'Valor'
selecao = (valor >= limite_inf) & (valor <= limite_sup)
dados_new = dados[selecao]


# In[16]:


# boxplot com os limites aplicados
dados_new.boxplot('Valor')


# In[17]:


# comparando os histogramas (distribuição de frequências) antes e depois
dados.hist('Valor')
dados_new.hist('Valor')


# ## Identificando e Removendo Outliers (continuação)

# In[18]:


# by separa pela coluna atribuída
dados.boxplot(['Valor'], by = ['Tipo'])


# In[21]:


# agrupando pelo 'Tipo'
grupo_tipo = dados.groupby(['Tipo'])


# In[22]:


type(grupo_tipo)


# In[23]:


# agrupando pelo 'Tipo', mas selecionando apenas coluna 'Valor'
grupo_tipo = dados.groupby(['Tipo'])['Valor']
type(grupo_tipo)


# In[24]:


grupo_tipo.groups


# In[25]:


# calculando quartis e intervalo interquartil
q1 = grupo_tipo.quantile(.25)
q3 = grupo_tipo.quantile(.75)
iiq = q3 - q1
limite_inf = q1 - 1.5 * iiq
limite_sup = q3 + 1.5 * iiq


# In[26]:


q1


# In[27]:


q3


# In[28]:


iiq


# In[29]:


limite_inf


# In[30]:


limite_sup


# In[31]:


# acessar apenas um dado da Series
limite_sup.Apartamento


# In[33]:


# OU
q3['Quitinete']


# In[35]:


for tipo in grupo_tipo.groups.keys():
    print(tipo)


# In[36]:


dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inf[tipo]) & (dados['Valor'] <= limite_sup[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])


# In[37]:


dados_new.boxplot(['Valor'], by = ['Tipo'])


# In[38]:


dados_new


# In[39]:


dados_new.to_csv('dados/aluguel_residencial_sem_outliers.csv', sep = ';', index = False)


# In[ ]:




