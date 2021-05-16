#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# função para abrir o arquivo
json = open('dados/aluguel.json')
print(json.read())


# In[5]:


# pd.read_json lê um arquivo tipo .json
df_json = pd.read_json('dados/aluguel.json')
df_json


# In[6]:


# função para abrir o arquivo
txt = open('dados/aluguel.txt')
print(txt.read())


# In[7]:


# pd.read_table lê um arquivo .txt
df_txt = pd.read_table('dados/aluguel.txt')
df_txt


# In[9]:


# pd.read_excel lê um arquivo .xlsx
df_xlsx = pd.read_excel('dados/aluguel.xlsx')
df_xlsx


# In[17]:


# pd.read_html lê arquivo html
df_html = pd.read_html('dados/dados_html_1.html')
df_html   # tipo list


# In[19]:


# em forma de DataFrame
df_html[0]    # tipo DataFrame


# In[21]:


# pode passar o url como parâmetro
df_html1 = pd.read_html('file:///C:/Users/Jorda/Documents/Programa%C3%A7%C3%A3o/Data%20Science/Jordan/Curso_02_Pandas/extras/dados/dados_html_1.html')
df_html1[0] 


# In[23]:


df_html2 = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')

len(df_html2)  # 3 tabelas no link


# In[30]:


df_html2[0]


# In[31]:


df_html2[1]


# In[32]:


df_html2[2]


# In[ ]:




