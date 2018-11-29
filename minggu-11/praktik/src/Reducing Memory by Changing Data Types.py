#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


# In[2]:


college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
col2.head()


# In[3]:


col2.dtypes


# In[4]:


original_mem = col2.memory_usage(deep=True)
original_mem


# In[5]:


col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)


# In[6]:


col2.dtypes


# In[7]:


col2.select_dtypes(include=['object']).nunique()


# In[8]:


col2['STABBR'] = col2['STABBR'].astype('category')
col2.dtypes


# In[9]:


new_mem = col2.memory_usage(deep=True)
new_mem


# In[10]:


new_mem / original_mem


# In[11]:


college = pd.read_csv('data/college.csv')


# In[12]:


college[['CURROPER', 'INSTNM']].memory_usage(deep=True)


# In[13]:


college.loc[0, 'CURROPER'] = 10000000
college.loc[0, 'INSTNM'] = college.loc[0, 'INSTNM'] + 'a'
# college.loc[1, 'INSTNM'] = college.loc[1, 'INSTNM'] + 'a'
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)


# In[14]:


college['MENONLY'].dtype


# In[15]:


college['MENONLY'].astype('int8') # ValueError: Cannot convert non-finite values (NA or inf) to integer


# In[16]:


college.describe(include=['int64', 'float64']).T


# In[17]:


college.describe(include=[np.int64, np.float64]).T


# In[18]:


college['RELAFFIL'] = college['RELAFFIL'].astype(np.int8)


# In[19]:


college.describe(include=['int', 'float']).T  # defaults to 64 bit int/floats


# In[20]:


college.describe(include=['number']).T  # also works as the default int/float are 64 bits


# In[21]:


college['MENONLY'] = college['MENONLY'].astype('float16')
college['RELAFFIL'] = college['RELAFFIL'].astype('int8')


# In[22]:


college.index = pd.Int64Index(college.index)
college.index.memory_usage()


# In[ ]:




