#!/usr/bin/env python
# coding: utf-8

# # Chapter 2: Essential DataFrame Operations
# 
# ## Recipes
# * [Selecting multiple DataFrame columns](#Selecting-multiple-DataFrame-columns)
# * [Selecting columns with methods](#Selecting-columns-with-methods)
# * [Ordering column names sensibly](#Ordering-column-names-sensibly)
# * [Operating on the entire DataFrame](#Operating-on-the-entire-DataFrame)
# * [Chaining DataFrame methods together](#Chaining-DataFrame-methods-together)
# * [Working with operators on a DataFrame](#Working-with-operators-on-a-DataFrame)
# * [Comparing missing values](#Comparing-missing-values)
# * [Transposing the direction of a DataFrame operation](#Transposing-the-direction-of-a-DataFrame-operation)
# * [Determining college campus diversity](#Determining-college-campus-diversity)

# In[1]:


import pandas as pd
import numpy as np
pd.options.display.max_columns = 40


# # Selecting multiple DataFrame columns

# In[2]:


movie = pd.read_csv('data/movie.csv')
movie_actor_director = movie[['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']]
movie_actor_director.head()


# In[3]:


movie[['director_name']].head()


# In[4]:


movie['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']


# ## There's more...

# In[5]:


cols =['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']
movie_actor_director = movie[cols]


# # Selecting columns with methods

# In[6]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
movie.get_dtype_counts()


# In[7]:


movie.select_dtypes(include=['int']).head()


# In[8]:


movie.select_dtypes(include=['number']).head()


# In[9]:


movie.filter(like='facebook').head()


# In[10]:


movie.filter(regex='\d').head()


# In[11]:


movie.filter(items=['actor_1_name', 'asdf']).head()


# # Ordering column names sensibly

# In[12]:


movie = pd.read_csv('data/movie.csv')


# In[13]:


movie.head()


# In[14]:


movie.columns


# In[15]:


disc_core = ['movie_title','title_year', 'content_rating','genres']
disc_people = ['director_name','actor_1_name', 'actor_2_name','actor_3_name']
disc_other = ['color','country','language','plot_keywords','movie_imdb_link']
cont_fb = ['director_facebook_likes','actor_1_facebook_likes','actor_2_facebook_likes',
           'actor_3_facebook_likes', 'cast_total_facebook_likes', 'movie_facebook_likes']
cont_finance = ['budget','gross']
cont_num_reviews = ['num_voted_users','num_user_for_reviews', 'num_critic_for_reviews']
cont_other = ['imdb_score','duration', 'aspect_ratio', 'facenumber_in_poster']


# In[16]:


new_col_order = disc_core + disc_people + disc_other +                     cont_fb + cont_finance + cont_num_reviews + cont_other
set(movie.columns) == set(new_col_order)


# In[17]:


movie2 = movie[new_col_order]
movie2.head()


# # Operating on the entire DataFrame

# In[18]:


pd.options.display.max_rows = 8
movie = pd.read_csv('data/movie.csv')
movie.shape


# In[19]:


movie.size


# In[20]:


movie.ndim


# In[21]:


len(movie)


# In[22]:


movie.count()


# In[23]:


movie.min()


# In[24]:


movie.describe()


# In[25]:


pd.options.display.max_rows = 10


# In[26]:


movie.describe(percentiles=[.01, .3, .99])


# In[27]:


pd.options.display.max_rows = 8


# In[28]:


movie.isnull().sum()


# ## There's more...

# In[29]:


movie.min(skipna=False)


# # Chaining DataFrame methods together

# In[30]:


movie = pd.read_csv('data/movie.csv')
movie.isnull().head()


# In[31]:


movie.isnull().sum().head()


# In[32]:


movie.isnull().sum().sum()


# In[33]:


movie.isnull().any().any()


# ## How it works...

# In[34]:


movie.isnull().get_dtype_counts()


# ## There's more...

# In[35]:


movie[['color', 'movie_title', 'color']].max()


# In[36]:


movie.select_dtypes(['object']).fillna('').max()


# # Working with operators on a DataFrame

# ## Getting ready...

# In[37]:


college = pd.read_csv('data/college.csv')
college + 5


# In[38]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')


# In[39]:


college == 'asdf'


# In[40]:


college_ugds_.head()


# In[41]:


college_ugds_.head() + .00501


# In[42]:


(college_ugds_.head() + .00501) // .01


# In[43]:


college_ugds_op_round = (college_ugds_ + .00501) // .01 / 100
college_ugds_op_round.head()


# In[44]:


college_ugds_round = (college_ugds_ + .00001).round(2)
college_ugds_round.head()


# In[45]:


.045 + .005


# In[46]:


college_ugds_op_round.equals(college_ugds_round)


# ## There's more...

# In[47]:


college_ugds_op_round_methods = college_ugds_.add(.00501).floordiv(.01).div(100)


# # Comparing missing values

# In[48]:


np.nan == np.nan


# In[49]:


None == None


# In[50]:


5 > np.nan


# In[51]:


np.nan > 5


# In[52]:


5 != np.nan


# In[53]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')


# In[54]:


college_ugds_.head() == .0019


# In[55]:


college_self_compare = college_ugds_ == college_ugds_
college_self_compare.head()


# In[56]:


college_self_compare.all()


# In[57]:


(college_ugds_ == np.nan).sum()


# In[58]:


college_ugds_.isnull().sum()


# In[59]:


from pandas.testing import assert_frame_equal


# In[60]:


assert_frame_equal(college_ugds_, college_ugds_)


# ## There's more...

# In[61]:


college_ugds_.eq(.0019).head()


# # Transposing the direction of a DataFrame operation

# In[62]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()


# In[63]:


college_ugds_.count()


# In[64]:


college_ugds_.count(axis=0)


# In[65]:


college_ugds_.count(axis='index')


# In[66]:


college_ugds_.count(axis='columns').head()


# In[67]:


college_ugds_.sum(axis='columns').head()


# In[68]:


college_ugds_.median(axis='index')


# ## There's more

# In[69]:


college_ugds_cumsum = college_ugds_.cumsum(axis=1)
college_ugds_cumsum.head()


# In[70]:


college_ugds_cumsum.sort_values('UGDS_HISP', ascending=False)


# # Determining college campus diversity

# In[71]:


pd.read_csv('data/college_diversity.csv', index_col='School')


# In[72]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()


# In[73]:


college_ugds_.isnull().sum(axis=1).sort_values(ascending=False).head()


# In[74]:


college_ugds_ = college_ugds_.dropna(how='all')


# In[75]:


college_ugds_.isnull().sum()


# In[76]:


college_ugds_.ge(.15).head()


# In[77]:


diversity_metric = college_ugds_.ge(.15).sum(axis='columns')
diversity_metric.head()


# In[78]:


diversity_metric.value_counts()


# In[79]:


diversity_metric.sort_values(ascending=False).head()


# In[80]:


college_ugds_.loc[['Regency Beauty Institute-Austin', 
                          'Central Texas Beauty College-Temple']]


# In[81]:


us_news_top = ['Rutgers University-Newark', 
               'Andrews University', 
               'Stanford University', 
               'University of Houston',
               'University of Nevada-Las Vegas']


# In[82]:


diversity_metric.loc[us_news_top]


# ## There's more...

# In[83]:


college_ugds_.max(axis=1).sort_values(ascending=False).head(10)


# In[84]:


college_ugds_.loc['Talmudical Seminary Oholei Torah']


# In[85]:


(college_ugds_ > .01).all(axis=1).any()

