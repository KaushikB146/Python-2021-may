
# coding: utf-8

# In[2]:


def func1():
    x = 10
    print(x)


# In[3]:


def outer_func():
    x = 300
    print('Outer function ',x)
    def inner_fun():
        print('Inner function ',x) 
    
    inner_fun()

outer_func()


# In[4]:


x = 300

def my_func():
    
    print('my_func : ',x)
    
    def my_inner_fun():
        print('my_inner_fun : ',x)
        
    my_inner_fun()
    
print('Global : ',x)

my_func()


# In[5]:


y = 1000

def func1():
    y = 100
    print('Value of y in func1= ', y )
    
    def func2():
        y = 10
        print('Value of y in func2= ', y )
        
        def func3():
            y = 1
            print('Value of y = ', y )
        
        func3()
    
    func2()
    
print('Value of y global = ', y )
func1()

