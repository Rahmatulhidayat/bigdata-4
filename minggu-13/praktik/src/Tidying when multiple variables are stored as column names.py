#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


weightlifting = pd.read_csv('data/weightlifting_men.csv')
weightlifting


# In[3]:


wl_melt = weightlifting.melt(id_vars='Weight Category', 
                             var_name='sex_age', 
                             value_name='Qual Total')
wl_melt.head()


# In[4]:


sex_age = wl_melt['sex_age'].str.split(expand=True)
sex_age.head()


# In[5]:


sex_age.columns = ['Sex', 'Age Group']
sex_age.head()


# In[6]:


sex_age['Sex'] = sex_age['Sex'].str[0]
sex_age.head()


# In[7]:


wl_cat_total = wl_melt[['Weight Category', 'Qual Total']]
wl_tidy = pd.concat([sex_age, wl_cat_total], axis='columns')
wl_tidy.head()


# In[8]:


cols = ['Weight Category', 'Qual Total']
sex_age[cols] = wl_melt[cols]


# In[9]:


age_group = wl_melt.sex_age.str.extract('(\d{2}[-+](?:\d{2})?)', expand=False)
sex = wl_melt.sex_age.str[0]
new_cols = {'Sex':sex, 
            'Age Group': age_group}


# In[10]:


wl_tidy2 = wl_melt.assign(**new_cols).drop('sex_age', axis='columns')
wl_tidy2.head()


# In[11]:


wl_tidy2.sort_index(axis=1).equals(wl_tidy.sort_index(axis=1))


# In[ ]:




