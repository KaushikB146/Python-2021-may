
# coding: utf-8

# In[1]:


print("hello world")

try:
    print(name)
except:
    print("Name variable is not defined")
      
print('Welcome to exception handling')
print('Thank you')


# In[3]:


print("start of the program")

try:
    num1 = int(input("Enter the numerator : "))
    num2 = int(input("Enter the denominator : "))

    print('Numerator = {} , Denominator = {}'.format(num1,num2))

    result = num1/num2
    print("result = ",result)
    
except ZeroDivisionError:
    print("Enter a non-zero denominator")
    
except ValueError:
    print("Please enter the numbers only")
    
except:
    print("Something went wrong")
    
finally:
    print("End of program")

