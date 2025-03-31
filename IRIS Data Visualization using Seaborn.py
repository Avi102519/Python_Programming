#!/usr/bin/env python
# coding: utf-8

# # IRIS Dataset Visualization using Seaborn,Matplotlib

# In[22]:


import numpy as np #linear algebra
import pandas as pd #data processing,CSV file I/O(e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[4]:


iris=pd.read_csv(r'/Users/aviswe/Desktop/830/Datasets/Iris.csv')


# In[5]:


iris


# # **Displaying data**

# In[6]:


iris.head()


# In[7]:


iris.drop('Id',axis=1,inplace=True)


# In[8]:


iris.head()


# In[10]:


#Checking for missing values
iris.info()


# In[12]:


iris['Species'].value_counts()


# In[16]:


#to view the frequency of the three species in the dataset
#sns.countplot('Species',data=iris)
#plt.show()

sns.countplot(x='Species', data=iris)
plt.show()


# in the above graph each species have 50 smaples in the iris dataset

# # Jointplot in the seaborn library specific and can be used to quickly visualize and analyze the relationship between two variables and describe their individual distributions on the same plot

# In[17]:


iris.head()


# In[18]:


fig = sns.jointplot(x='SepalLengthCm',y = 'SepalWidthCm',data=iris)


# In[20]:


sns.jointplot(x="SepalLengthCm",y="SepalWidthCm", data=iris, kind = "reg")


# In[21]:


sns.jointplot(x="SepalLengthCm",y="SepalWidthCm", data=iris, kind = "hex")


# # FacetGrid Plot

# In[27]:


#5.FacetGrid Plot¶

sns.FacetGrid(iris,hue='Species',height=5)\
.map(plt.scatter,'SepalLengthCm','SepalWidthCm')\
.add_legend() #Instead of height we can use size


# # BoxPlot-Visualize the statistical summary of the features being plotted.

# In[28]:


iris.head(1)


# In[32]:


fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.boxplot(x='Species',y='PetalLengthCm',data=iris,order=['Iris-virginica','Iris-versicolor','Iris-setosa'],linewidth=2.5,orient='v',dodge=False)


# In[33]:


iris.boxplot(by='Species',figsize=(12,6))


# # Strip plot

# In[35]:


fig= plt.gcf()
fig.set_size_inches(10,7)
fig=sns.stripplot(x='Species',y='SepalLengthCm',data=iris,jitter=True,edgecolor='gray',size=8,palette='winter',orient='v')


# # Combining box and Strip plots

# In[38]:


fig = plt.gcf()
fig.set_size_inches(10,7)
fig=sns.boxplot(x='Species',y='SepalLengthCm',data=iris)
fig=sns.stripplot(x='Species',y='SepalLengthCm',data=iris,jitter=True,edgecolor='gray')


# In[44]:


ax= sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax= sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")

#boxtwo=ax.artists[2]
#boxtwo.set_facecolor('yellow')
#boxtwo.set_edgecolor('black')
#boxthree=ax.artists[1]
#boxthree.set_facecolor('red')
#boxthree.set_edgecolor('black')
#boxfour=ax.artists[0]
#boxfour.set_facecolor('green')
#boxfour.set_edgecolor('black')



for i,artist in enumerate(ax.artists):
    colors=['yellow','red','green']
    edge_colors =['black','black','black']
    artist.set_facecolor(colors[i])
    artist.set_edgecolor(edge_colors[i])
    
plt.show()


# # Violin Plot- to see the distribution of data and its probability distribution
# this chart is a combination of Boxplot and Density plot that is rotated and placed on eachside.

# In[46]:


fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.violinplot(x='Species',y ='SepalLengthCm',data=iris)


# In[47]:


plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
sns.violinplot(x='Species',y='PetalLengthCm',data=iris)
plt.subplot(2,2,2)
sns.violinplot(x='Species',y='PetalWidthCm',data=iris)
plt.subplot(2,2,3)
sns.violinplot(x='Species',y='SepalLengthCm',data=iris)
plt.subplot(2,2,4)
sns.violinplot(x='Species',y='SepalWidthCm',data=iris)


# ** Pair Plot:**
# A “pairs plot” is also known as a scatterplot, in which one variable in the same data row is matched with another variable's value, like this: Pairs plots are just elaborations on this, showing all variables paired with all the other variables.

# In[48]:


sns.pairplot(data=iris,kind='scatter')


# In[49]:


sns.pairplot(iris,hue='Species')


# ** Heat map**
# Heat map is used to find out the correlation between different features in the dataset.High positive or negative value shows that the features have high correlation.This helps us to select the parmeters for machine learning.

# In[90]:


#fig =plt.gcf()
#fig.set_size_inches(10,7)
#numeric_iris=iris.drop(columns=['Species'])
#fig=sns.heatmap(iris.corr(),annot=True,cmap='cubehelix',linewidths=1,linecolor='k',square=True)
#plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Drop non-numeric column
iris_numeric = iris.drop(columns=['Species'])

# Create heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(iris_numeric.corr(), annot=True, cmap='cubehelix', linewidths=1, linecolor='k')
plt.title("Correlation Heatmap - Iris Dataset")
plt.show()


# ** Distribution plot:**
# The distribution plot is suitable for comparing range and distribution for groups of numerical data. Data is plotted as value points along an axis. You can choose to display only the value points to see the distribution of values, a bounding box to see the range of values, or a combination of both as shown here.The distribution plot is not relevant for detailed analysis of the data as it deals with a summary of the data distribution.

# In[54]:


iris.hist(edgecolor='black', linewidth=1.2)
fig=plt.gcf()
fig.set_size_inches(12,6)


# # ** Swarm plot**
# It looks a bit like a friendly swarm of bees buzzing about their hive. More importantly, each data point is clearly visible and no data are obscured by overplotting.A beeswarm plot improves upon the random jittering approach to move data points the minimum distance away from one another to avoid overlays. The result is a plot where you can see each distinct data point, like shown in below plot

# In[60]:


sns.set(style="darkgrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.swarmplot(x="Species",y="PetalLengthCm",data= iris)


# In[61]:


sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
ax = sns.violinplot(x="Species", y="PetalLengthCm", data=iris, inner=None)
ax = sns.swarmplot(x="Species", y="PetalLengthCm", data=iris,color="white", edgecolor="black")


# # lmplot

# In[63]:


fig=sns.lmplot(x="PetalLengthCm",y = "PetalWidthCm",data = iris)


# # FacetGrid

# In[65]:


sns.FacetGrid(iris,hue = "Species",height =6) \
.map(sns.kdeplot, "PetalLengthCm") \
.add_legend()
plt.ioff()


# # Factor Plot

# In[69]:


#sns.factorplot('Species','SepalLengthCm',data=iris)
#plt.ioff()
#plt.show()


sns.catplot(x='Species',y='SepalLengthCm',data=iris)
plt.ioff()
plt.show()


# # Boxen Plot

# In[75]:


#fig=plt.gcf()
#fig.set_size_inches(10,7)
#fig=sns.boxenplot(x='Species',y='SepalLengthCm',data=iris)

import matplotlib.pyplot as plt #added


fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.boxenplot(x='Species',y='SepalLengthCm',data=iris)
plt.show() #added


# # KDE plot

# In[81]:


#sub= iris[iris['Species']=='Iris-setosa']
#sns.kdeplot(data=sub[['SepalLengthCm','SepalWidthCm']],cmap="plasma",shade=True,shade_lowest=False)
#plt.title('Iris-setosa')
#plt.xlabel('Sepal Length Cm')
#plt.ylabel('Sepal Width Cm')




sub=iris[iris['Species']=='Iris-setosa']
sns.kdeplot(data=sub,x='SepalLengthCm',y='SepalWidthCm',cmap="plasma",shade=True,shade_lowest = False)
#sns.kdeplot(data=sub[[x='SepalLengthCm',y='SepalWidthCm']],cmap="plasma", shade=True, shade_lowest=False)
plt.title("Iris-setosa")
plt.xlabel("Sepal Length Cm")
plt.ylabel("Sepal Width Cm")
plt.show()


# # Dashboard

# In[82]:


sns.set_style('darkgrid')
f,axes=plt.subplots(2,2,figsize=(15,15))

k1=sns.boxplot(x="Species", y="PetalLengthCm", data=iris,ax=axes[0,0])
k2=sns.violinplot(x='Species',y='PetalLengthCm',data=iris,ax=axes[0,1])
k3=sns.stripplot(x='Species',y='SepalLengthCm',data=iris,jitter=True,edgecolor='gray',size=8,palette='winter',orient='v',ax=axes[1,0])
#axes[1,1].hist(iris.hist,bin=10)
axes[1,1].hist(iris.PetalLengthCm,bins=100)
#k2.set(xlim=(-1,0.8))
plt.show()


# # In the dashboard we have shown how to create multiple plots to foam a dashboard using Python.In this plot we have demonstrated how to plot Seaborn and Matplotlib plots on the same Dashboard.

# # Stacked Histogram

# In[83]:


iris['Species'] = iris['Species'].astype('category')


# In[84]:


list1=list()
mylabels=list()
for gen in iris.Species.cat.categories:
    list1.append(iris[iris.Species==gen].SepalLengthCm)
    mylabels.append(gen)
    
h=plt.hist(list1,bins=30,stacked=True,rwidth=1,label=mylabels)
plt.legend()
plt.show()


# # With Stacked Histogram we can see the distribution of Sepal Length of Different Species together.This shows us the range of Sepan Length for the three different Species of Iris Flower.

# # **Area Plot:**
# Area Plot gives us a visual representation of Various dimensions of Iris flower and their range in dataset.

# In[87]:


iris.plot.area(y=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'],alpha=0.4,figsize=(12, 6));
plt.show()


# # Distplot
# It helps us to look at the distribution of a single variable.Kde shows the density of the distribution
# 

# In[89]:


sns.distplot(iris['SepalLengthCm'],kde=True,bins=20);
plt.show()


# In[ ]:




