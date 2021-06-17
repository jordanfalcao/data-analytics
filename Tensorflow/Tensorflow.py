#!/usr/bin/env python
# coding: utf-8

# In[32]:


import tensorflow as tf
import pandas as pd
import numpy as np


# In[15]:


with tf.compat.v1.Session() as sess:
    frase = tf.constant('Olá, Mundo!')
    rodar = sess.run(frase)
print(rodar.decode('UTF-8'))


# In[17]:


frase = tf.constant('Olá, mundo!')
tf.print(frase)


# In[23]:


a = tf.constant(5)
b = tf.constant(3)
c = tf.constant(2)

d = tf.multiply(a, b)
e = tf.add(b, c)
f = tf.subtract(d, e)

tf.print(d, e, f)


# In[30]:


type(f)


# In[40]:


a = tf.constant(2)  # 1x1
b = tf.constant([3, 1, 5, 8, 6])  # 1xn
c = tf.constant([[2, 0, 4],[3, 5, 7]])  #nxn

tf.print(c)


# In[48]:


a1 = np.array(2)
b1 = np.array([3, 1, 5, 8, 6])
c1 = np.array([[2, 0, 4],[3, 5, 7]])


# In[47]:


print(a.shape)
print(a1.shape)
print(b.shape)
print(b1.shape)
print(c.shape)
print(c1.shape)


# In[55]:


const = tf.constant(4)
const_1 = tf.constant(4, dtype = tf.float64)  # inserindo o tipo


# In[56]:


print(const)
print(const_1)


# ## Multiplicação de matrizes

# In[76]:


A = tf.constant([[1, 2, 3], [4, 5, 6]])
B = tf.constant([[0, 0], [1, 0], [0, 1]])
x = tf.constant([0, 1, 0])


# In[60]:


tf.print(A)
tf.print(B)


# In[61]:


# multiplicando as matrizes
resultado = tf.matmul(A, B)
tf.print(resultado)


# In[64]:


# dá erro, não é possível multiplicar essas matrizes
# resultado = tf.matmul(A, x)


# In[78]:


# expandindo x para ter a quantidade de linhas igual a quantidade de colunas de A
x = tf.expand_dims(x, 1) # na prática, transpos a matriz


# In[73]:


resultado_2 = tf.matmul(A, x)
resultado_2


# In[81]:


transposta = tf.transpose(A)


# In[82]:


tf.print(A)
tf.print(transposta)


# ## Variáveis

# In[83]:


variavel = tf.Variable(2)


# In[84]:


tf.print(variavel)


# In[86]:


# criando uma matriz aleatória shape (3, 5)
matriz = tf.random.normal((3, 5), 0, 1) # ((linhas, colunas), média, desvio padrão)


# In[88]:


tf.print(matriz)


# In[89]:


variavel_2 = tf.Variable(matriz)


# In[90]:


# imprimindo a variável matriz
tf.print(variavel_2)


# In[92]:


# tipos das variáveis
print(matriz)     # tensor
print(variavel_2) # variable


# ## Placeholders

# In[94]:


dados_x = np.random.randn(4, 8)   # cria matriz de 4 linhas e 8 colunas com números aleatórios
dados_w = np.random.randn(8, 2)   # cria matriz de 8 linhas e 2 colunas com números aleatórios

b = tf.random.normal((4, 2), 0, 1, tf.float64)   # cria matriz (tensor) de 4 linhas e 2 colunas

operacao = tf.matmul(dados_x, dados_w) + b   # [4, 8] x [8, 2] = [4, 2]
maximo = tf.math.reduce_max(operacao) # encontra o maior valor da matriz operacao


# In[95]:


tf.print(operacao)  # matriz [4, 2]
tf.print(maximo)    # valor máximo


# In[96]:


x1 = np.random.randn(4,8)  
w1 = np.random.randn(8,2)


x2 = np.random.randn(4,8)  
w2 = np.random.randn(8,2)


x3 = np.random.randn(4,8)  
w3 = np.random.randn(8,2)

x4 = np.random.randn(4,8)  
w4 = np.random.randn(8,2)

x5 = np.random.randn(4,8)  
w5 = np.random.randn(8,2)

lista_x = [x1, x2, x3, x4, x5]
lista_w = [w1, w2, w3, w4, w5]
lista_saida = []

b = tf.random.normal((4,2),0,1, tf.float64)   # cria matriz (tensor) de 4 linhas e 2 colunas com números aleatórios

for i in range(5):
    operacao = (tf.matmul(lista_x[i], lista_w[i])) + b
    maximo = tf.reduce_max(operacao) # encontra o maior valor da matriz operacao
    lista_saida.append(maximo)


# In[ ]:


tf.print(lista_saida)

