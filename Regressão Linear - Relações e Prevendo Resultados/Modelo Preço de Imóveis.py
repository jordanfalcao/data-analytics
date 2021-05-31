#!/usr/bin/env python
# coding: utf-8

# # Valor estimado é o mesmo do modelo criado no exercício.

# In[3]:


import pickle

modelo = open('modelo_preco_imoveis','rb')
novo = pickle.load(modelo)
modelo.close()

area = 85
garagem = 3
banheiros = 4
lareira = 3
marmore = 1
andares = 1

entrada=[[area, garagem, banheiros, lareira, marmore, andares]]

print('$ {0:.2f}'.format(novo.predict(entrada)[0]))

