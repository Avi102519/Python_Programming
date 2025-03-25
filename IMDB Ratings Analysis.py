#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd #Importing Pandas library


# In[4]:


ratings = pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/archive/rating.csv') #reading the ratings csv file


# In[5]:


ratings.shape


# In[6]:


print(type(ratings)) #printing the type of ratings dataset


# In[7]:


ratings.head(20) #Getting the top 20 rows


# In[89]:


tags = pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/archive/tag.csv')#reading the tag excel
tags.head()


# In[9]:


movies = pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/archive/movie.csv')


# In[10]:


ratings.columns


# In[11]:


tags.columns


# In[12]:


movies.columns


# In[13]:


del ratings['timestamp']


# In[14]:


del tags['timestamp']


# In[15]:


tags.head()


# In[16]:


row_0 = tags.iloc[1] #locking the first index


# In[17]:


print(row_0) #Printing the locked index


# In[18]:


row_0.index


# In[19]:


'rating' in row_0 # to check the 'rating' column availability


# In[20]:


'userId' in row_0


# In[21]:


hi = tags.iloc[4]
hi


# In[22]:


hi.name #name returns the index id


# In[23]:


row_0.name #name returns the index id


# In[24]:


row_0 = row_0.rename('firstRow') #Renamed the index value in the iloc
row_0.name


# In[25]:


row_0


# In[26]:


hi = hi.rename('4thRow') #Rename validity limited for this iloc
hi


# In[27]:


tags.head(10)


# # DataFrames

# In[28]:


tags.head()


# In[29]:


tags.index #Returns the index starting and stopping values and step


# In[30]:


tags.columns #Returns the column heading


# In[31]:


tags.iloc[[0,11,500]] #getting the index valuses 0,11,500


# # Descriptive Statistics

# In[32]:


ratings.head()


# In[33]:


ratings['rating'].describe() #Returns the statistical values on rating column in ratings table


# In[34]:


ratings.describe() #Returns the statistical values on ratings table


# In[35]:


ratings['rating'].mean() #Returns the mean value on rating column in ratings table


# In[36]:


ratings['rating'].min() #Returns the min value on rating column in ratings table


# In[37]:


ratings['rating'].max() #Returns the max value on rating column in ratings table


# In[38]:


ratings['rating'].std() #Returns the standard deviaton value on rating column in ratings table


# In[39]:


ratings['rating'].mode() #Returns the mode value on rating column in ratings table


# In[40]:


ratings.corr() #Returns the corelation values on ratings table


# In[41]:


filter1 = ratings['rating']>10
print(filter1)
filter1.any()  #Returns False unless there is at least one element.


# In[42]:


filter2 = ratings['rating']>0
filter2.all() #Returns True unless there is at least one element within a series.


# # Data Cleaning: Handling Missing Data

# In[43]:


movies.shape


# In[44]:


movies.isnull().any().any() #No Null values


# In[45]:


ratings.shape


# In[46]:


ratings.isnull().any().any() # No Null values


# In[47]:


tags.isnull().any().any() #some null values


# In[48]:


tags = tags.dropna() #Dropped the null values


# In[49]:


tags.isnull().any().any() #no null values


# In[50]:


tags.shape


# # Data Visualization

# In[51]:


get_ipython().run_line_magic('matplotlib', 'inline')

ratings.hist(column='rating', figsize=(10,5))


# In[52]:


ratings.boxplot(column= 'rating',figsize = (10,5))


# # Slicing Out Columns

# In[53]:


tags['tag'].head()


# In[54]:


movies[['title','genres']].head()


# In[55]:


ratings[-10:]


# In[56]:


ratings.tail(10)


# In[57]:


tag_counts = tags['tag'].value_counts()
tag_counts[-10:]


# In[58]:


tag_counts[:10].plot(kind = 'bar',figsize=(10,5))


# # Filters for Selecting Rows

# In[99]:


ratings.head()


# In[59]:


is_highly_rated = ratings['rating']>=5.0 #Returns the dataset with movierating>=5.0
ratings[is_highly_rated][30:50]


# In[104]:


print(is_highly_rated)


# In[60]:


is_action = movies['genres'].str.contains('Action') #Returns the action genre movies
movies[is_action][5:15]


# In[61]:


movies[is_action].head(15)


# # Group By and Aggregrate

# In[65]:


ratings_count = ratings[['movieId','rating']].groupby('rating').count()
ratings_count


# In[68]:


average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()


# In[108]:


group = ratings.groupby('movieId').mean()
group.head()


# In[69]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.tail()


# # 🔰 Merge Dataframes¶

# In[70]:


tags.head()


# In[71]:


movies.head()


# In[72]:


t = movies.merge(tags,on='movieId',how= 'inner') #Inner Joining 'Movies' and 'tags' data frames on 'movieid'.
t.head()


# # 📚 Combine aggreagation, merging, and filters to get useful analytics¶

# In[73]:


avg_ratings = ratings.groupby('movieId',as_index=False).mean()
del avg_ratings['userId']
avg_ratings.head()


# In[74]:


box_office = movies.merge(avg_ratings, on='movieId',how='inner')
box_office.tail()


# In[75]:


is_highly_rated = box_office['rating']>=4.0
box_office[is_highly_rated][-5:]


# In[78]:


is_Adventure = box_office['genres'].str.contains('Adventure')
box_office[is_Adventure][:5]


# In[79]:


box_office[is_Adventure & is_highly_rated][-5:]


# # 📝 Vectorized String Operations¶

# In[80]:


movies.head()


# # 🔬 Split 'genres' into multiple columns¶

# In[81]:


movie_genres = movies['genres'].str.split('|',expand=True)


# In[82]:


movie_genres[:10]


# # 🚩 Add a new column for comedy genre flag¶

# In[83]:


movie_genres['IsComedy'] = movies['genres'].str.contains('Comedy')


# In[85]:


movie_genres[:10]


# # 📟 Extract year from title e.g. (2007)¶

# In[109]:


movies.head()


# In[86]:


movies['year'] = movies['title'].str.extract('.*\((.*)\).*',expand = True)


# In[87]:


movies.tail()


# # 🕐 Parsing Timestamps¶
# Timestamps are common in sensor data or other time series datasets. Let us revisit the tags.csv dataset and read the timestamps!

# In[90]:


tags = pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/archive/movie.csv',sep= ',')


# In[91]:


tags.dtypes


# In[92]:


tags.head()


# In[95]:


tags.head(2)


# # 📇 Average Movie Ratings over Time¶
# Movie ratings related to the year of launch?¶

# In[96]:


average_rating = ratings[['movieId','rating']].groupby('movieId',as_index=False).mean()
average_rating.tail()


# In[98]:


joined = movies.merge(average_rating, on='movieId', how='inner')
joined.head()
#joined.corr()


# In[ ]:




