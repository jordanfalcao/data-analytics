#!/usr/bin/env python
# coding: utf-8

# <h2>Aula 04</h2>

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('iris.csv')


# In[5]:


df.head()


# <h3>Gráfico de Dispersão</h3>

# In[6]:


# gráfico de dispersão
fig = plt.figure(figsize=(15, 8))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.scatter(df['comprimento_sépala'], df['largura_sépala'])
eixo.set_title('Gráfico de dispersão', fontsize = 25, pad = 15)
eixo.set_xlabel('Comprimento da sépala', fontsize = 15)
eixo.set_ylabel('Largura da sépala', fontsize = 15)


# In[8]:


# alterando tamanho dos ticks
fig = plt.figure(figsize=(15, 8))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.scatter(df['comprimento_sépala'], df['largura_sépala'])
eixo.set_title('Gráfico de dispersão', fontsize = 25, pad = 15)
eixo.set_xlabel('Comprimento da sépala', fontsize = 15)
eixo.set_ylabel('Largura da sépala', fontsize = 15)
eixo.tick_params(labelsize = 15)


# In[13]:


# classificando por espécie, 3 plots no mesmo eixo
fig = plt.figure(figsize=(15, 8))
eixo = fig.add_axes([0, 0, 1, 1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}

for especie in df['espécie'].unique():
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'], color = cores[especie])

eixo.set_title('Gráfico de dispersão', fontsize = 25, pad = 15)
eixo.set_xlabel('Comprimento da sépala', fontsize = 15)
eixo.set_ylabel('Largura da sépala', fontsize = 15)
eixo.tick_params(labelsize = 15)
eixo.legend(cores, fontsize = 18)


# In[14]:


# adicionando marcadores
fig = plt.figure(figsize=(15, 8))
eixo = fig.add_axes([0, 0, 1, 1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}
marcadores = {'Iris-setosa': 'x', 'Iris-versicolor': 'o', 'Iris-virginica': 'v'}

for especie in df['espécie'].unique():
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'], 
                 color = cores[especie], marker = marcadores[especie])

eixo.set_title('Gráfico de dispersão', fontsize = 25, pad = 15)
eixo.set_xlabel('Comprimento da sépala', fontsize = 15)
eixo.set_ylabel('Largura da sépala', fontsize = 15)
eixo.tick_params(labelsize = 15)
eixo.legend(cores, fontsize = 18)


# In[16]:


# tamanho dos marcadores
fig = plt.figure(figsize=(15, 8))
eixo = fig.add_axes([0, 0, 1, 1])

cores = {'Iris-setosa': 'r', 'Iris-versicolor': 'b', 'Iris-virginica': 'g'}
marcadores = {'Iris-setosa': 'x', 'Iris-versicolor': 'o', 'Iris-virginica': 'v'}

for especie in df['espécie'].unique():
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'], tmp['largura_sépala'], 
                 color = cores[especie], marker = marcadores[especie],
                 s = 100)

eixo.set_title('Gráfico de dispersão', fontsize = 25, pad = 15)
eixo.set_xlabel('Comprimento da sépala', fontsize = 15)
eixo.set_ylabel('Largura da sépala', fontsize = 15)
eixo.tick_params(labelsize = 15)
eixo.legend(cores, fontsize = 18)


# <h3>Boxplot - Gráfico de Caixa</h3>

# In[17]:


# boxplot
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.boxplot(df['largura_pétala'])
eixo.set_title('Gráfico de caixa', fontsize = 15, pad = 10)
eixo.set_xticklabels(['largura_pétala'])


# In[21]:


# boxplot excluindo a espécie
fig = plt.figure(figsize = (8, 5))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.boxplot(df.drop('espécie', axis = 1).values)
eixo.set_title('Gráfico de caixa', fontsize = 15, pad = 10)
eixo.set_xticklabels(df.drop('espécie', axis = 1).columns)
eixo


# In[22]:


# adicionando cores
fig = plt.figure(figsize = (8, 5))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.boxplot(df.drop('espécie', axis = 1).values, patch_artist = True)
eixo.set_title('Gráfico de caixa', fontsize = 15, pad = 10)
eixo.set_xticklabels(df.drop('espécie', axis = 1).columns)
eixo


# In[23]:


# alterando cores
fig = plt.figure(figsize = (8, 5))
eixo = fig.add_axes([0, 0, 1, 1])

cores = ['red', 'blue', 'orange', 'green']

caixas = eixo.boxplot(df.drop('espécie', axis = 1).values, patch_artist = True)
eixo.set_title('Gráfico de caixa', fontsize = 15, pad = 10)
eixo.set_xticklabels(df.drop('espécie', axis = 1).columns)

for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color = cor)

eixo


# In[25]:


# alterando marcadores de outliers
fig = plt.figure(figsize = (8, 5))
eixo = fig.add_axes([0, 0, 1, 1])

cores = ['red', 'blue', 'orange', 'green']

caixas = eixo.boxplot(df.drop('espécie', axis = 1).values, patch_artist = True)
eixo.set_title('Gráfico de caixa', fontsize = 15, pad = 10)
eixo.set_xticklabels(df.drop('espécie', axis = 1).columns)

for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color = cor)
    
for outlier in caixas['fliers']:
    outlier.set(marker = 'x', markersize = 8)

eixo


#  <h3>Histogramas</h3>

# In[29]:


# histograma
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.hist(df['comprimento_pétala'])
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)


# In[30]:


# divisões/bins
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.hist(df['comprimento_pétala'], bins = 20)
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)


# In[36]:


# horizontal/vertical
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.hist(df['comprimento_pétala'], bins = 20, orientation = 'horizontal')
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_ylabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)


# In[37]:


# horizontal/vertical
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.hist(df['comprimento_pétala'], bins = 20)
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)


# In[38]:


# normalizar / densidade
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

eixo.hist(df['comprimento_pétala'], bins = 20, density = True)
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)


# In[40]:


# inserindo média e desvio padrão
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

mu, sigma = df['comprimento_pétala'].mean(), df['comprimento_pétala'].std()

eixo.hist(df['comprimento_pétala'], bins = 20)
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)

eixo.annotate('$mu = {0:.2f}$\n$sigma = {1:.2f}$'.format(mu, sigma),
              xy = (4.5, 20), fontsize = 18)
eixo


# In[41]:


# reta da média
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

mu, sigma = df['comprimento_pétala'].mean(), df['comprimento_pétala'].std()

eixo.hist(df['comprimento_pétala'], bins = 20)
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)

eixo.annotate('$mu = {0:.2f}$\n$sigma = {1:.2f}$'.format(mu, sigma),
              xy = (4.5, 20), fontsize = 18)

eixo.axvline(mu, color = 'k', linestyle = '--')
eixo.annotate('média', xy = (mu - 1.3, 28), fontsize = 18)


# In[51]:


# reta da média e mediana
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

mu, sigma, mediana = df['comprimento_pétala'].mean(), df['comprimento_pétala'].std(),  df['comprimento_pétala'].median()

eixo.hist(df['comprimento_pétala'], bins = 20)
eixo.set_title('Histograma comprimento de pétala', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)

eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
              xy = (5, 20), fontsize = 18)

eixo.axvline(mu, color = 'k', linestyle = '--')
eixo.annotate('média', xy = (mu - 1.3, 30), fontsize = 18)

eixo.axvline(mediana, color = 'g', linestyle = '--')
eixo.annotate('mediana', xy = (mediana + 0.3, 30), fontsize = 18, color = 'g')

eixo


# In[58]:


# histograma apenas da Iris Versicolo / salvando imagem
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

df_iv = df[df['espécie'] == 'Iris-versicolor']
mu, sigma, mediana = df_iv['comprimento_pétala'].mean(), df_iv['comprimento_pétala'].std(),  df_iv['comprimento_pétala'].median()

eixo.hist(df_iv['comprimento_pétala'], bins = 20)
eixo.set_title('Iris Versicolor', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)

eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
              xy = (4.7, 6), fontsize = 18)

eixo.axvline(mu, color = 'k', linestyle = '--')
eixo.annotate('média', xy = (mu - 0.5, 5.5), fontsize = 18)

eixo.axvline(mediana, color = 'g', linestyle = '--')
eixo.annotate('mediana', xy = (mediana - 0.7, 6.5), fontsize = 18, color = 'g')

fig.savefig('histograma_iv.png', bbox_inches = 'tight')


# In[63]:


# histograma apenas da Iris Setosa / salvando imagem
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

df_is = df[df['espécie'] == 'Iris-setosa']
mu, sigma, mediana = df_is['comprimento_pétala'].mean(), df_is['comprimento_pétala'].std(),  df_is['comprimento_pétala'].median()

eixo.hist(df_is['comprimento_pétala'], bins = 20)
eixo.set_title('Iris Setosa', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)

eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
              xy = (1.7, 8), fontsize = 18)

eixo.axvline(mu, color = 'k', linestyle = '--')
eixo.annotate('média', xy = (mu - 0.2, 13), fontsize = 18)

eixo.axvline(mediana, color = 'g', linestyle = '--')
eixo.annotate('mediana', xy = (mediana + 0.05, 13), fontsize = 18, color = 'g')

fig.savefig('histograma_is.png', bbox_inches = 'tight')


# In[71]:


# histograma apenas da Iris Setosa / salvando imagem
fig = plt.figure(figsize = (5, 4))
eixo = fig.add_axes([0, 0, 1, 1])

df_ivg = df[df['espécie'] == 'Iris-virginica']
mu, sigma, mediana = df_ivg['comprimento_pétala'].mean(), df_ivg['comprimento_pétala'].std(),  df_ivg['comprimento_pétala'].median()

eixo.hist(df_ivg['comprimento_pétala'], bins = 20)
eixo.set_title('Iris Virginica', fontsize = 16, pad = 10)
eixo.set_xlabel('Comprimento da pétala', fontsize = 14)
eixo.grid(True)

eixo.annotate('$\mu = {0:.2f}$\n$\sigma = {1:.2f}$'.format(mu, sigma),
              xy = (6.4, 7), fontsize = 18)

eixo.axvline(mu, color = 'k', linestyle = '--')
eixo.annotate('média', xy = (mu, 8), fontsize = 18)

eixo.axvline(mediana, color = 'g', linestyle = '--')
eixo.annotate('mediana', xy = (mediana, 7), fontsize = 18, color = 'g')

fig.savefig('histograma_ivg.png', bbox_inches = 'tight')


# In[70]:


# importando Image da PIL
from PIL import Image


# In[78]:


# criando imagem combinada e salvando pela biblioteca PIL
largura, altura = Image.open('histograma_ivg.png').size
combinada = Image.new('RGB', (3*largura, altura))
intervalo = 0 

for imagem in map(Image.open, ['histograma_iv.png','histograma_is.png', 'histograma_ivg.png']):
    combinada.paste(imagem, (intervalo, 0))
    intervalo += largura
    
combinada.save('combinada.png')  # método diferente de salva da biblioteca PIL


# In[77]:


combinada

