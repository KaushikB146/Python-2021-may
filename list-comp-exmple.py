
# coding: utf-8

# In[1]:


x  = 'PythonList'

x_list = [] # step 1

for char in x: # step 2
    x_list.append(char) # step 3
    
print(x_list)


# In[2]:


list1 = []

for i in range(11):
    list1.append(i**2)

print(list1)


# In[3]:


list1 = [] 

for i in range(11):
    if(i%2 == 0):
        list1.append(i)
        
print(list1)


# In[4]:


km_list = [1,2,3,4,5]

m_list = []

for i in km_list:
    m_list.append(i*1000)
    
print(m_list)

