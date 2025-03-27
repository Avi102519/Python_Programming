#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #importing pandas library


# In[2]:


pd.__version__


# In[3]:


rd= pd.read_excel(r'/Users/aviswe/Desktop/830/Datasets/Rawdata (1).xlsx')


# In[4]:


rd


# In[5]:


rd.isnull().sum()


# In[6]:


nd = rd.copy()


# In[7]:


nd


# In[8]:


id(nd)


# In[9]:


rd.shape #shape of the data frame


# In[10]:


rd.columns


# In[11]:


rd.info() #Information of the Dataframe


# In[12]:


rd.isnull()


# In[13]:


rd.isna()


# In[14]:


rd.isnull().sum()


# In[15]:


rd


# # Data Cleaning

# In[16]:


rd['Name'] # ^#* are regular expressions


# In[17]:


rd['Name'] = rd['Name'].str.replace(r'\W','',regex=True) #not small w use W


# In[18]:


rd['Name']


# In[19]:


rd['Domain'] = rd['Domain'].str.replace(r'\W','',regex=True)
rd['Domain']


# In[20]:


rd['Age'] = rd['Age'].str.replace(r'\W','',regex=True) #Cleaning the data
rd['Age']


# In[21]:


rd['Age'] = rd['Age'].str.extract('(\d+)') #extracting the data
rd['Age']


# In[22]:


rd['Location'] = rd['Location'].str.replace(r'\W','',regex=True)
rd['Location']


# In[24]:


rd['Salary']= rd['Salary'].str.replace(r'\W','',regex=True)
rd['Salary']


# In[25]:


rd['Exp'] = rd['Exp'].str.extract('(\d+)') 
rd['Exp']


# In[26]:


rd


# In[27]:


cd = rd.copy()


# In[28]:


cd


# # EDA Techniques

# In[29]:


cd.isnull().sum()


# In[30]:


cd['Age']


# In[31]:


import numpy as np #Importing numpy


# In[33]:


cd['Age'] = cd['Age'].fillna(np.mean(pd.to_numeric(cd['Age']))) #Filling the null values with mean strategy
cd['Age']


# In[34]:


cd['Exp'] = cd['Exp'].fillna(np.mean(pd.to_numeric(cd['Exp']))) #Filling the null values with mean strategy
cd['Exp']


# In[35]:


cd


# In[36]:


cd['Location']=cd['Location'].fillna(cd['Location'].mode()[0]) # for mode strategy apply [0]
cd['Location']


# In[37]:


cd


# In[38]:


cd.info() #Clean data information


# In[75]:


cd['Age'] = cd['Age'].astype('int') #Converting System data type to User defined Datatype


# In[74]:


cd['Exp'] = cd['Exp'].astype('int')


# In[72]:


cd['Salary'] = cd['Salary'].astype('int')


# In[46]:


cd['Name']= cd['Name'].astype('category')
cd['Domain']= cd['Domain'].astype('category')
cd['Location']= cd['Location'].astype('category')


# In[76]:


cd.info()


# In[48]:


cd.to_csv('cd.csv') #saved the clean data into local systme location


# In[49]:


import os
os.getcwd() # Saved the cleaned data file in the '/Users/aviswe' location


# # Visualizing the data using Matplotlib and Seaborn

# In[50]:


import matplotlib.pyplot as plt #importing libraies Matplotlib,seaborn
import seaborn as sns


# In[51]:


import warnings
warnings.filterwarnings('ignore')


# In[52]:


cd['Salary']


# In[53]:


vis1= sns.distplot(cd['Salary']) #Univariate Analysis


# In[54]:


vis2 = plt.hist(cd['Salary']) #univariate Analysis


# In[55]:


vis3 = sns.lmplot(data = cd,x = 'Exp',y = 'Salary') #Bivariate Analysis


# In[56]:


vis4 = sns.lmplot(data= cd,x='Exp',y = 'Salary',fit_reg=False) #Bivariate plot has no line


# In[57]:


cd[:] #Slicing the clean data


# In[58]:


cd[0:6:2] #Returns every second row in the dataframe


# In[59]:


cd.columns


# In[60]:


x_iv = cd[['Name', 'Domain', 'Age', 'Location', 'Exp']] #Extracting the independent variables


# In[61]:


x_iv #independent variable


# In[62]:


y_dv = cd[['Salary']] #extracting the dependent variable


# In[63]:


y_dv #Dependent variable


# In[64]:


rd


# In[65]:


cd


# In[66]:


x_iv


# In[67]:


y_dv


# In[68]:


cd


# In[69]:


imputation = pd.get_dummies(cd) #Converting categorical data into numerical data


# In[70]:


imputation #Imouted data frame


# In[71]:


cd #clean data frame


# # Conclusion of the project
# Raw data is having regex,Missing values and uncleaned data
# Performed the below activities using the EDA techniques
#     1.filled missing numerical and categorical data
#     2.Implimented the Outlier treatment,Univariate,Bivariate,correlation, Imputed categorical data into numerical data.
