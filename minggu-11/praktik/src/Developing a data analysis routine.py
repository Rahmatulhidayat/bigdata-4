#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


# In[2]:


college = pd.read_csv('data/college.csv')


# In[3]:


college.head()


# In[4]:


college.shape


# In[5]:


with pd.option_context('display.max_rows', 8):
    display(college.describe(include=[np.number]).T)


# In[6]:


college.describe(include=[np.object, pd.Categorical]).T


# In[7]:


college.info()


# In[8]:


college.describe(include=[np.number]).T


# In[9]:


college.describe(include=[np.object, pd.Categorical]).T


# In[10]:


with pd.option_context('display.max_rows', 5):
    display(college.describe(include=[np.number], 
                 percentiles=[.01, .05, .10, .25, .5, .75, .9, .95, .99]).T)


# In[11]:


college_dd = pd.read_csv('data/college_data_dictionary.csv')


# In[12]:


with pd.option_context('display.max_rows', 8):
    display(college_dd)


# In[ ]:




