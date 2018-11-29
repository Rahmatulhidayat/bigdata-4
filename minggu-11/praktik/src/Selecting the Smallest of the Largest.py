#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


# In[2]:


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
movie2.head()


# In[3]:


movie2.nlargest(100, 'imdb_score').head()


# In[4]:


movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')


# In[ ]:




