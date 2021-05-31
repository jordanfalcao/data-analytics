#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: green; font-size: 36px; font-weight: bold;'>Data Science - Regressão Linear</h1>

# # <font color='red' style='font-size: 30px;'>Conhecendo o Dataset</font>
# <hr style='border: 2px solid red;'>

# ## Importando bibliotecas

# In[43]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## O Dataset e o Projeto
# <hr>
# 
# ### Fonte: https://www.kaggle.com/greenwing1985/housepricing
# 
# ### Descrição:
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Nosso objetivo neste exercício é criar um modelo de machine learning, utilizando a técnica de Regressão Linear, que faça previsões sobre os preços de imóveis a partir de um conjunto de características conhecidas dos imóveis.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Vamos utilizar um dataset disponível no Kaggle que foi gerado por computador para treinamento de machine learning para iniciantes. Este dataset foi modificado para facilitar o nosso objetivo, que é fixar o conhecimento adquirido no treinamento de Regressão Linear.</p>
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>Siga os passos propostos nos comentários acima de cada célular e bons estudos.</p>
# 
# ### Dados:
# <ul style='font-size: 18px; line-height: 2; text-align: justify;'>
#     <li><b>precos</b> - Preços do imóveis</li>
#     <li><b>area</b> - Área do imóvel</li>
#     <li><b>garagem</b> - Número de vagas de garagem</li>
#     <li><b>banheiros</b> - Número de banheiros</li>
#     <li><b>lareira</b> - Número de lareiras</li>
#     <li><b>marmore</b> - Se o imóvel possui acabamento em mármore branco (1) ou não (0)</li>
#     <li><b>andares</b> - Se o imóvel possui mais de um andar (1) ou não (0)</li>
# </ul>

# ## Leitura dos dados
# 
# Dataset está na pasta "Dados" com o nome "HousePrices_HalfMil.csv" em usa como separador ";".

# In[44]:


dados = pd.read_csv('HousePrices_HalfMil.csv', sep = ';')


# ## Visualizar os dados

# In[45]:


dados.head(10)


# ## Verificando o tamanho do dataset

# In[46]:


dados.shape


# # <font color='red' style='font-size: 30px;'>Análises Preliminares</font>
# <hr style='border: 2px solid red;'>

# ## Estatísticas descritivas

# In[47]:


dados.describe().round(3)


# ## Matriz de correlação
# 
# <p style='font-size: 18px; line-height: 2; margin: 10px 50px; text-align: justify;'>O <b>coeficiente de correlação</b> é uma medida de associação linear entre duas variáveis e situa-se entre <b>-1</b> e <b>+1</b> sendo que <b>-1</b> indica associação negativa perfeita e <b>+1</b> indica associação positiva perfeita.</p>
# 
# ### Observe as correlações entre as variáveis:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>Quais são mais correlacionadas com a variável dependete (Preço)?</li>
#     <li>Qual o relacionamento entre elas (positivo ou negativo)?</li>
#     <li>Existe correlação forte entre as variáveis explicativas?</li>
# </ul>

# In[48]:


dados.corr().round(4)


# - As variáveis explicativas mais correlacionadas são 'andares' e 'mármore';
# - Todas as variáveis explicativas se relacionam positivamente com a variável dependente (preço);
# - Existe correlação entre as variáveis explicativas, isso pode ser um problema para nosso modelo.

# # <font color='red' style='font-size: 30px;'>Comportamento da Variável Dependente (Y)</font>
# <hr style='border: 2px solid red;'>

# # Análises gráficas

# <img width='700px' src='../Dados/img/Box-Plot.png'>

# ## Importando biblioteca seaborn

# In[49]:


import seaborn as sns


# ## Configure o estilo e cor dos gráficos (opcional)

# In[50]:


sns.set_palette('BuPu_r')
sns.set_style('darkgrid')


# ## Box plot da variável *dependente* (y)
# 
# 
# ### Avalie o comportamento da distribuição da variável dependente:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>Parecem existir valores discrepantes (outliers)?</li>
#     <li>O box plot apresenta alguma tendência?</li>
# </ul>

# https://seaborn.pydata.org/generated/seaborn.boxplot.html?highlight=boxplot#seaborn.boxplot

# In[51]:


# boxplot do preço
ax = sns.boxplot(data = dados['precos'], orient = 'v', width = 0.2)
ax.figure.set_size_inches(12, 6)
ax.set_title('Preço dos Imóveis', fontsize = 20)
ax.set_ylabel('Reais - R$', fontsize = 16)
ax


# - Aparentemente, temos uma variável dependente simétrica;
# - Não visualizamos outliers (valores discrepantes) no preço dos imóveis.

# ## Investigando a variável *dependente* (y) juntamente com outras característica
# 
# Faça um box plot da variável dependente em conjunto com cada variável explicativa (somente as categóricas).
# 
# ### Avalie o comportamento da distribuição da variável dependente com cada variável explicativa categórica:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>As estatísticas apresentam mudança significativa entre as categorias?</li>
#     <li>O box plot apresenta alguma tendência bem definida?</li>
# </ul>

# ### Box-plot (Preço X Garagem)

# In[52]:


# boxplot do preço de acordo coma quantidade de vagas na garagem
ax = sns.boxplot(y = 'precos', x = 'garagem', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Preço dos Imóveis x Vagas de Garagem', fontsize = 20)
ax.set_ylabel('Reais - R$', fontsize = 16)
ax.set_xlabel('Vagas de Garagem', fontsize = 16)
ax


# ### Box-plot (Preço X Banheiros)

# In[53]:


# boxplot do preço de acordo coma quantidade de banheiros
ax = sns.boxplot(y = 'precos', x = 'banheiros', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(14, 6)
ax.set_title('Preço dos Imóveis x Banheiros', fontsize = 20)
ax.set_ylabel('Reais - R$', fontsize = 16)
ax.set_xlabel('Quantidade de Banheiros', fontsize = 16)
ax


# ### Box-plot (Preço X Lareira)

# In[54]:


# boxplot do preço de acordo coma quantidade de lareiras
ax = sns.boxplot(y = 'precos', x = 'lareira', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(14, 6)
ax.set_title('Preço dos Imóveis x Lareiras', fontsize = 20)
ax.set_ylabel('Reais - R$', fontsize = 16)
ax.set_xlabel('Quantidade de Lareiras', fontsize = 16)
ax


# ### Box-plot (Preço X Acabamento em Mármore)

# In[55]:


# boxplot do preço de acordo com acabamento em mármore
ax = sns.boxplot(y = 'precos', x = 'marmore', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Preço dos Imóveis x Acabamento em Mármore', fontsize = 20)
ax.set_ylabel('Reais - R$', fontsize = 16)
ax.set_xlabel('Acabamento em Mármore', fontsize = 16)
ax


# ### Box-plot (Preço X Andares)

# In[56]:


# boxplot do preço de acordo coma quantidade de andares
ax = sns.boxplot(y = 'precos', x = 'andares', data = dados, orient = 'v', width = 0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Preço dos Imóveis x Andares', fontsize = 20)
ax.set_ylabel('Reais - R$', fontsize = 16)
ax.set_xlabel('Quantidade de Andares', fontsize = 16)
ax


# - Nota-se uma tendência de crescimento no valor do imóvel com o aumento da quantidade de banheiros, vagas de garagem e lareiras.
# 
# - É notório, também, que os imóveis que tem 1º andar são mais caros que os que são apenas térreo.
# 
# - Vê-se, ainda, que os imóveis com acabamento em mármore tem o valor mais elevado que aqueles que não possuem.

# ## Distribuição de frequências da variável *dependente* (y)
# 
# Construa um histograma da variável dependente (Preço).
# 
# ### Avalie:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>A distribuição de frequências da variável dependente parece ser assimétrica?</li>
#     <li>É possível supor que a variável dependente segue uma distribuição normal?</li>
# </ul>

# https://seaborn.pydata.org/generated/seaborn.distplot.html?highlight=distplot#seaborn.distplot

# In[69]:


ax = dados['precos'].hist(bins = 10, legend = True)
ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequência dos Preços', fontsize = 20)
ax.set_xlabel('Reais - R$', fontsize = 14)
ax


# - O gráfico da Distribuição de Frequência dos Preços aparenta uma distribuição normal, com preços concentrados na faixa entre 35.000,00 e 55.000,00 reais.

# ## Gráficos de dispersão entre as variáveis do dataset

# ## Plotando o pairplot fixando somente uma variável no eixo y
# 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot
# 
# Plote gráficos de dispersão da variável dependente contra cada variável explicativa. Utilize o pairplot da biblioteca seaborn para isso.
# 
# Plote o mesmo gráfico utilizando o parâmetro kind='reg'.
# 
# ### Avalie:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>É possível identificar alguma relação linear entre as variáveis?</li>
#     <li>A relação é positiva ou negativa?</li>
#     <li>Compare com os resultados obtidos na matriz de correlação.</li>
# </ul>

# In[75]:


# apenas a variável 'precos'
ax = sns.pairplot(dados, y_vars = 'precos', x_vars = ['area','garagem', 'banheiros', 'lareira', 'marmore', 'andares'])
ax.fig.suptitle('Dispersão entre Variáveis', fontsize = 20, y = 1.08)
ax


# In[76]:


# apenas a variável 'precos'
ax = sns.pairplot(dados, y_vars = 'precos', x_vars = ['area','garagem', 'banheiros', 'lareira', 'marmore', 'andares'], kind = 'reg')
ax.fig.suptitle('Dispersão entre Variáveis', fontsize = 20, y = 1.08)
ax


# - Pelos gráficos e comparando com nossa matriz correlação, nota-se que a variável dependente (preço) tem uma 'relação positiva' com as variáveis explicativas, ou seja, quanto maior a área e mais vagas de garagem, banheiros, lareiras e andares, maior o Preço. 

# # <font color='red' style='font-size: 30px;'>Estimando um Modelo de Regressão Linear</font>
# <hr style='border: 2px solid red;'>

# ## Importando o *train_test_split* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# In[77]:


from sklearn.model_selection import train_test_split


# ## Criando uma Series (pandas) para armazenar a variável dependente (y)

# In[78]:


y = dados['precos']


# ## Criando um DataFrame (pandas) para armazenar as variáveis explicativas (X)

# In[79]:


X = dados[['area', 'garagem', 'banheiros', 'lareira', 'marmore', 'andares']]


# ## Criando os datasets de treino e de teste

# In[80]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=2811)


# ## Importando *LinearRegression* e *metrics* da biblioteca *scikit-learn*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# 
# https://scikit-learn.org/stable/modules/classes.html#regression-metrics

# In[81]:


from sklearn.linear_model import LinearRegression
from sklearn import metrics


# ## Instanciando a classe *LinearRegression()*

# In[82]:


modelo = LinearRegression()


# ## Utilizando o método *fit()* para estimar o modelo linear utilizando os dados de TREINO (y_train e X_train)
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit

# In[83]:


modelo.fit(X_train, y_train)


# ## Obtendo o coeficiente de determinação (R²) do modelo estimado com os dados de TREINO
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.score
# 
# 
# ### Avalie:
# <ul style='font-size: 16px; line-height: 2; text-align: justify;'>
#     <li>O modelo apresenta um bom ajuste?</li>
#     <li>Você lembra o que representa o R²?</li>
#     <li>Qual medida podemos tomar para melhorar essa estatística?</li>
# </ul>

# In[84]:


print('R² = {}'.format(modelo.score(X_train, y_train).round(3)))


# ## Gerando previsões para os dados de TESTE (X_test) utilizando o método *predict()*
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict

# In[88]:


y_previsto = modelo.predict(X_test)


# ## Obtendo o coeficiente de determinação (R²) para as previsões do nosso modelo
# 
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score

# In[89]:


print('R² = %s' % metrics.r2_score(y_test, y_previsto).round(3))


# # <font color='red' style='font-size: 30px;'>Obtendo Previsões Pontuais</font>
# <hr style='border: 2px solid red;'>

# ## Criando um simulador simples
# 
# Crie um simulador que gere estimativas de preço a partir de um conjunto de informações de um imóvel.

# In[90]:


area = 85
garagem = 3
banheiros = 4
lareira = 3
marmore = 1
andares = 1

entrada=[[area, garagem, banheiros, lareira, marmore, andares]]

print('$ {0:.2f}'.format(modelo.predict(entrada)[0]))


# # <font color='red' style='font-size: 30px;'>Métricas de Regressão</font>
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
# ### Coeficiente de Determinação - R²
# 
# O coeficiente de determinação (R²) é uma medida resumida que diz quanto a linha de regressão ajusta-se aos dados. É um valor entra 0 e 1.
# 
# $$R^2(y, \hat{y}) = 1 - \frac {\sum_{i=0}^{n-1}(y_i-\hat{y}_i)^2}{\sum_{i=0}^{n-1}(y_i-\bar{y}_i)^2}$$

# ## Obtendo métricas para o modelo com Temperatura Máxima

# In[92]:


eqm = metrics.mean_squared_error(y_test, y_previsto).round(3)
reqm = np.sqrt(metrics.mean_squared_error(y_test, y_previsto)).round(2)
R2 = metrics.r2_score(y_test, y_previsto).round(3)

pd.DataFrame([eqm, reqm, R2], ['EQM', 'REQM', 'R²'], columns = ['Métricas'])


# # <font color='red' style='font-size: 30px;'>Salvando e Carregando o Modelo Estimado</font>
# <hr style='border: 2px solid red;'>

# ## Importando a biblioteca pickle

# In[93]:


import pickle


# ## Salvando o modelo estimado

# In[94]:


output = open('modelo_preco_imoveis', 'wb') # wb write binary
pickle.dump(modelo, output)
output.close()


# ### Em um novo notebook/projeto Python
# 
# <h4 style='color: blue; font-weight: normal'>In [1]:</h4>
# 
# ```sh
# import pickle
# 
# modelo = open('modelo_preço','rb')
# lm_new = pickle.load(modelo)
# modelo.close()
# 
# area = 38
# garagem = 2
# banheiros = 4
# lareira = 4
# marmore = 0
# andares = 1
# 
# entrada = [[area, garagem, banheiros, lareira, marmore, andares]]
# 
# print('$ {0:.2f}'.format(lm_new.predict(entrada)[0]))
# ```
# 
# <h4 style='color: red; font-weight: normal'>Out [1]:</h4>
# 
# ```
# $ 46389.80
# ```
