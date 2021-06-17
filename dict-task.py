
# coding: utf-8

# In[17]:


dict1 = {
    "Brand":"Bajaj",
    "model":"Pulsar",
    "year":2015,
    "cost":85000
}
dict1
dict1["model"]
keys = list(dict1.keys())
print(keys)
vals = list(dict1.values())
print(vals)


# In[24]:


dict1 = {
    "Brand":"Bajaj",
    "model":"Pulsar",
    "year":2015,
    "cost":85000
}
dict1["color"] = "Black"
dict1["Discount"] = 10000
R = dict1.pop("model")
del dict1['year']
dict1.clear()
print(dict1)


# In[27]:


D1= {
  "brand": "Bajaj",
  "model": "Pulsar",
  "year": 2015,
  "cost": 85000
}
D2= D1.copy()
print(D2)


# In[28]:


C1 = {
  "name" : "SUSH",
  "year" : 1995
}
C2 = {
  "name" : "MITHA",
  "year" : 2001
}

myfamily = {
  "C1" : C1,
  "C2" : C2
}
myfamily


# In[60]:


dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}

#access "Mike"
#access 80
#change "Mike" to "Your name"
#add ML = 80 and DL = 80 inside marks

dict1["april_batch"]["student"]["marks"]["DL"] = 80
dict1["april_batch"]["student"]["marks"]["ML"] = 80
print(dict1)

