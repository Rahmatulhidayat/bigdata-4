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
movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
movie_smallest_largest


# In[3]:


movie2.sort_values('imdb_score', ascending=False).head(100).head()


# In[4]:


movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget').head()


# In[5]:


movie2.nlargest(100, 'imdb_score').tail()


# In[6]:


movie2.sort_values('imdb_score', ascending=False).head(100).tail()


# In[ ]:




