#!/usr/bin/env python
# coding: utf-8

# In[1]:


def update(x):
    x= 8
    print(x)
update(10)


# In[2]:


def update(x):
    x=8
    return x
update(10)


# In[4]:


def update(name,age):
    print(name)
    print(age)
update('Aira',5)


# In[5]:


def update(name,age):
    print(name)
    print(age)
update(5,'Aira')


# # Define the function without argument

# In[6]:


def add(x,y):
    c=x+y
    print(c)
add(5)


# In[7]:


def add(x,y):
    c= x+y
    print(c)
add(5,6,7,8)


# In[8]:


def add(x,y):
    c=x+y
    print(c)
add(5,'a')


# In[9]:


def add(x,y):
    c=x+y
    print(c)
add(5,4)


# In[10]:


def greet():
    print('hello')
    print('good morning')
greet()

def add(x,y):
    c=x+y
    print(c)
    
add(5,4)


# In[11]:


def greet():
    print('hello')
    print('good morning')
def add(x,y):
    c=x+y
    print(c)
greet()
print('___________')
add(5,4)


# In[12]:


def add(x,y,z):
    c=x+y+z
    print(c)
add(6,4,5)


# In[13]:


def greet():
    print('hello')
    print('Good Noon')

def add(x,y):
    c=x+y
    return c
def sub(x,y):
    d=x-y
    return d
greet()
add(5,4)
sub(10,2)


# In[14]:


def greet():
    print('hello')
    print('Good Noon')

def add(x,y):
    c=x+y
    print(c)
def sub(x,y):
    d=x-y
    return d
greet()
add(5,4)
sub(10,2)


# In[15]:


def greet():
    print('hello')
    print('Good Noon')

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
greet()
add_sub(8,1)


# In[16]:


def add_sub(x,y): #what if i want to return 2 values & function can accept multiple values
    c=x+y
    d=x-y
    return c,d
result = add_sub(6,4)

print(result)
print(type(result))


# In[19]:


def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
res1,res2 = add_sub(6,2)
print(res1,res2)
print(type(res1))
print(type(res2))


# # Update Variable

# In[20]:


def update():
    x=8
    print(x)
update()


# In[21]:


def update():
    x=8
    print(x)
update(8)


# In[22]:


def update(x): #Update function takes inside value
    x=8
    print(x)
update(10)


# In[23]:


def update(x): # print function takes priority than update
    x=8
    return x

a= 10
update(a)
print(a)


# # Function Argument

# In[24]:


def add(a,b): #a,b is called formal arguments
    c=a+b
    print(c)
add(6,4) #6,4 are called actual arguments


# In[25]:


#formal arguments shall match with actual arguments
def add(a,b): 
    c=a+b
    print(c)
add(4,5,6)


# In[26]:


def add(a,b):
    c=a+b
    print(c)   
add(5)


# In[27]:


def person(name,age):
    print(name)
    print(age)
person('nit',25)


# In[28]:


def person(name,age):
    print(name)
    print(age)
person('nit')


# In[29]:


#Change the actual arguments sequence,Still it works
def person(name,age):
    print(name)
    print(age)
person(25,'nit')


# In[30]:


def person(name,age):
    print(name)
    print(age-5)
person(22,'nit')


# In[31]:


def person(name,age):
    print(name)
    print(age-5) #The function sequence has to follow when we use arithmetic operations 
person('nit',22)


# # Keyword Arguments

# In[32]:


def person(name,age):
    print(name)
    print(age-5)
person(age=22,name='nit') # No need to follow sequence,if we use both formal and actual arguments at the function calling


# In[33]:


def person(name, age, mob):
    print(name)
    print(age-5)
    print(mob)
    
person(age = 22, name = 'nit', mob = 101)


# In[34]:


def person(name, age=18): #Default values for formal arguments
    print(name)
    print(age)
    
person('nit')


# In[35]:


def persom(name, age=18):
    print(name)
    print(age)
person('nit',40)


# In[ ]:




