#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


state_fruit2 = pd.read_csv('data/state_fruit2.csv')
state_fruit2


# In[3]:


state_fruit2.melt(id_vars=['State'],
                 value_vars=['Apple', 'Orange', 'Banana'])


# In[4]:


state_fruit2.index=list('abc')
state_fruit2.index.name = 'letter'


# In[5]:


state_fruit2


# In[6]:


state_fruit2.melt(id_vars=['State'],
                 value_vars=['Apple', 'Orange', 'Banana'],
                 var_name='Fruit',
                 value_name='Weight')


# In[7]:


state_fruit2.melt()


# In[8]:


state_fruit2.melt(id_vars='State')


# In[ ]:




