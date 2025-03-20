#!/usr/bin/env python
# coding: utf-8

# # Matrix visualization on Data frames using Pandas
# Statistical visualizaton on data frames using Seaborn

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_csv(r"/Users/aviswe/Desktop/830/Datasets/data (1).csv")


# In[3]:


df


# In[4]:


len(df) # Returns the total number of rows in the dataset


# In[6]:


df.columns


# In[7]:


len(df.columns) #Returns the no.of columns


# In[8]:


df.head() #Returns the top 5 rows


# In[9]:


df.head(2) #Hyper parameterization in Head function


# In[10]:


df.tail() #Rrturns the bottom 5 rows


# In[11]:


df.tail(2) #Hyper parameterization in Tail function


# In[12]:


df.info() #Returns the su of columnwise data


# In[13]:


df.describe() #Returns the statistical info on Numerical columns


# In[14]:


df.columns = ['a','b','c','d','e'] #Renaming the data set columns names to a,b,c,d,e
df.head()


# In[16]:


df.columns = ['CountryName','CountryCode','BirthRate','InternetUsers','IncomeGroup'] #renaming dataset columns
df.head()


# In[17]:


df[21:26] #Python returns based on the entered index values from 21 to 25(26-1)


# In[18]:


df[:] #returns entire dataset


# In[19]:


df[:10] #Returns the rows till 9(10-1)


# In[20]:


df.head(10) # Returns the top 10 rows(indexwise)


# In[21]:


df[: : -1] #returns the dataset in reverse order (bottom to top)


# In[22]:


df[: : 20] #Returns every 20th row


# In[23]:


df['CountryName'].head() # returns the top 5 values for Country Name and its atatype


# In[24]:


['CountryName','BirthRate']


# In[26]:


df[['CountryName','BirthRate']].head()  #returns the top 5 values for Country Name&BirthRate and its datatype


# In[28]:


df['BirthRate']


# In[29]:


df[['CountryName','BirthRate']][4:8] #returns the row index from 4 to 7(8-1)


# In[30]:


df[['CountryCode','BirthRate','InternetUsers']][4:8] #Creating s subset dataframe


# In[31]:


df.BirthRate*df.InternetUsers #Mathemetical Operations on Dataset


# In[32]:


df['newrow']=df.BirthRate*df.InternetUsers #Adding a new column
df


# In[34]:


df.drop('newrow',axis=1)


# In[35]:


df


# In[36]:


df = df.drop('newrow',axis=1) #Removing a column


# In[37]:


df


# In[38]:


df.columns[2]


# In[39]:


filter = df.InternetUsers<2 #Creating s filter


# In[40]:


filter


# In[41]:


df[3:7]


# In[42]:


df[filter] # Sorting the dataset using the filter


# In[43]:


df.BirthRate>40 #Compares the BirthRate on basis of 40 and returns true or false


# In[45]:


filter2 = df.BirthRate>40


# In[46]:


filter2


# In[47]:


df[filter2]


# In[48]:


df[filter & filter2]


# In[49]:


df[(df.BirthRate > 40) & (df.InternetUsers < 2)]


# In[50]:


df[df.IncomeGroup == 'Low income'] #Returns low income group rows


# In[51]:


df.IncomeGroup.unique() #Returns the array with unique incomegroup values


# # Inroduction to Seaborn
# seaborn is ver powerful data statistical visualization package in Python

# In[53]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 8,4


# In[54]:


df.head()


# In[56]:


#Distributions:
vis1 = sns.distplot(df["InternetUsers"])


# In[57]:


#Box Plots:
vis2 = sns.boxplot(data = df,x="IncomeGroup",y='BirthRate')


# In[59]:


vis3 = sns.lmplot(data=df,x='InternetUsers',y = 'BirthRate',fit_reg = False) #lm - Linear Model


# In[61]:


vis4 = sns.lmplot(data = df,x = 'InternetUsers',y = 'BirthRate')


# In[62]:


vis5 = sns.lmplot(data = df,x= 'InternetUsers',y = 'BirthRate',fit_reg = False,hue = 'IncomeGroup')
#huehue- Parameter for color


# In[67]:


vis5 = sns.lmplot(data=df,x='InternetUsers',y= 'BirthRate',fit_reg=False,hue='IncomeGroup')


# In[ ]:




