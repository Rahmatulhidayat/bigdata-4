#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
city.head()


# In[3]:


city.iloc[3]


# In[4]:


city.iloc[[10,20,30]]


# In[5]:


city.iloc[4:50:10]


# In[6]:


city.loc['Heritage Christian University']


# In[7]:


np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
labels


# In[8]:


city.loc[labels]


# In[9]:


city.loc['Alabama State University':'Reid State Technical College':10]


# In[10]:


city['Alabama State University':'Reid State Technical College':10]


# In[11]:


city.iloc[[3]]


# In[12]:


city.loc['Reid State Technical College':'Alabama State University':10]


# In[13]:


city.loc['Reid State Technical College':'Alabama State University':-10]


# In[ ]:




