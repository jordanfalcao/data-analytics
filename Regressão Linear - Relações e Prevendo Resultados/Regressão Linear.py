#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: green; font-size: 36px; font-weight: bold;'>Data Science - Regressão Linear</h1>

# # <font color='red' style='font-size: 30px;'>Conhecendo o Dataset</font>
# <hr style='border: 2px solid red;'>

# ## Importando bibliotecas
# 
# https://matplotlib.org/
# 
# https://pandas.pydata.org/
# 
# http://www.numpy.org/

# In[118]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np


# ## Bibliotecas opcionais
# 
# https://docs.python.org/3/library/warnings.html

# In[119]:


import warnings

warnings.filterwarnings('ignore') # ou warnings.filterwarnings('action = 'once')


# ## O Dataset e o Projeto
# <hr>
# 
# ### Fonte: https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo
# 
# ### Descrição:
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>A cerveja é uma das bebidas mais democráticas e consumidas no mundo. Não sem razão, é perfeito para quase todas as situações, desde o happy hour até grandes festas de casamento.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O objetivo deste treinamento será estimar um modelo de <b>Machine Learning</b> utilizando a técnica de <b>Regressão Linear</b> para demonstrar os impactos das variáveis disponibilizadas neste dataset sobre o consumo de cerveja (Y). No final do projeto teremos um modelo de previsão para o consumo médio de cerveja segundo os inputs de um conjunto de variáveis (X's).</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Os dados (amostra) foram coletados em São Paulo - Brasil, em uma área universitária, onde existem algumas festas com grupos de alunos de 18 a 28 anos de idade (média).</p>
# 
# ### Dados:
# <ul style='font-size: 18px; line-height: 2; text-align: justify;'>
#     <li><b>data</b> - Data</li>
#     <li><b>temp_media</b> - Temperatura Média (°C)</li>
#     <li><b>temp_min</b> - Temperatura Mínima (°C)</li>
#     <li><b>temp_max</b> - Temperatura Máxima (°C)</li>
#     <li><b>chuva</b> - Precipitação (mm)</li>
#     <li><b>fds</b> - Final de Semana (1 = Sim; 0 = Não)</li>
#     <li><b>consumo</b> - Consumo de Cerveja (litros)</li>
# </ul>

# ## Leitura dos dados

# In[120]:


dados = pd.read_csv('../Dados/Consumo_cerveja.csv', sep = ';')


# ## Visualizar os dados

# In[121]:


dados.head(10)


# ## Verificando o tamanho do dataset

# In[122]:


dados.shape


# # <font color='red' style='font-size: 30px;'>Análises Preliminares</font>
# <hr style='border: 2px solid red;'>

# ## Estatísticas descritivas

# In[123]:


# .describe() mostra algumas estatítiscas descritivas
dados.describe().round(2)


# ## Matriz de correlação
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>coeficiente de correlação</b> é uma medida de associação linear entre duas variáveis e situa-se entre <b>-1</b> e <b>+1</b> sendo que <b>-1</b> indica associação negativa perfeita e <b>+1</b> indica associação positiva perfeita.</p>

# In[124]:


# .corr() apresenta a correlação entre todas as variáveis
dados.corr().round(4)


# # <font color='red' style='font-size: 30px;'>Comportamento da Variável Dependente (Y)</font>
# <hr style='border: 2px solid red;'>

# # Análises gráficas

# ## Plotando a variável *dependente* (y)
# https://pandas.pydata.org/pandas-docs/stable/visualization.html

# In[125]:


# destructuring subplot retorna uma tupla
fig, ax = plt.subplots(figsize = (20, 6))


# comportamento do consumo ao longo do ano
ax.set_title('Consumo de Cerveja', fontsize = 20)
ax.set_ylabel('Litros', fontsize = 16)
ax.set_xlabel('Dias', fontsize = 16)
ax = dados['consumo'].plot(fontsize = 14)


# # <font color='red' style='font-size: 30px;'>Box Plot</font>
# <hr style='border: 2px solid red;'>

# <img width='700px' src='../Dados/img/Box-Plot.png'>

# ## Importando biblioteca seaborn
# https://seaborn.pydata.org/
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O Seaborn é uma biblioteca Python de visualização de dados baseada no matplotlib. Ela fornece uma interface de alto nível para desenhar gráficos estatísticos.</p>

# In[126]:


import seaborn as sns


# ## Box plot da variável *dependente* (y)

# https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot

# In[127]:


# boxplot do consumo
ax = sns.boxplot(data = dados['consumo'], orient = 'v', width = 0.2)
ax.figure.set_size_inches(12, 6)
ax.set_title('Consumo de Cerveja', fontsize = 20)
ax.set_ylabel('Litros', fontsize = 16)
ax


# # <font color='red' style='font-size: 30px;'>Box Plot com Duas Variáveis</font>
# <hr style='border: 2px solid red;'>

# ## Investigando a variável *dependente* (y) segundo determinada característica

# In[128]:


# boxplot do consumo
ax = sns.boxplot(y = 'consumo', x = 'fds', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Consumo de Cerveja', fontsize = 20)
ax.set_ylabel('Litros', fontsize = 16)
ax.set_xlabel('Final de Semana', fontsize = 16)
ax


# ## Configurações de estilo e cor da biblioteca *seaborn*
# 
# ### Controle de estilo
# 
# > ####  API
# > https://seaborn.pydata.org/api.html#style-api
# 
# > #### Tutorial
# > https://seaborn.pydata.org/tutorial/aesthetics.html#aesthetics-tutorial
# 
# ### Paleta de cores
# 
# > #### API
# > https://seaborn.pydata.org/api.html#palette-api
# 
# > #### Tutorial
# > https://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial

# Todos os palettes da Seaborn
# 
# https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f

# In[129]:


# palette -> Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r...
sns.set_palette('Accent')

# style -> white, dark, whitegrid, darkgrid, ticks
sns.set_style('darkgrid')


# In[130]:


# boxplot do consumo
ax = sns.boxplot(y = 'consumo', x = 'fds', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Consumo de Cerveja', fontsize = 20)
ax.set_ylabel('Litros', fontsize = 16)
ax.set_xlabel('Final de Semana', fontsize = 16)
ax


# # <font color='red' style='font-size: 30px;'>Distribuição de Frequências</font>
# <hr style='border: 2px solid red;'>

# ## Distribuição de frequências da variável *dependente* (y)

# https://seaborn.pydata.org/generated/seaborn.distplot.html?highlight=distplot#seaborn.distplot

# In[131]:


ax = sns.distplot(dados['consumo'])
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências', fontsize = 20)
ax.set_ylabel('Consumo de Cerveja - Litros', fontsize = 16)
ax


# # <font color='red' style='font-size: 30px;'>Variável Dependente X Variáveis Explicativas (pairplot)</font>
# <hr style='border: 2px solid red;'>

# ## Gráficos de dispersão entre as variáveis do dataset

# ## seaborn.pairplot
# 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota o relacionamento entre pares de variáveis em um dataset.</p>

# In[132]:


# gráfico de dispersão
ax = sns.pairplot(dados)


# ## Plotando o pairplot fixando somente uma variável no eixo y

# In[133]:


# apenas uma ou mais variáveis variável (consumo)
ax = sns.pairplot(dados, y_vars = 'consumo', x_vars = ['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'])
ax.fig.suptitle('Dispersão entre Variáveis', fontsize = 20, y = 1.08)
ax


# In[134]:


# kind = 'reg', estima uma reta de regressão entre as duas variáveis
ax = sns.pairplot(dados, y_vars = 'consumo', x_vars = ['temp_min', 'temp_media', 'temp_max', 'chuva', 'fds'], kind = 'reg')
ax.fig.suptitle('Dispersão entre Variáveis', fontsize = 20, y = 1.08)
ax


# # <font color='red' style='font-size: 30px;'>Variável Dependente X Variáveis Explicativas (jointplot)</font>
# <hr style='border: 2px solid red;'>

# ## seaborn.jointplot
# 
# https://seaborn.pydata.org/generated/seaborn.jointplot.html?highlight=jointplot#seaborn.jointplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota o relacionamento entre duas variáveis e suas respectivas distribuições de frequência.</p>

# In[135]:


# além do relacionamento entre variáveis, plota as respectivas distribuições de frequências
ax = sns.jointplot(x="temp_max", y="consumo", data=dados)

ax.fig.suptitle('Dispersao - Consumo X Temperatura', fontsize=18, y=1.05)
ax.set_axis_labels("Temperatura Máxima", "Consumo de Cerveja", fontsize=14)
ax


# ## Plotando um jointplot com a reta de regressão estimada

# In[136]:


ax = sns.jointplot(x="temp_max", y="consumo", data=dados, kind = 'reg')

ax.fig.suptitle('Dispersao - Consumo X Temperatura', fontsize=18, y=1.05)
ax.set_axis_labels("Temperatura Máxima", "Consumo de Cerveja", fontsize=14)
ax


# # <font color='red' style='font-size: 30px;'>Variável Dependente X Variáveis Explicativas (lmplot)</font>
# <hr style='border: 2px solid red;'>

# ## seaborn.lmplot
# 
# https://seaborn.pydata.org/generated/seaborn.lmplot.html?highlight=lmplot#seaborn.lmplot
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Plota a reta de regressão entre duas variáveis juntamente com a dispersão entre elas.</p>

# In[137]:


# lmplot
ax = sns.lmplot(x = 'temp_max', y = 'consumo', data = dados)

ax.fig.suptitle('Reta de Regressao - Consumo X Temperatura', fontsize=16, y=1.02)
ax.set_xlabels("Temperatura Máxima (°C)", fontsize=14)
ax.set_ylabels("Consumo de Cerveja (litros)", fontsize=14)

ax


# ## Plotando um lmplot utilizando uma terceira variável na análise (tipo I)

# In[138]:


# parâmetro hue agrupa o gráfico por uma 3ª variável
ax = sns.lmplot(x = 'temp_max', y = 'consumo', data = dados, hue = 'fds', markers = ['o', '*'], legend = False)

ax.fig.suptitle('Reta de Regressao - Consumo X Temperatura', fontsize=16, y=1.02)
ax.set_xlabels("Temperatura Máxima (°C)", fontsize=14)
ax.set_ylabels("Consumo de Cerveja (litros)", fontsize=14)
ax.add_legend(title = 'Fim de Semana')

ax


# ## Plotando um lmplot utilizando uma terceira variável na análise (tipo II)

# In[139]:


# parâmetro col separa o gráfico por uma 3ª variável
ax = sns.lmplot(x = 'temp_max', y = 'consumo', data = dados, col = 'fds')

ax.fig.suptitle('Reta de Regressao - Consumo X Temperatura', fontsize=16, y=1.02)
ax.set_xlabels("Temperatura Máxima (°C)", fontsize=14)
ax.set_ylabels("Consumo de Cerveja (litros)", fontsize=14)
ax.add_legend(title = 'Fim de Semana')

ax


# # <font color='red' style='font-size: 30px;'>Estimando um Modelo de Regressão Linear para o Consumo</font>
# <hr style='border: 2px solid red;'>

# # Regresão Linear
# <hr>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>A análise de regressão diz respeito ao estudo da dependência de uma variável (a variável <b>dependente</b>) em relação a uma ou mais variáveis, as variáveis explanatórias, visando estimar e/ou prever o valor médio da primeira em termos dos valores conhecidos ou fixados das segundas.</p>
# 
# 
# ## scikit-learn (https://scikit-learn.org/stable/)
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O *scikit-learn* é um módulo Python especializado em soluções para *machine learning*.</p>
# 
# 

# ## Importando o *train_test_split* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# In[140]:


# importando função train_test_split da biblioteca sklearn
from sklearn.model_selection import train_test_split


# ## Criando uma Series (pandas) para armazenar o Consumo de Cerveja (y)

# In[141]:


# primeiramente separar nossas variáveis dependentes e explicativas
y = dados['consumo']   # variável dependente


# ## Criando um DataFrame (pandas) para armazenar as variáveis explicativas (X)

# In[142]:


# variáveis explicativas
X = dados[['temp_max', 'chuva', 'fds']]


# ## Criando os datasets de treino e de teste

# In[143]:


# train_test_split separa o DF em subconjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2811) # test 30%


# ## Verificando os tamanhos dos arquivos gerados pela função *train_test_split*

# In[144]:


# 70%
X_train.shape


# In[145]:


# 30%
X_test.shape


# In[146]:


# valor total
X_train.shape[0] + X_test.shape[0]


# In[147]:


# X original
X.shape[0] * 0.3


# In[148]:


X.shape[0] * 0.7


# <img width='600px' src='../Dados/img/reg_01.jpg'>

# ## Importando *LinearRegression* e *metrics* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# 
# https://scikit-learn.org/stable/modules/classes.html#regression-metrics

# In[149]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics


# ## Instanciando a classe *LinearRegression()*

# In[150]:


modelo = LinearRegression()


# ## Utilizando o método *fit()* do objeto "modelo" para estimar nosso modelo linear utilizando os dados de TREINO (X_train e y_train)
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit

# In[151]:


# treinando o modelo criado
modelo.fit(X_train, y_train)


# ## Obtendo o coeficiente de determinação (R²) do modelo estimado com os dados de TREINO
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.score
# 
# ### Coeficiente de Determinação - R²
# 
# O coeficiente de determinação (R²) é uma medida resumida que diz quanto a linha de regressão ajusta-se aos dados. É um valor entra 0 e 1.
# 
# $$R^2(y, \hat{y}) = 1 - \frac {\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}{\sum_{i=0}^{n-1}(y_i-\bar{y}_i)^2}$$

# In[152]:


# modelo.score(X_train, y_train) aprensenta o Coeficiente de Determinação R²
print('R² = {}'.format(modelo.score(X_train, y_train).round(3))) # quanto mais próximo de 1, melhor


# ## Gerando previsões para os dados de TESTE (X_test) utilizando o método *predict()* do objeto "modelo"
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict

# In[177]:


# .predict() consumo previsto pra cada entrada
y_previsto = modelo.predict(X_test)


# ## Obtendo o coeficiente de determinação (R²) para as previsões do nosso modelo
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score

# In[154]:


# metrics.r2_score()
print('R² = %s' % metrics.r2_score(y_test, y_previsto).round(3))


# # <font color='red' style='font-size: 30px;'>Obtendo Previsões Pontuais</font>
# <hr style='border: 2px solid red;'>

# ## Dados de entrada

# In[159]:


# primeira linha do X_test
entrada = X_test[0:1]
entrada


# ## Gerando previsão pontual

# In[160]:


# previsão para entraa específica
modelo.predict(entrada)[0]


# ## Criando um simulador simples

# In[164]:


# atribui-se uma entrada e para prever uma saída (consumo)
temp_max = 40
chuva = 0
fds = 1
entrada = [[temp_max, chuva, fds]]

print('{0:.2f} litros'.format(modelo.predict(entrada)[0]))


# # <font color='red' style='font-size: 30px;'>Interpretação dos Coeficientes Estimados</font>
# <hr style='border: 2px solid red;'>

# <img width='600px' src='../Dados/img/reg_02.jpg'>

# ## Obtendo o intercepto do modelo
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>intercepto</b> representa o efeito médio em $Y$ (Consumo de Cerveja) tendo todas as variáveis explicativas excluídas do modelo. De forma mais simples, o <b>intercepto</b> representa o efeito médio em $Y$ (Consumo de Cerveja) quando $X_2$ (Temperatura Máxima), $X_3$ (Chuva) e $X_4$ (Final de Semana) são iguais a zero.</p>

# In[166]:


# consumo de cerveja (ß1) zerando as variáveis explicativas
modelo.intercept_     # .intercept_


# In[168]:


type(modelo.intercept_)


# ## Obtendo os coeficientes de regressão
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>Os <b>coeficientes de regressão</b> $\beta_2$, $\beta_3$ e $\beta_4$ são conhecidos como <b>coeficientes parciais de regressão</b> ou <b>coeficientes parciais angulares</b>. Considerando o número de variáveis explicativas de nosso modelo, seu significado seria o seguinte: $\beta_2$ mede a variação no valor médio de $Y$ (Consumo de Cerveja), por unidade de variação em $X_2$ (Temperatura Máxima), mantendo-se os valores de $X_3$ (Chuva) e $X_4$ (Final de Semana) constantes. Em outras palavras, ele nos dá o efeito "direto" ou "líquido" de uma unidade de variação em $X_2$ sobre o valor médio de $Y$, excluídos os efeitos que $X_3$ e $X_4$ possam ter sobre a média de $Y$. De modo análogo podemos interpretar os demais coeficientes de regressão.</p>

# In[169]:


# .coef_ para obtermos os ß2, ß2 e ß4
modelo.coef_


# In[170]:


type(modelo.coef_)


# ## Confirmando a ordem das variáveis explicativas no DataFrame

# In[171]:


X.columns


# ## Criando uma lista com os nomes das variáveis do modelo

# In[175]:


index = ['Intercepto', 'Temperatura Máxima', 'Chuva (mm)', 'Fim de Semana']


# ## Criando um DataFrame para armazenar os coeficientes do modelo
# 
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html?#numpy.append

# In[176]:


pd.DataFrame(data = np.append(modelo.intercept_, modelo.coef_), index = index, columns = ['Parâmetros'])


# ## Interpretação dos Coeficientes Estimados
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Intercepto</b> → Excluindo o efeito das variáveis explicativas ($X_2=X_3=X_4=0$) o efeito médio no Consumo de Cerveja seria de <b>5951,98 litros</b>.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Temperatura Máxima (°C)</b> → Mantendo-se os valores de $X_3$ (Chuva) e $X_4$ (Final de Semana) constantes, o acréscimo de 1°C na Temperatura Máxima gera uma variação média no Consumo de Cerveja de <b>684,74 litros</b>.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Chuva (mm)</b> → Mantendo-se os valores de $X_2$ (Temperatura Máxima) e $X_4$ (Final de Semana) constantes, o acréscimo de 1mm de Chuva gera uma variação média no Consumo de Cerveja de <b>-60,78 litros</b>.
# </p>
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>
# <b>Final de Semana (Sim/Não)</b> → Mantendo-se os valores de $X_2$ (Temperatura Máxima) e $X_3$ (Chuva) constantes, o fato de o dia ser classificado como Final de Semana gera uma variação média no Consumo de Cerveja de <b>5401,08 litros</b>.
# </p>

# # <font color='red' style='font-size: 30px;'>Análises Gráficas das Previsões do Modelo</font>
# <hr style='border: 2px solid red;'>

# ## Gerando as previsões do modelo para os dados de TREINO

# In[179]:


y_previsto_train = modelo.predict(X_train)


# ## Gráfico de dispersão entre valor estimado e valor real
# 
# https://seaborn.pydata.org/generated/seaborn.scatterplot.html

# In[183]:


ax = sns.scatterplot(x = y_previsto_train, y = y_train)

ax.figure.set_size_inches(12, 6)
ax.set_title('Previsão x Real', fontsize = 18)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize = 14)
ax.set_ylabel('Consumo de Cerveja (litros) - Real', fontsize = 14)
ax


# ## Obtendo os resíduos

# In[181]:


# erro 
residuo = y_train - (y_previsto_train)


# ## Gráfico de dispersão entre valor estimado e resíduos
# 
# Método informal de verificação da hipótese de variância constante dos resíduos (homocedasticidade)

# In[186]:


ax = sns.scatterplot(x = y_previsto_train, y = residuo, s = 150)
ax.figure.set_size_inches(20, 8)
ax.set_title('Resíduo x Previsão', fontsize = 18)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize = 14)
ax.set_ylabel('Resíduos', fontsize = 14)
ax


# ## Utilizando os resíduos ao quadrado

# <img width='800px' src='../Dados/img/var_u.jpg'>
# Fonte: Econometria Básica - 5ª edição - Gujarati e Porter

# In[188]:


ax = sns.scatterplot(x = y_previsto_train, y = residuo ** 2, s = 150)
ax.figure.set_size_inches(20, 8)
ax.set_title('Resíduo x Previsão', fontsize = 18)
ax.set_xlabel('Consumo de Cerveja (litros) - Previsão', fontsize = 14)
ax.set_ylabel('Resíduos²', fontsize = 14)
ax  # formato de cone, variância não é constante


# ## Plotando a distribuição de frequências dos resíduos

# In[191]:


ax = sns.distplot(residuo)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências dos Resíduos', fontsize = 18)
ax.set_xlabel('Litros', fontsize = 14)

ax  # lembra uma curva normal


# # <font color='red' style='font-size: 30px;'>Comparando Modelos</font>
# <hr style='border: 2px solid red;'>

# ## Estimando um novo modelo com a substituição da variável explicativa Temperatura Máxima pela Temperatuda Média

# In[192]:


# alterando a temperatura máxima pela média
X2 = dados[['temp_media', 'chuva', 'fds']]


# ## Criando os datasets de treino e de teste

# In[193]:


# novos subconjuntos com a Temperatura Média
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.3, random_state=2811) # test 30%


# ## Instanciando a classe *LinearRegression()*

# In[194]:


modelo_2 = LinearRegression()


# ## Utilizando o método *fit()* do objeto "modelo_2" para estimar nosso modelo linear utilizando os dados de TREINO (y2_train e X2_train)

# In[195]:


modelo_2.fit(X2_train, y2_train)


# ## Obtendo o coeficiente de determinação (R²) do novo modelo estimado e comparando com o resultado do modelo anterior

# In[203]:


# modelo.score(X_train, y_train) determinação R²
print('Modelo com Temp. Média:')
print('R² = {}'.format(modelo_2.score(X2_train, y2_train).round(3)))


# In[201]:


# modelo com Temperatura Máxima
print('Modelo com Temp. Máxima:')
print('R² = {}'.format(modelo.score(X_train, y_train).round(3)))


# ## Gerando previsões para os dados de TESTE (X_test e X2_test) utilizando o método *predict()* dos objetos "modelo" e "modelo_2"

# In[200]:


y_previsto = modelo.predict(X_test)
y_previsto_2 = modelo_2.predict(X2_test)


# ## Obtendo o coeficiente de determinação (R²) para as previsões dos dois modelos

# In[204]:


print('Modelo com Temp. Média:')
print('R² = {}'.format(metrics.r2_score(y2_test, y_previsto_2).round(3)))


# In[205]:


print('Modelo com Temp. Máxima:')
print('R² = {}'.format(metrics.r2_score(y_test, y_previsto).round(3)))


# # <font color='red' style='font-size: 30px;'>Outras Métricas de Regressão</font>
# <hr style='border: 2px solid red;'>

# ## Métricas da regressão
# <hr>
# 
# fonte: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics
# 
# Algumas estatísticas obtidas do modelo de regressão são muito úteis como critério de comparação entre modelos estimados e de seleção do melhor modelo, as principais métricas de regressão que o scikit-learn disponibiliza para modelos lineares são as seguintes:
# 
# ### Erro Quadrático Médio
# 
# Média dos quadrados dos erros. Ajustes melhores apresentam $EQM$ mais baixo.
# 
# $$EQM(y, \hat{y}) = \frac 1n\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2$$
# 
# ### Raíz do Erro Quadrático Médio
# 
# Raíz quadrada da média dos quadrados dos erros. Ajustes melhores apresentam $\sqrt{EQM}$ mais baixo.
# 
# $$\sqrt{EQM(y, \hat{y})} = \sqrt{\frac 1n\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}$$
# 
# 

# ## Obtendo métricas para o modelo com Temperatura Média

# In[206]:


eqm_2 = metrics.mean_squared_error(y2_test, y_previsto_2).round(3)
reqm_2 = np.sqrt(metrics.mean_squared_error(y2_test, y_previsto_2)).round(3)
R2_2 = metrics.r2_score(y2_test, y_previsto_2).round(3)

pd.DataFrame([eqm_2, reqm_2, R2_2], ['EQM', 'REQM', 'R²'], columns = ['Métricas'])


# ## Obtendo métricas para o modelo com Temperatura Máxima

# In[207]:


eqm = metrics.mean_squared_error(y_test, y_previsto).round(3)
reqm = np.sqrt(metrics.mean_squared_error(y_test, y_previsto)).round(3)
R2 = metrics.r2_score(y_test, y_previsto).round(3)

pd.DataFrame([eqm, reqm, R2], ['EQM', 'REQM', 'R²'], columns = ['Métricas'])


# # <font color='red' style='font-size: 30px;'>Salvando e Carregando o Modelo Estimado</font>
# <hr style='border: 2px solid red;'>

# ## Dados de entrada

# In[208]:


X_test[0:1]


# In[209]:


entrada = X_test[0:1]


# ## Gerando previsão pontual

# In[214]:


modelo.predict(entrada)[0]


# ## Criando um simulador simples

# In[216]:


temp_max = 40
chuva = 12.2
fds = 0
entrada = [[temp_max, chuva, fds]]

print('{0:.2f} litros'.format(modelo.predict(entrada)[0]))


# ## Salvando o modelo estimado

# ## pickle (https://docs.python.org/3/library/pickle.html)
# 
# <p style='font-size: 20px; line-height: 2; margin: 10px 50px; text-align: justify;'>O módulo <b>pickle</b> implementa protocolos binários para serializar e desserializar a estrutura de um objeto Python.</p>

# In[217]:


import pickle


# In[218]:


# open() e close()
# pickle.dump()
output = open('modelo_consumo_cerveja', 'wb') # wb write binary
pickle.dump(modelo, output)
output.close()


# ### Em um novo notebook/projeto Python
# 
# <h4 style='color: blue; font-weight: normal'>In [1]:</h4>
# 
# ```sh
# import pickle
# 
# modelo = open('modelo_consumo_cerveja','rb')
# lm_new = pickle.load(modelo)
# modelo.close()
# 
# temp_max = 30.5
# chuva = 12.2
# fds = 0
# entrada = [[temp_max, chuva, fds]]
# print('{0:.2f} litros'.format(lm_new.predict(entrada)[0]))
# ```
# 
# <h4 style='color: red; font-weight: normal'>Out [1]:</h4>
# 
# ```
# 26094.90 litros
# ```
