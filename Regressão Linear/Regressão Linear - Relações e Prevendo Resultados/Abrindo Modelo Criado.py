#!/usr/bin/env python
# coding: utf-8

# # Este notebook está na mesma pasta que nosso modelo criado.

# In[1]:


import pickle

modelo = open('modelo_consumo_cerveja','rb') # rb read binary
lm_new = pickle.load(modelo)
modelo.close()

temp_max = 30.5
chuva = 12.2
fds = 0
entrada = [[temp_max, chuva, fds]]
print('{0:.2f} litros'.format(lm_new.predict(entrada)[0]))

