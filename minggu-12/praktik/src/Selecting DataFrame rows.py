#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college.head()


# In[3]:


pd.options.display.max_rows = 6


# In[4]:


college.iloc[60]


# In[5]:


college.loc['University of Alaska Anchorage']


# In[6]:


college.iloc[[60, 99, 3]]


# In[7]:


labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
college.loc[labels]


# In[8]:


college.iloc[99:102]


# In[9]:


start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
college.loc[start:stop]


# In[10]:


college.iloc[[60, 99, 3]].index.tolist()


# In[ ]:




