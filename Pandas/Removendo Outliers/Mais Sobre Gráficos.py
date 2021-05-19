#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15,8))


# In[15]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados.head(8)


# In[16]:


# criando a área que englobará o gráfico
area = plt.figure()


# In[17]:


# adicionando subplots(linhas, colunas, posição)
g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)


# In[18]:


# tipos diferentes de gráficos
g1.scatter(dados.Valor, dados.Area) # gráfico de dispersão
g1.set_title('Valor x Area')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0]) # organizando os índices
g3.plot(dados_g3)
g3.set_title('Amostras Aleatórias (Valor)')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')


# In[19]:


area


# In[21]:


# salvando a figura
area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight') #bbox = tight tira o excesso das bordas

