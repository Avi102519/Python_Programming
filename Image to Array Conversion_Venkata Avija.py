#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt #


# In[3]:


from PIL import Image #Python Image Library


# In[4]:


horse = Image.open(r'/Users/aviswe/Desktop/830/Practice/HorseImage.jpg')


# In[5]:


horse


# In[6]:


plt.show(horse)


# In[7]:


type(horse)


# In[8]:


horse_arr = np.asarray(horse) #converting image to array


# In[9]:


horse_arr 


# In[10]:


type(horse_arr)


# In[11]:


horse_arr.shape  #Shape format-width,height,Dimension


# In[12]:


plt.imshow(horse_arr)


# In[13]:


horse_red = horse_arr.copy() #copied horse array into horse_red variable
horse_red


# In[14]:


plt.imshow(horse_red) #image_red image view


# In[15]:


horse_red.shape


# In[16]:


plt.imshow(horse_red[:,:,0]) #Hyper parameterization with color codes


# In[17]:


horse_red[:,:,0]


# In[18]:


plt.imshow(horse_red[:,:,0],cmap = 'gray')


# In[19]:


plt.imshow(horse_red[:,:,0],cmap = 'Purples')


# In[20]:


plt.imshow(horse_red[:,:,0],cmap = 'Blues')


# In[21]:


plt.imshow(horse_red[:,:,1],cmap = 'gray')


# In[22]:


plt.imshow(horse_red[:,1:,0],cmap = 'gray')


# In[23]:


plt.imshow(horse_red[:,:,2],cmap = 'gray')


# In[24]:


horse_red[:,:,0]


# In[25]:


horse_red[:,:,1]


# In[26]:


horse_red[:,:,2]


# In[27]:


horse_red[:,:,1] =0


# In[28]:


horse_red[:,:,1]


# In[29]:


plt.imshow(horse_red)


# In[30]:


horse_red[:,:,2] =0


# In[31]:


horse_red[:,:,2]


# In[32]:


plt.imshow(horse_red)


# In[33]:


arr1 = np.asarray(horse)


# In[34]:


type(arr1)


# In[35]:


arr1.shape


# In[36]:


plt.imshow(arr1)


# In[ ]:




