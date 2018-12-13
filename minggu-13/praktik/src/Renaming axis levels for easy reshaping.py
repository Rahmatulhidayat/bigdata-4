#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv')


# In[3]:


cg = college.groupby(['STABBR', 'RELAFFIL'])['UGDS', 'SATMTMID']             .agg(['count', 'min', 'max']).head(6)


# In[4]:


cg


# In[5]:


cg = cg.rename_axis(['AGG_COLS', 'AGG_FUNCS'], axis='columns')
cg


# In[6]:


cg.stack('AGG_FUNCS').head()


# In[7]:


cg.stack('AGG_FUNCS').swaplevel('AGG_FUNCS', 'STABBR', axis='index').head()


# In[8]:


cg.stack('AGG_FUNCS')   .swaplevel('AGG_FUNCS', 'STABBR', axis='index')   .sort_index(level='RELAFFIL', axis='index')   .sort_index(level='AGG_COLS', axis='columns').head(6)


# In[9]:


cg.stack('AGG_FUNCS').unstack(['RELAFFIL', 'STABBR'])


# In[10]:


cg.stack(['AGG_FUNCS', 'AGG_COLS']).head(12)


# In[11]:


cg.rename_axis([None, None], axis='index').rename_axis([None, None], axis='columns')


# In[ ]:




