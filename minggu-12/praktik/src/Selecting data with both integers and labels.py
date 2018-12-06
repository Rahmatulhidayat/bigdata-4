#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')


# In[3]:


col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
col_start, col_end


# In[4]:


college.iloc[:5, col_start:col_end]


# In[5]:


row_start = college.index[10]
row_end = college.index[15]
college.loc[row_start:row_end, 'UGDS_WHITE':'UGDS_UNKN']


# In[ ]:




