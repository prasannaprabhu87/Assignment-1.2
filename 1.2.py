
# coding: utf-8

# In[38]:


finalOP=''
for i in range(2000,3201):
    
    if (i%7 == 0) and (i%5 != 0):
        finalOP=finalOP + str(i)+ ','
    
print (finalOP[:-1])

