#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


pd.set_option('max_columns', 8, 'max_rows', 10)


# In[3]:


movie = pd.read_csv('bigdata/pandas-cookbook/data/movie.csv')
movie.head()


# In[ ]:




