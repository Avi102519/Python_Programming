#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #importing Pandas


# In[2]:


pd.__version__


# In[3]:


s = pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/Sample - Superstore_Orders.csv')


# In[4]:


s


# In[5]:


id(s) #returns the memory allocation for the dataset


# In[6]:


len(s)  #Length(rows) if a dataset


# In[7]:


s.shape #Provides total rows and columns in the dataset 


# In[8]:


s.columns #returns the column headers


# In[9]:


len(s.columns)  #returns the no.of columns


# In[10]:


s.isnull() #Returns the null/missing values in the dataset


# In[11]:


s.isnull().sum() # columnwise sum of the null/missing values in the dataset


# In[12]:


s[:]


# In[13]:


s[0:10]


# In[14]:


s[0:20:5]


# In[15]:


s.head() #bydefault head returns top 5 rows


# In[16]:


s.head(2) #head function can be hyper-parameterized by value in head function paranthesis


# In[17]:


s.tail() #Returns the bottom 5 rows by default


# In[18]:


s.tail(3) #Hyper parameterization in tail function


# In[19]:


# Data set is a combination of Numerical and Categorical data


# In[20]:


s.isna() # same as isnull() returns the null values in dataset


# In[22]:


#Statistical data
s.describe() #returns the descriptive statistics for the Numerical data in dataset


# In[ ]:




