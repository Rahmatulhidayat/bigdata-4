#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


flights = pd.read_csv('data/flights.csv')
flights.head()


# In[3]:


fp = flights.pivot_table(index='AIRLINE', 
                         columns='ORG_AIR', 
                         values='CANCELLED', 
                         aggfunc='sum',
                         fill_value=0).round(2)
fp.head()


# In[4]:


fg = flights.groupby(['AIRLINE', 'ORG_AIR'])['CANCELLED'].sum()
fg.head()


# In[5]:


fg_unstack = fg.unstack('ORG_AIR', fill_value=0)
fg_unstack.head()


# In[6]:


fp.equals(fg_unstack)


# In[7]:


fp2 = flights.pivot_table(index=['AIRLINE', 'MONTH'],
                          columns=['ORG_AIR', 'CANCELLED'],
                          values=['DEP_DELAY', 'DIST'],
                          aggfunc=[np.mean, np.sum],
                          fill_value=0)
fp2.head()


# In[8]:


flights.groupby(['AIRLINE', 'MONTH', 'ORG_AIR', 'CANCELLED'])['DEP_DELAY', 'DIST']        .agg(['mean', 'sum'])        .unstack(['ORG_AIR', 'CANCELLED'], fill_value=0)        .swaplevel(0, 1, axis='columns')        .head()


# In[ ]:




