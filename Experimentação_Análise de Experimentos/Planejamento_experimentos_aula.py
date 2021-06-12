#!/usr/bin/env python
# coding: utf-8

# <h1 style='color: blue; font-size: 34px; font-weight: bold;'> Planejamento de Experimentos 
# </h1>
# 

# # <font color='red' style='font-size: 30px;'>1.0 Introdução   </font>
# <hr style='border: 2px solid red;'>
# 
# 
# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>    
# <i> “Chamar um especialista em estatística depois que o experimento foi feito pode ser o mesmo que pedir para ele fazer um exame post-mortem. Talvez ele consiga dizer do que foi que o experimento morreu.”  </i>     
# </p>    
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: right; text-indent: 0px;'>    
#     <b>Sir Ronald Fisher</b>  
# 
# <hr>
# 
# 
# 
# 
# 

# # <font color='red' style='font-size: 30px;'> Introdução à análise de experimentos   </font>
# <hr style='border: 2px solid red;'>

# # <font color = 'purple'> Inserindo o experimento num Data Frame </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# ## Importando as bibliotecas 

# ### Pandas
# 
# https://pandas.pydata.org/

# In[10]:


import pandas as pd


# ### Numpy
# 
# http://www.numpy.org/

# In[11]:


import numpy as np


# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
#     <font color="red"> <b>Ensaios realizados na forma normalizada</b> 
# 
# 
# <img width='800px' src='figuras/Figura_2.png'>
# 
#  
#    
#    
#     

# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
# <font color="MidnightBlue"> Construindo uma matriz representando todos os ensaios realizados:
# 

# In[12]:


# criando a matriz normalizada
ensaios = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]])
ensaios


# ### pyDOE2
# 
# https://pypi.org/project/pyDOE2/

# In[14]:


from scipy import misc


# In[16]:


# instalando a biblioteca pyDOE2
get_ipython().system('pip install pyDOE2')


# In[17]:


import pyDOE2 as doe


# ## Costruindo um planejamento fatorial de 2²
# 

# In[18]:


# criando a matriz normalizada através da biblioteca pyDOE2
ensaios = doe.ff2n(2)      # Two-level full factorial design


# In[19]:


ensaios


# ## Incerindo o planejamento em um Data Frame

# In[20]:


experimento = pd.DataFrame(ensaios, columns = ['Farinha', 'Chocolate'])


# In[21]:


experimento


# ### Inserindo coluna com os resultados 

# In[22]:


experimento['Porcoes'] = [19, 37, 24, 49]


# In[23]:


experimento


# <hr>
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
#     <font color="MidnightBlue"> <b>Conclusão:</b> Temos, por fim, nosso experimento representado por um <i>DataFrame</i> do Pandas. Usaremos este <i>DataFrame</i> para iniciarmos a análise do nosso experimento. 
#     
# <hr>   

# # <font color = 'purple'> Analisando graficamente o experimento   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# ###  Importando o Seaborn
# 
# https://seaborn.pydata.org

# In[24]:


import seaborn as sns


# In[25]:


# paletas -> Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
sns.set_palette('terrain')

# estilo -> white, dark, whitegrid, darkgrid, ticks
sns.set_style('darkgrid')


# ### Para a farinha

# In[31]:


# gráfico da Farinha x Porções
ax1 = sns.lmplot(data = experimento, x = 'Farinha', y = 'Porcoes', ci = None, hue = 'Chocolate')
ax1.set(xticks = (-1, 1))


# ### Para o chocolate

# In[32]:


# gráfico da Chocolate x Porções
ax1 = sns.lmplot(data = experimento, x = 'Chocolate', y = 'Porcoes', ci = None, hue = 'Farinha')
ax1.set(xticks = (-1, 1))


# # <font color = 'purple'> Ajustando o modelo estatístico </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# <hr>
# 
# <img width='800px' src='figuras/Figura_3.png'>
# 
# <p style='margin: 30px 30px;'> 
# 
# <hr>
# 

# ### Bibliotecas  Stats Model
# 

# In[35]:


import statsmodels.api as sm

import statsmodels.formula.api as smf


# In[36]:


# método OLS, P = B0 = B1*Farinha + B2*Chocolate + B3*Farinha*Chocolate
modelo = smf.ols(data = experimento, formula = 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate')


# In[37]:


# ajustando o modelo
modelo_ajustado = modelo.fit() 


# In[38]:


print(modelo_ajustado.summary())


# # <font color = 'purple'> Aumentando os Graus de liberdade  </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 
# 
# 
# <p style='margin: 30px 30px;'>     
#     
# 

# <hr>
# 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
#     <font color="red"> <b>Replicatas no centro</b>
# 
# 
# <img width='800px' src='figuras/Figura_5.png'> 
# 
# 
# <p style='margin: 30px 30px;'> 
#     
#     
#  
#     
# 
#     
# <hr>    

# In[41]:


# 4 ensaios no centro da área de experimentação
centro = np.array([[0, 0, 29], [0, 0, 30], [0, 0, 29], [0, 0, 30]])
centro


# In[42]:


centro_dataframe = pd.DataFrame(centro, columns = ['Farinha', 'Chocolate', 'Porcoes'], index = [4, 5, 6, 7])


# In[43]:


centro_dataframe


# ### .

# In[44]:


experimento = experimento.append(centro_dataframe)


# In[45]:


experimento


# # <font color = 'purple'>  Análise de significância estatística   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# In[47]:


modelo = smf.ols(data = experimento, formula = 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate')


# In[48]:


modelo_ajustado = modelo.fit()


# In[49]:


print(modelo_ajustado.summary())


# <p style='margin: 200px 200px;'>    
# 
# 
# <hr>
# 
# 
#     
#  <img width='400px' src='figuras/Figura_6.png'> 
# 
# 
# <p style='margin: 30px 30px;'>    
# 
# <hr>
# 
# 
#  <img width='600px' src='figuras/Figura_7.png'> 
# 
# 
# <p style='margin: 30px 30px;'>        
#     
#     
#  <hr>   
#     
# 
#   
#  <img width='600px' src='figuras/Figura_10.png'> 
# 
# 
# <p style='margin: 30px 30px;'>       
#   
# <hr>        

# 
# # <font color = 'purple'> Teste de significância estatística usando o <b>t<b>    </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 
# 
# 
# 

# <hr>
# <img width='600px' src='figuras/Figura_11.png'> 
# 
# 
# <hr>
#   <p style='margin: 30px 30px;'>     
# <img width='900px' src='figuras/Figura_8.png'> 
# 
# 
# <hr>
# 
# 

# <p style='margin: 150px 150px;'>     
# <img width='1000px' src='figuras/Figura_20.png'
# 
# 
# 
# <hr>
# <p style='margin: 150px 150px;'>    

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### .

# In[ ]:





# ### .
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Plotando o gráfico 

# In[ ]:





# # <font color = 'purple'> Propondo um novo modelo   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 

# <hr>
# 
# <img width='800px' src='figuras/Figura_3.png'>
# 
# <p style='margin: 30px 30px;'> 
# 
# <hr>

# <p style='margin: 200px 200px;'>
# 
# 
# <hr>
# 
# <img width='600px' src='figuras/Figura_9.png'> 
# 
# <p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
# 
# 
# <p style='margin: 30px 30px;'>
# 
#     
# <hr>    
# 

# In[ ]:





# In[ ]:





# In[ ]:





# <hr>

# # <font color = 'purple'> Gráfico Padronizado de Pareto do novo modelo    </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### .

# In[ ]:





# In[ ]:





# In[ ]:





# ### Plotando o gráfico

# In[ ]:





# <font color='red' style='font-size: 30px;'> Preditos por observados  </font>
# <hr style='border: 2px solid red;'>

# In[ ]:





# In[ ]:





# ### .

# In[ ]:





# In[ ]:





# ### .

# In[ ]:





# In[ ]:






# <hr>

# In[ ]:





# ### .

# # <font color = 'purple'> Explorando o modelo   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# In[ ]:





# In[ ]:





# ### .

# ### Definindo a função

# In[ ]:





# In[ ]:





# 
# <p style='margin: 150px 150px;'>
# 
# 
# <hr>
# 
# <img width='700px' src='figuras/Figura_22.png'> 
# 
# 
# <hr>

# # <font color = 'purple'> Mapa de cores   </font>
# 
# 
# <p style='margin: 30px 30px;'>
#     
# <hr style = 'border: 1px solid purple;'>

# 
# <p style='margin: 150px 150px;'>
# 
# 
# <hr>
# 
# <img width='700px' src='figuras/Figura_23.jpg'> 
# 
# #### Fonte: National Centers for Environmental Prediction
# 
# 
# <hr>
# 
# 
# 
# <p style='margin: 50px 50px;'>
# 

# 
# 
# <p style='margin: 150px 150px;'>
# 
# 
# <hr>
# 
# <img width='600px' src='figuras/Figura_24.png'> 
# 
# 
# <hr>
# 
# 
# 
# <p style='margin: 30px 30px;'>

# In[ ]:





# In[ ]:





# ### . 

# In[ ]:





# In[ ]:





# ### .

# ### Construindo a superfície de resposta

# In[ ]:





# https://matplotlib.org/users/colormaps.html

# In[ ]:





# In[ ]:




