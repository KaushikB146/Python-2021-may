
# coding: utf-8

# In[2]:


square = lambda num:num**2
square(5)


# In[3]:


add = lambda x,y,z:x + y + z
add(5,10,15)


# In[4]:


my_nums = [1,2,3,4,5]
map(square,my_nums)


# In[5]:


my_nums = [1,2,3,4,5]
def even_odd(num):
    if(num%2==0):
        return 'even'
    else:
        return 'odd'
list(map(even_odd,my_nums)) 


# In[6]:


words_list = ['apple','banana','airport','ant','cat']
def starts_with_a(word):
    if(word[0] == 'a'):
        return True
    else:
        return False
list(filter(starts_with_a,words_list)) 


# In[7]:


nums = [0,1,2,3,4,5,6,7,8,9,10]
def check_even(num):
    if(num%2==0):
        return True
    else:
        return False
list(map(check_even,nums))


# In[8]:


nums = [0,1,2,3,4,5,6,7,8,9,10]
def check_even(num):
    if(num%2==0):
        return True
    else:
        return False
list(filter(check_even,nums))


# In[9]:


my_nums = [1,2,3,4,5]
filter(lambda num:num%2 == 0,nums)
for item in filter(lambda num:num%2 == 0,nums):
    print(item)

