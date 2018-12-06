#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college.iloc[:3, :4]


# In[3]:


college.loc[:'Amridge University', :'MENONLY']


# In[4]:


college.iloc[:, [4,6]].head()


# In[5]:


college.loc[:, ['WOMENONLY', 'SATVRMID']]


# In[6]:


college.iloc[[100, 200], [7, 15]]


# In[7]:


rows = ['GateWay Community College', 'American Baptist Seminary of the West']
columns = ['SATMTMID', 'UGDS_NHPI']
college.loc[rows, columns]


# In[8]:


college.iloc[5, -4]


# In[9]:


college.loc['The University of Alabama', 'PCTFLOAN']


# In[10]:


college.iloc[90:80:-2, 5]


# In[11]:


start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
college.loc[start:stop:-2, 'RELAFFIL']


# In[ ]:




