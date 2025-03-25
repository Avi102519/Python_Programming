#!/usr/bin/env python
# coding: utf-8

# # Import Pandas library

# In[1]:


import pandas as pd


# In[16]:


Data = {"Address":["5200,Virginia Way,Brentwood,TN,37027","1100, Martin Luther king Blvd,Nashville,TN,37211"],
        "Date":["11/01/2015","09/23/2023"],
        "time":["08:30:00","06:00:00"],
        "Name":["TCS","HCA"]
       }


# # Convert to data Frame

# In[41]:


dataframe1 = pd.DataFrame(Data)


# In[42]:


dataframe1


# In[43]:


dataframe1["Address"]


# # Split Address into multiple columns

# In[44]:


dataframe1[["bldg","Street","City","State","ZipCode"]]= dataframe1["Address"].str.split(',',expand =True)


# In[45]:


print(dataframe1)


# # Split Date into multiple columns

# In[46]:


dataframe1["Date"]


# In[47]:


dataframe1[["month","Day","Year"]]= dataframe1["Date"].str.split('/',expand = True)


# In[48]:


print (dataframe1)


# # Split time into multiple columns

# In[49]:


dataframe1["time"]


# In[50]:


dataframe1[["hr","min","sec"]]= dataframe1["time"].str.split(':',expand = True)
print(dataframe1)


# # Drop the original columns

# In[51]:


dataframe1.drop(columns = ["time"],inplace = True)
dataframe1.drop(columns = ["Address"],inplace = True)
dataframe1.drop(columns = ["Date"],inplace = True)


# In[52]:


print(dataframe1)


# # Join the splitted data into dataframe

# In[53]:


dataframe2 = pd.DataFrame(dataframe1)


# In[54]:


dataframe2


# In[ ]:


excel = pd.read_excel(r'file location')
xml = pd.read_xml(r'file location')
html = pd.read_html(r'file location')

