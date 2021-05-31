#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: blue; font-size: 36px; font-weight: bold;'>Data Science - Regressão Linear</h1>

# # <font color='blue' style='font-size: 30px;'>Bônus</font>
# <hr style='border: 2px solid blue;'>

# ## Importando nosso modelo

# In[4]:


import pickle

modelo = open('../Exercício/modelo_preco_imoveis','rb')
lm_new = pickle.load(modelo)
modelo.close()

area = 85
garagem = 3
banheiros = 4
lareira = 3
marmore = 1
andares = 1

entrada = [[area, garagem, banheiros, lareira, marmore, andares]]

print('$ {0:.2f}'.format(lm_new.predict(entrada)[0]))


# ## Exemplo de um simulador interativo para Jupyter
# 
# https://ipywidgets.readthedocs.io/en/stable/index.html
# 
# https://github.com/jupyter-widgets/ipywidgets

# In[5]:


# Importando bibliotecas
from ipywidgets import widgets, HBox, VBox
from IPython.display import display

# Criando as entradas do formulário
area = widgets.Text(description = "Área")
garagem = widgets.Text(description = "Garagem")
banheiros = widgets.Text(description = "Banheiros")
lareira = widgets.Text(description = "Lareira")
marmore = widgets.Text(description = "Mármore?")
andares = widgets.Text(description = "Andares?")

#criando o botão
botao = widgets.Button(description = "Simular")

# Posicionando os controles no display
esquerda = VBox([area, banheiros, marmore])
direita = VBox([garagem, lareira, andares])
entradas = HBox([esquerda, direita])

# Função de simulação
def simulador(sender):
    entrada=[[
                float(area.value if area.value else 0), 
                float(garagem.value if garagem.value else 0), 
                float(banheiros.value if banheiros.value else 0), 
                float(lareira.value if lareira.value else 0), 
                float(marmore.value if marmore.value else 0), 
                float(andares.value if andares.value else 0)
             ]]
    print('$ {0:.2f}'.format(lm_new.predict(entrada)[0]))
    
# Atribuindo a função "simulador" ao evento click do botão
botao.on_click(simulador)    


# In[6]:


# mostrando o botão criado e as entradas
display(entradas, botao)

