#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
state_fruit


# In[3]:


state_fruit.stack()


# In[4]:


state_fruit_tidy = state_fruit.stack().reset_index()
state_fruit_tidy


# In[5]:


state_fruit_tidy.columns = ['state', 'fruit', 'weight']
state_fruit_tidy


# In[6]:


state_fruit.stack()           .rename_axis(['state', 'fruit'])


# In[7]:


state_fruit.stack()           .rename_axis(['state', 'fruit'])           .reset_index(name='weight')


# In[8]:


state_fruit2 = pd.read_csv('data/state_fruit2.csv')
state_fruit2


# In[9]:


state_fruit2.stack()


# In[10]:


state_fruit2.set_index('State').stack()


# In[ ]:




