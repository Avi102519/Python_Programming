#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ds = pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/Movie-Rating.csv')
ds


# In[3]:


ds.head()


# In[4]:


ds.tail()


# In[5]:


ds.shape


# In[6]:


id(ds)


# In[7]:


ds.columns


# In[8]:


len(ds)


# In[9]:


ds.info()


# In[10]:


ds['Film'].astype('category')


# In[11]:


ds.info()


# In[12]:


ds['Film']=ds['Film'].astype('category')


# In[13]:


ds.info()


# In[14]:


ds.columns


# In[15]:


ds.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRatings','BudgetMillions','Year']


# In[16]:


ds.head(1)


# In[17]:


ds.describe()


# In[18]:


ds.info()


# In[19]:


ds['Genre'] = ds['Genre'].astype('category')
ds['Year'] = ds['Year'].astype('category')


# In[20]:


ds.info()


# In[21]:


ds.Genre


# In[22]:


ds.describe() #Statistical info for Numerical values


# In[25]:


#hot to work with joint plots
from matplotlib import pyplot as plt #Visualization
import seaborn as sns #advanced visualization
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[26]:


j = plt.jointplot(data = ds,x = 'CriticRating',y = 'AudienceRatings')


# In[27]:


j = sns.jointplot(data = ds,x='CriticRating',y = 'AudienceRatings')


# In[28]:


j = sns.jointplot(data = ds,x='CriticRating',y = 'AudienceRatings',kind= 'hex')


# In[29]:


j = sns.jointplot(data = ds,x='CriticRating',y = 'AudienceRatings',kind= 'kde') #Kernal Density


# In[30]:


j = sns.jointplot(data = ds,x='CriticRating',y = 'AudienceRatings',kind= 'scatter')
# Insight Most people like to watch AudienceRatings
#Audience ratings is dominent than critic rating


# In[31]:


m1 = sns.distplot(ds.AudienceRatings)


# In[32]:


m2 = sns.distplot(ds.CriticRating)


# In[33]:


m3 = sns.displot(ds.CriticRating)


# In[34]:


sns.set_style('darkgrid') #Background color setting


# In[35]:


m4 = sns.displot(ds.AudienceRatings,bins = 10)


# In[36]:


m5 = plt.hist(ds.AudienceRatings,bins = 15)


# In[37]:


sns.set_style('white') #normal distribution & called as bell curve
m6 = plt.hist(ds.AudienceRatings,bins = 20)


# In[38]:


n1 = plt.hist(ds.CriticRating,bins = 20) #uniform Distibution


# In[39]:


plt.hist(ds.BudgetMillions)
plt.show()


# In[40]:


plt.hist(ds[ds.Genre == 'Drama'].BudgetMillions)
plt.show()


# In[41]:


ds.head()


# In[42]:


ds.Genre.unique()


# In[43]:


#Below plots are stacked histogram because overlaped
plt.hist(ds[ds.Genre=='Action'].BudgetMillions,bins = 20)
plt.hist(ds[ds.Genre=='Thriller'].BudgetMillions,bins = 20)
plt.hist(ds[ds.Genre=='Drama'].BudgetMillions,bins = 20)
plt.legend()
plt.show()


# In[44]:


plt.hist([ds[ds.Genre=='Action'].BudgetMillions,\
         ds[ds.Genre=='Drama'].BudgetMillions,\
         ds[ds.Genre=='Thriller'].BudgetMillions,\
         ds[ds.Genre=='Comedy'].BudgetMillions],
         bins = 20,stacked =True)
plt.show()


# In[45]:


# if you have 100 categories you cannot copy & paste all the things
for gen in ds.Genre.cat.categories:
    print(gen)


# In[46]:


vis1 = sns.lmplot(data=ds,x='CriticRating',y='AudienceRatings',\
                 fit_reg=False)


# In[47]:


vis2 = sns.lmplot(data = ds,x='CriticRating',y='AudienceRatings',\
                 fit_reg = False,hue = 'Genre')


# In[48]:


vis3 = sns.lmplot(data = ds,x='CriticRating',y='AudienceRatings',\
                 fit_reg = False, hue = 'Genre',aspect =1)


# In[ ]:


# Kernal Density Estimate plot ( KDE PLOT) 
# how can i visulize audience rating & critics rating . using scatterplot


# In[50]:


get_ipython().system('pip install seaborn --upgrade')


# In[54]:


#k1 = sns.kdeplot(ds.CriticRating,ds.AudienceRatings)
k1 = sns.kdeplot(x= ds.CriticRating, y= ds.AudienceRatings)

# where do u find more density and how density is distibuted across from the the chat 
# center point is kernal this is calld KDE & insteade of dots it visualize like this
# we can able to clearly see the spread at the audience ratings


# In[56]:


k1 = sns.kdeplot(x=ds.CriticRating,y= ds.AudienceRatings,shade = True,shade_lowest=False,cmap='Reds')


# In[57]:


k2 = sns.kdeplot(x=ds.CriticRating,y=ds.AudienceRatings,shade_lowest=False,cmap='Greens_r')


# In[58]:


sns.set_style('dark')
k1 = sns.kdeplot(x=ds.BudgetMillions,y=ds.AudienceRatings,shade_lowest=False,cmap='Greens_r')


# In[59]:


pip install notebook


# In[60]:


sns.set_style('dark')
k1=sns.kdeplot(x= ds.BudgetMillions,y=ds.AudienceRatings)


# In[61]:


k2 = sns.kdeplot(x= ds.BudgetMillions,y=ds.CriticRating)


# In[62]:


#subplots

f, ax = plt.subplots(1,2, figsize =(12,6))
#f, ax = plt.subplots(3,3, figsize =(12,6))


# In[66]:


ds.head(1)


# In[68]:


f,axes= plt.subplots(1,2,figsize =(12,6))
#k1 = sns,kdeplot(x= ds.BudgetMillions,y=ds.AudienceRatings,ax = axes[0])
k1 = sns.kdeplot(x=ds.BudgetMillions,y=ds.AudienceRatings,ax=axes[0])
k2 = sns.kdeplot(x=ds.BudgetMillions,y=ds.CriticRating,ax = axes[1])


# In[69]:


axes


# In[70]:


#Box plots - 

w = sns.boxplot(data=ds, x='Genre', y = 'CriticRating')


# In[71]:


#violin plot

z = sns.violinplot(data=ds, x='Genre', y = 'CriticRating') 


# In[72]:


w1 = sns.boxplot(data=ds[ds.Genre == 'Drama'], x='Year', y = 'CriticRating')


# In[73]:


w1 = sns.violinplot(data=ds[ds.Genre == 'Drama'], x='Year', y = 'CriticRating')


# In[74]:


g =sns.FacetGrid (ds, row = 'Genre', col = 'Year', hue = 'Genre') #kind of subplots


# In[75]:


plt.scatter(ds.CriticRating,ds.AudienceRatings)


# In[76]:


g =sns.FacetGrid (ds, row = 'Genre', col = 'Year', hue = 'Genre')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRatings' ) #scatterplots are mapped in facetgrid


# In[77]:


# you can populated any type of chat. 

g =sns.FacetGrid (ds, row = 'Genre', col = 'Year', hue = 'Genre')
g = g.map(plt.hist, 'BudgetMillions') #scatterplots are mapped in facetgrid


# In[78]:


g =sns.FacetGrid (ds, row = 'Genre', col = 'Year', hue = 'Genre')
kws = dict(s=50, linewidth=0.5,edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRatings',**kws ) #scatterplots are mapped in facetgrid


# In[ ]:




