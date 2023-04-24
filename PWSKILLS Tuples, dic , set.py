#!/usr/bin/env python
# coding: utf-8

# In[1]:


t =()


# In[2]:


type(t)


# In[3]:


t1 = (1,2,3,4,45,45.45,45+4j, "sudh", True)


# In[4]:


type(t1)


# In[5]:


l = [1,2,3,4]


# In[6]:


type(l)


# In[7]:


t1


# In[8]:


t1[0]


# In[9]:


t1[1]


# In[10]:


t1[7]


# In[11]:


t1[::-1]


# In[12]:


t1 = t1[::-1] # reverse 


# In[13]:


t1


# In[14]:


t1[0:3]


# In[15]:


t1.count(4)


# In[16]:


t1.count("abc")


# In[17]:


t1.index(2)


# In[18]:


t1.index(1)


# In[19]:


t1[-1]


# In[20]:


t1.index("sudh")


# In[21]:


t1.count(True)


# In[22]:


t1.count(1)


# In[23]:


t1


# In[24]:


l


# In[25]:


t1[0]


# In[26]:


t1[-1]


# In[27]:


t1[0] = 345


# In[ ]:


t1


# In[ ]:


type(t1)


# In[ ]:


l[0]


# In[28]:


l[0]


# In[29]:


1


# In[30]:


t1


# In[31]:


for i in t1:
    print(i)


# In[32]:


t2 = (True, "Sudh", (45+7j), 45.45, 45,4,3,2,1)


# In[33]:


for i in t2:
    print(i,type(i))


# In[34]:


t2 = (1,2,3,3,4)


# In[35]:


t2*3


# In[36]:


max(t2)


# In[37]:


min(t2)


# In[38]:


#typle are bsically follows immutability concepts where it is not going  to allow to change any element in particular inde


# In[39]:


t1


# In[40]:


t2


# In[41]:


t1 = (1,2,32,4)
t2 = (4,5,6,7,8)


# In[42]:


t3 = (t1,t2)


# In[43]:


t3


# In[44]:


t4 = ((1,2,3,4,5),[1,3,5,6,7,8])


# In[45]:


t4


# In[46]:


del t4


# In[47]:


t4


# In[48]:


t2


# In[49]:


len(t2)


# In[50]:


"sudh" in t1


# In[51]:


2 in t1


# #Sets

# In[52]:


s = {}


# In[53]:


type(s)


# In[54]:


set2 = set()


# In[55]:


type(set2)


# In[56]:


s1 = {1,2,3,4,5}


# In[57]:


type(s1)


# In[58]:


s2 = {1,1,12,3,3,3,4,5,5,55,523,34,3,45,6,67}


# In[59]:


s2


# In[60]:


list(s2)


# In[61]:


tuple(s2)


# In[62]:


l


# In[63]:


l = list(s2)


# In[64]:


tuple(s2)


# In[65]:


l


# In[66]:


set(l)


# In[67]:


s4 = {1,2,3,4,[1,2,3,4]}


# In[68]:


s5 = {1,2,3,4,(1,2,3,4)}


# In[69]:


s5


# In[70]:


s6 = {"sudh", "Sudh", 2,3,4,5}


# In[71]:


s6


# In[72]:


s7 = {"sudh", "sudh", 2,3,4,5}


# In[73]:


s7


# In[74]:


s7[0]


# In[75]:


s7[::-1]


# In[76]:


s7


# In[77]:


for i in s7:
    print(i)


# In[78]:


s7


# In[79]:


s7.add(34)


# In[80]:


s7


# In[81]:


s7.add(2)


# In[82]:


s7


# In[83]:


len(s7)


# In[84]:


s7.pop()


# In[85]:


s7


# In[86]:


s7.clear()


# In[87]:


s7


# In[88]:


s8 = {1,2,3,4}
s9 = {1,2,3,5}


# In[89]:


s8.difference(s9)


# In[90]:


s9.difference(s8)


# #Dic

# In[91]:


d = {}


# In[92]:


type(d)


# In[93]:


d1 = {"name": "sudh", "email_id": "ss@mail.com", "number": 12345}


# In[94]:


type(d1)


# In[95]:


d1


# In[96]:


d2 = {"name": "sudh", "name": "sudhanshu", }


# In[97]:


d2


# In[98]:


d3 = {234234: "abc"}


# In[99]:


d3


# In[100]:


d4 = {234.45 :"abc"}


# In[101]:


d4


# In[102]:


d5 = {True : "abc"}


# In[103]:


d5


# In[104]:


d6 = {# : "abc"}


# In[105]:


d7 = {@ :"avc"}


# In[106]:


d8 ={ "avn" : @@}


# In[107]:


d8


# In[108]:


d9 = {"ab" : [1,2,3,4]}


# In[109]:


d9


# In[110]:


d10 = {('ab',"dg"): [123]}


# In[111]:


d10


# In[112]:


d11 = {{"key": 234}: "abc"}


# In[113]:


d12 = {"course_name": ["data science master", "web dev", " java with dsa and  system desing"]}


# In[114]:


d12


# In[115]:


d13 = {"key" : (1,2,3,4,5)}


# In[116]:


d13


# In[117]:


d14 = {"key" : {1,2,3,4}}


# In[118]:


d14


# In[119]:


d15 = {"key": {"name": "sudhanshu ", "class": "DMS"}}


# In[120]:


d15


# In[121]:


d16 = {"batch_name": ["data science masters", "web dev", "JDS"], "start_date": (28,14,21),"mentor_name":{"krish naik", "sudhanshu", "hitesh"}}


# In[122]:


d16


# In[123]:


d16["timing"] = (8,8,8,)


# In[124]:


d16


# In[125]:


d16['batch_name']


# In[126]:


type(d16['mentor_name'])


# In[128]:


d16['keys']


# In[131]:


d16['name'] ="vandana"


# In[132]:


d16


# In[133]:


d16['name']


# In[134]:


d16['name'].upper()


# In[135]:


d16['name'].lower()


# In[136]:


d15


# In[137]:


d15['key']['class']


# In[138]:


d15['key']


# In[139]:


type(d15['key'])


# In[140]:


d15['key1']= "abc"


# In[141]:


d15


# In[142]:


del d15['key1']


# In[143]:


d15


# In[146]:


d15.clear()# clear data inside the data set


# In[147]:


d15


# In[148]:


len(d16)


# In[149]:


d16


# In[150]:


d16.keys()


# In[151]:


d16.values()


# In[152]:


list(d16.values())


# In[153]:


list(d16.keys())


# In[154]:


list(d16.items())


# In[156]:


d16


# In[157]:


d17 = d16.copy()


# In[158]:


d17


# In[159]:


d18 = d16


# In[160]:


d18


# In[161]:


del d16['name']


# In[162]:


d16


# In[163]:


d17


# In[164]:


d18


# In[165]:


d16


# In[166]:


d16.pop()


# In[168]:


d16.pop('timing')


# In[169]:


d16


# In[172]:


d.fromkeys((1,2,3) , ('a','b','c'))


# In[174]:


d19 = {'key1': "value", "key2" : "value2"}
d20 = {"keys3" : "Values3" , "keys4" : "Value4"}


# In[176]:


(d19,d20)


# In[177]:


d19.update(d20)


# In[178]:


d19


# In[179]:


d20


# In[180]:


d20.update(d19)


# In[181]:


d20


# In[182]:


d20.get("sudh")


# In[185]:


d20


# In[188]:


d20.get("keys3")


# In[189]:


d20['keys3']


# In[190]:


d20['sudh']


# In[191]:


{for i in range(1,11)}


# In[192]:


list(range(1,11))


# In[194]:


for i in range(1,11):
    print(i)


# In[196]:


{i: i**2 for i in range(1,11)}


# In[198]:


{i : i**3 for i in range(1,40)}


# In[204]:


import math
d21 ={i: math.log10(i)for i in range(1,11)}


# In[205]:


d16


# In[206]:


'batch_name' in d16


# In[207]:


d21


# In[210]:


for i in d21.keys():
    if i % 2 == 0:
        print(d21[i])


# In[211]:


for i in d21.keys():
    if i % 2 != 0:
        print(d21[i])


# In[ ]:




