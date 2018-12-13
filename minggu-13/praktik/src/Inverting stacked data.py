#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college = pd.read_csv('data/college.csv', 
                          index_col='INSTNM', 
                          usecols=usecol_func)
college.head()


# In[3]:


college_stacked = college.stack()
college_stacked.head(18)


# In[4]:


college_stacked.unstack().head()


# In[5]:


college2 = pd.read_csv('data/college.csv', 
                      usecols=usecol_func)
college2.head()


# In[6]:


college_melted = college2.melt(id_vars='INSTNM', 
                               var_name='Race',
                               value_name='Percentage')
college_melted.head()


# In[7]:


melted_inv = college_melted.pivot(index='INSTNM',
                                  columns='Race',
                                  values='Percentage')
melted_inv.head()


# In[8]:


college2_replication = melted_inv.loc[college2['INSTNM'], 
                                      college2.columns[1:]]\
                                         .reset_index()
college2.equals(college2_replication)


# In[9]:


college.stack().unstack(0)


# In[10]:


college.T


# In[ ]:




