#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(7**4)


# In[2]:


s = 'Hi there Sam!'
print(s.split(" "))


# In[3]:


planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers".format(planet, diameter))


# In[4]:


lst = [1,2,[3,4], [5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])


# In[5]:


d = {
    'k1': [1,2,3,{
        'tricky': ['oh', 'man', 'inception',{'target': 
                                             [1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


# In[6]:


# Tuple is immutable


# In[11]:


def domainGet(str):
    arr = str.split('@');
    if len(arr) == 2:
        return arr[1]
    raise Exception('Email is not valid')
print(domainGet('user@domain.com'))
print(domainGet('userdomain.com'))


# In[15]:


def findDog(str):
    import re
    return True if re.search("[^a-zA-Z0-9]dog[^a-zA-Z0-9]", str) else False
print(findDog('This is a dog.'))
print(findDog('Is there a dog here.'))
print(findDog('This is a dog.s'))
print(findDog('This is a dogs .'))
print(findDog('This is a Dog.'))
print(findDog('This is a sdog.'))


# In[23]:


def countDog(str):
    import re
    arr = re.findall("^dog\s|\sdog\s|\sdog$", str)
    return len(arr)
print(countDog('dog This dog is a dog. dogs'))
print(countDog('this dog runs faster than the other dog dude!'))


# In[27]:


seq = ['soup', 'dog', 'salad', 'cat', 'great']
list(filter(lambda item: item[0] == 's', seq))


# In[35]:


def caught_speeding(speed, is_birthday):
    if speed <= 60 or (speed <= 65 and is_birthday):
        print('No Ticket' )
    elif speed <= 80 or (speed <= 85 and is_birthday):
        print('Small Ticket')
    else:
        print('Big Ticket')
caught_speeding(81, True)
caught_speeding(81, False)
caught_speeding(65, False)
caught_speeding(65, True)
caught_speeding(75, False)
caught_speeding(75, True)