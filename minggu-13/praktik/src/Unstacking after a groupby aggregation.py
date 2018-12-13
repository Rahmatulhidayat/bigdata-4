#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


employee = pd.read_csv('data/employee.csv')


# In[3]:


employee.groupby('RACE')['BASE_SALARY'].mean().astype(int)


# In[4]:


agg = employee.groupby(['RACE', 'GENDER'])['BASE_SALARY'].mean().astype(int)
agg


# In[5]:


agg.unstack('GENDER')


# In[6]:


agg.unstack('RACE')


# In[7]:


agg2 = employee.groupby(['RACE', 'GENDER'])['BASE_SALARY'].agg(['mean', 'max', 'min']).astype(int)
agg2


# In[ ]:




