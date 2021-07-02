# -*- coding: utf-8 -*-
"""ExperimentoTensorFlowSeno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cYH-PVeQO0vHQv-DMiegHYRzKM_Da9Go

# Modelo de regressão para uma fução conhecida em TensorFlow.Keras

### Nesse exemplo, vamos construir um modelo de predição para uma função matemática conhecida, de modo que possamos predizer um, ou mais, valores, a partir dos N valores anteriores dessa função. Utilizaremos para isso a função seno, e usaremos o conjunto TensorFlow keras para simplificar o processo de implementação desse exemplo.

## Inicialmente vamos inserir algumas bibliotecas no nosso projeto
"""

#importantdo as bibliotecas necessárias
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

"""## O Segundo passo é criar a base de dados necessária para o desenvolvimento do problema

#### Os Dados precisam ser organizados de modo que a entrada e a saida da rede representem a dinâmica do problema.
"""

# criação da função utilizada na informação e predição
def ProcessData(dado, intervalo_informacao, tamanho_predicao):
  '''
  dado = Conjunto de amostras usadas para o treinamento da rede
  intervalo_informação = Corresponde a quantidade de amostras que serão usadas para predição
  tamanho_predição = Corresponde a quantidade de amostras a serem preditas
  '''
  aux_a=np.zeros([len(dado)-(intervalo_informacao+tamanho_predicao),intervalo_informacao])
  aux_b=np.zeros([len(dado)-(intervalo_informacao+tamanho_predicao),tamanho_predicao])

  for i in range(len(dado)-(intervalo_informacao+tamanho_predicao)):
    aux_a[i] = dado[i:(i+intervalo_informacao)]
    aux_b[i] = dado[(i+intervalo_informacao):((i+intervalo_informacao)+tamanho_predicao)]

  return [aux_a,aux_b]

"""#### Vamos definir algumas variáveis auxiliares e o conjunto de de dados de entrada e saída do problema, para treinamento e teste."""

#criando o conjunto de dados para ser usados
freq = 60
num_periodos = 15

x1=np.linspace(0,num_periodos/freq,1000)
y1=(np.sin(2*np.pi*freq*x1)+1)/2
x2=x1[0:200]
y2=(np.sin(2*np.pi*freq*x2)+1)/2

# pré processamento de dados
[entrada_train, saida_train] = ProcessData(y1, 100, 10)
[entrada_test, saida_test] = ProcessData(y2, 100, 10)
print(saida_test.shape)

plt.figure(figsize=(15,6),dpi=110)
plt.plot(y1)
plt.plot(y2,'r')
plt.show()

entrada_train = tf.convert_to_tensor(entrada_train)
saida_train = tf.convert_to_tensor(saida_train)
entrada_test = tf.convert_to_tensor(entrada_test)
saida_test = tf.convert_to_tensor(saida_test)
#print(entrada_train.shape)
#print(saida_train.shape)
saida_train

"""### Uma vez criada a base de dados, vamos construir um modelo para regressão dos dados baseado em RNAs."""

# definindo o modelo
model = keras.Sequential([
    keras.Input(shape=(100,)),  # input layer (1)  não se mexe nesta camada
    keras.layers.Dense(20, activation='relu'),  # hidden layer (1)  activation pode ser 'relu', 'sigmoid'...
    keras.layers.Dense(10, activation='relu'),  # hidden layer (2)  mexe-se apenas nas hidden layers (quantidade de neurônios e tipo de função de ativação)
    keras.layers.Dense(10, activation='relu') # output layer   não se mexe nesta camada
])

# compilando o modelo
model.compile(optimizer='adam',   # otimizador 'adam'
              loss='mse',        # função de perda MSE - Mean Squared Error
              metrics=['accuracy'])

model.summary()

# O treinamento da rede é realizado usando o módulo fit e recebe como um dos 
# parâmetros a quantidade de iterações desejadas de minimização do erro.
model.fit(entrada_train, saida_train, shuffle=True, epochs=100)

"""### Uma vez treinada essa rede pode ser testada para avaliação de seu desempenho"""

test_loss, test_acc = model.evaluate(entrada_test,  saida_test, verbose=1) 

print('Test accuracy:', test_acc)

"""### Considerando o problema proposto devemos separar os dados para o treinamento de acordo com as restrições impostas no problema. Vamos usar um conjunto com 100 amostras de entrada para predizer as proximas 10 amostras de saída do sistema."""

# realizando uma predição
predictions = model.predict(entrada_test)

plt.figure(figsize=(15,6),dpi=110)
plt.plot(predictions[:,0],'*b')  
plt.plot(saida_test[:,0],'r')
plt.ylim([0,1.2])
plt.legend(['Dado Estimado','Dado Real'])
plt.show()

