
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x=np.arange(0,100)
y=x*2
z=x**2


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Exercise 1

# In[5]:


fig=plt.figure()
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y,'b')
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Example')


# ## Exercise 2

# In[17]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax1.plot(x,y,'b')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax2=fig.add_axes([0.2,0.5,0.2,0.2])
#ax2.set_xlim(auto=True)
#ax2.set_ylim([0, 200])
ax2.plot(x,y,'r')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')


# ## Exercise 3

# In[12]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax1.plot(x,z,'b')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Z Label')
ax2=fig.add_axes([0.2,0.5,0.4,0.4])
ax2.set_title('Zoom')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])
ax2.plot(x,y,'r')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')


# ## Exercise 4

# In[28]:


f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=False)
ax1.plot(x, y,'b--')
ax2.plot(x, z,'r')    


# In[12]:


f1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,figsize=(10,2))
ax1.plot(x, y,'b')
ax2.plot(x, z,'r--')  

