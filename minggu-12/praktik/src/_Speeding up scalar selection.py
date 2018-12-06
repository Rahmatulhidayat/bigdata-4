#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
college.loc[cn, 'UGDS_WHITE']


# In[3]:


college.at[cn, 'UGDS_WHITE']


# In[4]:


get_ipython().run_line_magic('timeit', "college.loc[cn, 'UGDS_WHITE']")


# In[5]:


get_ipython().run_line_magic('timeit', "college.at[cn, 'UGDS_WHITE']")


# In[6]:


row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')


# In[7]:


row_num, col_num


# In[8]:


get_ipython().run_line_magic('timeit', 'college.iloc[row_num, col_num]')


# In[9]:


get_ipython().run_line_magic('timeit', 'college.iat[row_num, col_num]')


# In[10]:


get_ipython().run_line_magic('timeit', 'college.iloc[5, col_num]')


# In[11]:


get_ipython().run_line_magic('timeit', 'college.iat[5, col_num]')


# In[12]:


state = college['STABBR']


# In[13]:


state.iat[1000]


# In[14]:


state.at['Stanford University']


# In[ ]:




