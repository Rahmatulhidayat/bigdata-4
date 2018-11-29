#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


# In[2]:


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'title_year', 'imdb_score']]


# In[3]:


movie2.sort_values('title_year', ascending=False).head()


# In[4]:


movie3 = movie2.sort_values(['title_year','imdb_score'], ascending=False)
movie3.head()


# In[5]:


movie_top_year = movie3.drop_duplicates(subset='title_year')
movie_top_year.head()


# In[6]:


movie4 = movie[['movie_title', 'title_year', 'content_rating', 'budget']]
movie4_sorted = movie4.sort_values(['title_year', 'content_rating', 'budget'], 
                                   ascending=[False, False, True])
movie4_sorted.drop_duplicates(subset=['title_year', 'content_rating']).head(10)


# In[ ]:




