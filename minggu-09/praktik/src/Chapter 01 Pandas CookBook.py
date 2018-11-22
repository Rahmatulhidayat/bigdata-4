#!/usr/bin/env python
# coding: utf-8

# # Chapter 1: Pandas Foundations
# 
# ## Recipes
# * [Dissecting the anatomy of a DataFrame](#Dissecting-the-anatomy-of-a-DataFrame)
# * [Accessing the main DataFrame components](#Accessing-the-main-DataFrame-components)
# * [Understanding data types](#Understanding-data-types)
# * [Selecting a single column of data as a Series](#Selecting-a-single-column-of-data-as-a-Series)
# * [Calling Series methods](#Calling-Series-methods)
# * [Working with operators on a Series](#Working-with-operators-on-a-Series)
# * [Chaining Series methods together](#Chaining-Series-methods-together)
# * [Making the index meaningful](#Making-the-index-meaningful)
# * [Renaming row and column names](#Renaming-row-and-column-names)
# * [Creating and deleting columns](#Creating-and-deleting-columns)

# In[1]:


import pandas as pd
import numpy as np


# # Dissecting the anatomy of a DataFrame

# #### Change options to get specific output for book

# In[2]:


pd.set_option('max_columns', 8, 'max_rows', 10)


# In[3]:


movie = pd.read_csv('data/movie.csv')
movie.head()


# ![dataframe anatomy](./images/ch01_dataframe_anatomy.png)

# # Accessing the main DataFrame components

# In[4]:


columns = movie.columns
index = movie.index
data = movie.values


# In[5]:


columns


# In[6]:


index


# In[7]:


data


# In[8]:


type(index)


# In[9]:


type(columns)


# In[10]:


type(data)


# In[11]:


issubclass(pd.RangeIndex, pd.Index)


# ## There's more

# In[12]:


index.values


# In[13]:


columns.values


# # Understanding data types

# In[14]:


movie = pd.read_csv('data/movie.csv')


# In[15]:


movie.dtypes


# In[16]:


movie.get_dtype_counts()


# # Selecting a single column of data as a Series

# In[17]:


movie = pd.read_csv('data/movie.csv')


# In[18]:


movie['director_name']


# In[19]:


movie.director_name


# In[20]:


type(movie['director_name'])


# ## There's more

# In[21]:


director = movie['director_name'] # save Series to variable
director.name


# In[22]:


director.to_frame().head()


# # Calling Series methods

# ## Getting ready...

# In[23]:


s_attr_methods = set(dir(pd.Series))
len(s_attr_methods)


# In[24]:


df_attr_methods = set(dir(pd.DataFrame))
len(df_attr_methods)


# In[25]:


len(s_attr_methods & df_attr_methods)


# ## How to do it...

# In[26]:


movie = pd.read_csv('data/movie.csv')
director = movie['director_name']
actor_1_fb_likes = movie['actor_1_facebook_likes']


# In[27]:


director.head()


# In[28]:


actor_1_fb_likes.head()


# In[29]:


pd.set_option('max_rows', 8)
director.value_counts()


# In[30]:


actor_1_fb_likes.value_counts()


# In[31]:


director.size


# In[32]:


director.shape


# In[33]:


len(director)


# In[34]:


director.count()


# In[35]:


actor_1_fb_likes.count()


# In[36]:


actor_1_fb_likes.quantile()


# In[37]:


actor_1_fb_likes.min(), actor_1_fb_likes.max(), actor_1_fb_likes.mean(), actor_1_fb_likes.median(), actor_1_fb_likes.std(), actor_1_fb_likes.sum()


# In[38]:


actor_1_fb_likes.describe()


# In[39]:


director.describe()


# In[40]:


actor_1_fb_likes.quantile(.2)


# In[41]:


actor_1_fb_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9])


# In[42]:


director.isnull()


# In[43]:


actor_1_fb_likes_filled = actor_1_fb_likes.fillna(0)
actor_1_fb_likes_filled.count()


# In[44]:


actor_1_fb_likes_dropped = actor_1_fb_likes.dropna()
actor_1_fb_likes_dropped.size


# ## There's more...

# In[45]:


director.value_counts(normalize=True)


# In[46]:


director.hasnans


# In[47]:


director.notnull()


# # Working with operators on a Series

# In[48]:


pd.options.display.max_rows = 6


# In[49]:


5 + 9    # plus operator example. Adds 5 and 9


# In[50]:


4 ** 2   # exponentiation operator. Raises 4 to the second power


# In[51]:


a = 10   # assignment operator.


# In[52]:


5 <= 9   # less than or equal to operator


# In[53]:


'abcde' + 'fg'    # plus operator for strings. C


# In[54]:


not (5 <= 9)      # not is an operator that is a reserved keyword and reverse a boolean


# In[55]:


7 in [1, 2, 6]    # in operator checks for membership of a list


# In[56]:


set([1,2,3]) & set([2,3,4])


# In[57]:


[1, 2, 3] - 3


# In[58]:


a = set([1,2,3])     
a[0]                 # the indexing operator does not work with sets


# ## Getting ready...

# In[59]:


movie = pd.read_csv('data/movie.csv')
imdb_score = movie['imdb_score']
imdb_score


# In[60]:


imdb_score + 1


# In[61]:


imdb_score * 2.5


# In[62]:


imdb_score // 7


# In[63]:


imdb_score > 7


# In[64]:


director = movie['director_name']


# In[65]:


director == 'James Cameron'


# ## There's more...

# In[66]:


imdb_score.add(1)              # imdb_score + 1


# In[67]:


imdb_score.mul(2.5)            # imdb_score * 2.5


# In[68]:


imdb_score.floordiv(7)         # imdb_score // 7


# In[69]:


imdb_score.gt(7)               # imdb_score > 7


# In[70]:


director.eq('James Cameron')   # director == 'James Cameron'


# In[71]:


imdb_score.astype(int).mod(5)


# In[72]:


a = type(1)


# In[73]:


type(a)


# In[74]:


a = type(imdb_score)


# In[75]:


a([1,2,3])


# # Chaining Series methods together

# In[76]:


movie = pd.read_csv('data/movie.csv')
actor_1_fb_likes = movie['actor_1_facebook_likes']
director = movie['director_name']


# In[77]:


director.value_counts().head(3)


# In[78]:


actor_1_fb_likes.isnull().sum()


# In[79]:


actor_1_fb_likes.dtype


# In[80]:


actor_1_fb_likes.fillna(0)                .astype(int)                .head()


# ## There's more...

# In[81]:


actor_1_fb_likes.isnull().mean()


# In[82]:


(actor_1_fb_likes.fillna(0)
                 .astype(int)
                 .head())


# # Making the index meaningful

# In[83]:


movie = pd.read_csv('data/movie.csv')


# In[84]:


movie.shape


# In[85]:


movie2 = movie.set_index('movie_title')
movie2


# In[86]:


pd.read_csv('data/movie.csv', index_col='movie_title')


# # There's more...

# In[87]:


movie2.reset_index()


# # Renaming row and column names

# In[88]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')


# In[89]:


idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'} 
col_rename = {'director_name':'Director Name', 
              'num_critic_for_reviews': 'Critical Reviews'} 


# In[90]:


movie.rename(index=idx_rename, 
             columns=col_rename).head()


# # There's more

# In[91]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
index = movie.index
columns = movie.columns

index_list = index.tolist()
column_list = columns.tolist()

index_list[0] = 'Ratava'
index_list[2] = 'Ertceps'
column_list[1] = 'Director Name'
column_list[2] = 'Critical Reviews'


# In[92]:


print(index_list[:5])


# In[93]:


print(column_list)


# In[94]:


movie.index = index_list
movie.columns = column_list


# In[95]:


movie.head()


# # Creating and deleting columns

# In[96]:


movie = pd.read_csv('data/movie.csv')


# In[97]:


movie['has_seen'] = 0


# In[98]:


movie.columns


# In[99]:


movie['actor_director_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                              movie['actor_2_facebook_likes'] + 
                                              movie['actor_3_facebook_likes'] + 
                                              movie['director_facebook_likes'])


# In[100]:


movie['actor_director_facebook_likes'].isnull().sum()


# In[101]:


movie['actor_director_facebook_likes'] = movie['actor_director_facebook_likes'].fillna(0)


# In[102]:


movie['is_cast_likes_more'] = (movie['cast_total_facebook_likes'] >= 
                                  movie['actor_director_facebook_likes'])


# In[103]:


movie['is_cast_likes_more'].all()


# In[104]:


movie = movie.drop('actor_director_facebook_likes', axis='columns')


# In[105]:


movie['actor_total_facebook_likes'] = (movie['actor_1_facebook_likes'] + 
                                       movie['actor_2_facebook_likes'] + 
                                       movie['actor_3_facebook_likes'])

movie['actor_total_facebook_likes'] = movie['actor_total_facebook_likes'].fillna(0)


# In[106]:


movie['is_cast_likes_more'] = movie['cast_total_facebook_likes'] >=                                   movie['actor_total_facebook_likes']
    
movie['is_cast_likes_more'].all()


# In[107]:


movie['pct_actor_cast_like'] = (movie['actor_total_facebook_likes'] / 
                                movie['cast_total_facebook_likes'])


# In[108]:


movie['pct_actor_cast_like'].min(), movie['pct_actor_cast_like'].max() 


# In[109]:


movie.set_index('movie_title')['pct_actor_cast_like'].head()


# ## There's more...

# In[110]:


profit_index = movie.columns.get_loc('gross') + 1
profit_index


# In[111]:


movie.insert(loc=profit_index,
                 column='profit',
                 value=movie['gross'] - movie['budget'])


# In[112]:


movie.head()


# In[ ]:




