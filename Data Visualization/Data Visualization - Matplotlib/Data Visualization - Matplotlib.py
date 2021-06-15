#!/usr/bin/env python
# coding: utf-8

# <h1>Aula 01</h1>

# In[16]:


import pandas as pd


# In[17]:


df = pd.read_csv('monitoramento_tempo.csv')


# In[18]:


df.head()


# In[19]:


df.info()


# In[20]:


# convertendo coluna 'data' para o tipo 'datetime'
df['data'] = pd.to_datetime(df['data'])


# In[21]:


df.info()


# In[22]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


# data x tempetatura
plt.plot(df['data'], df['temperatura'])


# In[24]:


# aumentando tamanho
plt.figure(figsize = (15, 8))
plt.plot(df['data'], df['temperatura'])


# In[25]:


# inserindo título
plt.figure(figsize = (15, 8))
plt.plot(df['data'], df['temperatura'])
plt.title('Temperatura no tempo', fontsize = 20)


# In[26]:


# figura vazia
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'


# In[28]:


# variáveis possibilitam configurações mais avançadas posteriormente
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'])
eixo.set_title('Temperatura no momento', fontsize = 20)


# In[30]:


# nomes aos eixos
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'])

eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)


# In[32]:


# legenda
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'])

eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# In[35]:


# alterar cor
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'darkviolet')   # aqui

eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# <h2>Link para tipos de cores:</h2>
# 
# https://matplotlib.org/stable/gallery/color/named_colors.html

# <h1>Aula 02</h1>
# 
# <h2>Customizando nossas visualizações</h2>

# In[36]:


# espessura da linha
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'g', lw = 4)   # aqui

eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# In[37]:


# espessura da linha
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'g', lw = 0.4)   # aqui

eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# In[38]:


# tipo da linha
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'g', ls = 'dotted') # aqui line style   

eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# In[40]:


import datetime


# In[41]:


# seccionar o gráfico
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'g') 

eixo.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# In[42]:


# marcadores
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'g', marker = 'o')   # aqui

eixo.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)


# In[43]:


# grid
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) # eixo vai de '0,0' a '1,1'
eixo.plot(df['data'], df['temperatura'], color = 'g') 

eixo.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo.set_title('Temperatura no momento', fontsize = 25)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)
eixo.grid(True)


# In[44]:


# outros eixos
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) 
eixo2 = fig.add_axes([0.1, 0.5, 0.4, 0.4]) 


# In[52]:


fig = plt.figure(figsize = (15, 8))

eixo = fig.add_axes([0, 0, 1, 1]) 
eixo2 = fig.add_axes([0.1, 0.5, 0.4, 0.4]) 

eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.grid(True)
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'best', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)

eixo2.plot(df['data'], df['temperatura'], color = 'b')
eixo2.set_title('Temperatura no momento', fontsize = 15)
eixo2.legend(['Temperatura'], loc = 'best', fontsize = 8)
eixo2.set_ylabel('Temperatura', fontsize = 10)
eixo2.set_xlabel('Data', fontsize = 10)


# In[54]:


# limitando gráfico maior e alterando posição do gráfico menor
fig = plt.figure(figsize = (15, 8))

eixo = fig.add_axes([0, 0, 1, 1]) 
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'upper left', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)

eixo2.plot(df['data'], df['temperatura'], color = 'b')
eixo2.set_title('Temperatura no momento', fontsize = 15)
eixo2.legend(['Temperatura'], loc = 'best', fontsize = 8)
eixo2.set_ylabel('Temperatura', fontsize = 10)
eixo2.set_xlabel('Data', fontsize = 10)
eixo2.grid(True)


# In[58]:


# limitando eixo y
fig = plt.figure(figsize = (15, 8))

eixo = fig.add_axes([0, 0, 1, 1]) 
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_xlim(datetime.datetime(2014, 5, 1), datetime.datetime(2014, 6, 1))
eixo.set_ylim(270, 320)
eixo.set_title('Temperatura no mês de maio de 2014', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'upper left', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)

eixo2.plot(df['data'], df['temperatura'], color = 'b')
eixo2.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo2.set_title('Temperatura no ano de 2014', fontsize = 15)
eixo2.legend(['Temperatura'], loc = 'best', fontsize = 8)
eixo2.set_ylabel('Temperatura', fontsize = 10)
eixo2.set_xlabel('Data', fontsize = 10)
eixo2.grid(True)


# In[60]:


# filtro / restrição
fig = plt.figure(figsize = (15, 8))

eixo = fig.add_axes([0, 0, 1, 1]) 
eixo2 = fig.add_axes([0.7, 0.65, 0.3, 0.3]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_xlim(datetime.datetime(2014, 5, 1), datetime.datetime(2014, 6, 1))
eixo.set_ylim(270, 320)
eixo.set_title('Temperatura no mês de maio de 2014', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'upper left', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 18)
eixo.set_xlabel('Data', fontsize = 18)

azul_esquerda = df['data'] < datetime.datetime(2014, 5, 1)
azul_direita = df['data'] >= datetime.datetime(2014, 6, 1)


eixo2.plot(df['data'], df['temperatura'], color = 'g')

eixo2.plot(df[azul_esquerda]['data'], df[azul_esquerda]['temperatura'], color = 'b')
eixo2.plot(df[azul_direita]['data'], df[azul_direita]['temperatura'], color = 'b')

eixo2.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo2.set_title('Temperatura no ano de 2014', fontsize = 15)
eixo2.legend(['Temperatura'], loc = 'best', fontsize = 8)
eixo2.set_ylabel('Temperatura', fontsize = 10)
eixo2.set_xlabel('Data', fontsize = 10)
eixo2.grid(True)


# <h2>Aula 03:</h2>

# In[61]:


# temperatura máxima e mínima
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 20)
eixo.set_xlabel('Data', fontsize = 20)

eixo.axhline(max(df['temperatura']), color = 'k', linestyle = '--')
eixo.axhline(min(df['temperatura']), color = 'k', linestyle = '--')


# In[62]:


# marcação no gráfico
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 20)
eixo.set_xlabel('Data', fontsize = 20)

x1 = df['data'][df['temperatura'].idxmax()]  # 'data' onde a temperatura é máxima
y1 = max(df['temperatura'])

eixo.annotate('Máximo', xy = (x1, y1), fontsize = 20)

eixo.axhline(max(df['temperatura']), color = 'k', linestyle = '--')
eixo.axhline(min(df['temperatura']), color = 'k', linestyle = '--')


# In[64]:


# marcação de seta no gráfico
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 20)
eixo.set_xlabel('Data', fontsize = 20)

x1 = df['data'][df['temperatura'].idxmax()]  # 'data' onde a temperatura é máxima
y1 = max(df['temperatura'])

x2 = df['data'][df['temperatura'].idxmax() - 7000]  # 7000 horas
y2 = max(df['temperatura']) - 5

eixo.annotate('Máximo', xy = (x1, y1), fontsize = 20, xytext = (x2, y2), arrowprops = dict(facecolor = 'k'))

eixo.axhline(max(df['temperatura']), color = 'k', linestyle = '--')
eixo.axhline(min(df['temperatura']), color = 'k', linestyle = '--')


# In[65]:


# mesmo procedimento para o mínimo
fig = plt.figure(figsize = (15, 8))
eixo = fig.add_axes([0, 0, 1, 1]) 

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'g') 
eixo.set_title('Temperatura no momento', fontsize = 25, pad = 20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize = 15)
eixo.set_ylabel('Temperatura', fontsize = 20)
eixo.set_xlabel('Data', fontsize = 20)

x1 = df['data'][df['temperatura'].idxmax()]  # 'data' onde a temperatura é máxima
y1 = max(df['temperatura'])

x2 = df['data'][df['temperatura'].idxmax() - 7000]  # 7000 horas
y2 = max(df['temperatura']) - 5

eixo.annotate('Máximo', xy = (x1, y1), fontsize = 20, xytext = (x2, y2), arrowprops = dict(facecolor = 'k'))

x1 = df['data'][df['temperatura'].idxmin()]  # 'data' onde a temperatura é mínima
y1 = min(df['temperatura'])

x2 = df['data'][df['temperatura'].idxmin() - 7000]  # 7000 horas
y2 = min(df['temperatura']) + 5

eixo.annotate('Mínimo', xy = (x1, y1), fontsize = 20, xytext = (x2, y2), arrowprops = dict(facecolor = 'k'))

eixo.axhline(max(df['temperatura']), color = 'k', linestyle = '--')
eixo.axhline(min(df['temperatura']), color = 'k', linestyle = '--')


# In[67]:


# média da temperatura agrupadas por dia da semana
temperatura_por_dia_da_semana = df.groupby('dia_da_semana')['temperatura'].mean()
nome_dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
temperatura_por_dia_da_semana = temperatura_por_dia_da_semana[nome_dias]
temperatura_por_dia_da_semana


# In[69]:


# gráfico de barras
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
indice = range(len(temperatura_por_dia_da_semana))

eixo.bar(indice, temperatura_por_dia_da_semana)
eixo.set_title('Temperatura por dia da semana', fontsize = 20, pad=10)
eixo.set_xlabel('Dia da semana', fontsize = 15)
eixo.set_ylabel('Temperatura média', fontsize = 15)


# In[74]:


# alterando os índices
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
indice = range(len(temperatura_por_dia_da_semana))

eixo.bar(indice, temperatura_por_dia_da_semana)
eixo.set_title('Temperatura por dia da semana', fontsize = 20, pad=10)
eixo.set_xlabel('Dia da semana', fontsize = 15)
eixo.set_ylabel('Temperatura média', fontsize = 15)
eixo.set_xticks(indice)
eixo.set_xticklabels(nome_dias)
eixo


# In[76]:


# alterando cores das barras
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
indice = range(len(temperatura_por_dia_da_semana))

indice = range(len(temperatura_por_dia_da_semana))
cores = ['black', 'r', 'g', 'b', 'yellow', 'orange', 'magenta']

eixo.bar(indice, temperatura_por_dia_da_semana, color=cores)
eixo.set_title('Temperatura por dia da semana', fontsize = 20, pad=10)
eixo.set_xlabel('Dia da semana', fontsize = 15)
eixo.set_ylabel('Temperatura média', fontsize = 15)
eixo.set_xticks(indice)
eixo.set_xticklabels(nome_dias)
eixo


# In[77]:


# inserindo borda nas barras
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
indice = range(len(temperatura_por_dia_da_semana))

indice = range(len(temperatura_por_dia_da_semana))
cores = ['black', 'r', 'g', 'b', 'yellow', 'orange', 'magenta']

eixo.bar(indice, temperatura_por_dia_da_semana, color=cores, edgecolor = 'k')
eixo.set_title('Temperatura por dia da semana', fontsize = 20, pad=10)
eixo.set_xlabel('Dia da semana', fontsize = 15)
eixo.set_ylabel('Temperatura média', fontsize = 15)
eixo.set_xticks(indice)
eixo.set_xticklabels(nome_dias)
eixo


# In[79]:


# gráfico de pizza/torta
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.pie(temperatura_por_dia_da_semana, labels = temperatura_por_dia_da_semana.index)
eixo.set_title('Temperatura por dia da semana', fontsize = 15, pad = 10)
eixo


# In[80]:


# adicionando porcentagem
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.pie(temperatura_por_dia_da_semana, labels = temperatura_por_dia_da_semana.index, autopct = '%.2f%%')  # aqui
eixo.set_title('Temperatura por dia da semana', fontsize = 15, pad = 10)
eixo


# In[81]:


# destacar/explodir fim de semana
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

explodir = [1, 0, 0, 0, 0, 1, 1]

eixo.pie(temperatura_por_dia_da_semana, labels = temperatura_por_dia_da_semana.index, 
         autopct = '%.2f%%', explode = explodir)  # aqui
eixo.set_title('Temperatura por dia da semana', fontsize = 15, pad = 10)
eixo


# In[82]:


# ajustando destacar/explodir fim de semana
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

explodir = [0.1, 0, 0, 0, 0, 0.1, 0.1]

eixo.pie(temperatura_por_dia_da_semana, labels = temperatura_por_dia_da_semana.index, 
         autopct = '%.2f%%', explode = explodir)  # aqui
eixo.set_title('Temperatura por dia da semana', fontsize = 15, pad = 10)
eixo


# In[83]:


# adicionando sombra
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

explodir = [0.1, 0, 0, 0, 0, 0.1, 0.1]

eixo.pie(temperatura_por_dia_da_semana, labels = temperatura_por_dia_da_semana.index, 
         autopct = '%.2f%%', explode = explodir, shadow = True)  # aqui
eixo.set_title('Temperatura por dia da semana', fontsize = 15, pad = 10)
eixo

