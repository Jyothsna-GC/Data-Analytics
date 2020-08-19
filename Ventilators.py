#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pulp import *


# In[2]:


prob = LpProblem("Ventilators", LpMaximize) #Create a LP max problem
x = LpVariable("x", lowBound=0, cat='Integer') # Create a variable x >= 0
y = LpVariable("y", lowBound=0, cat ='Integer') # Create a variable y >= 0
prob += 200 * x * 25 + 140 * y * 30 # Objective function
prob += x <= 30 # Max hours on x per week
prob += y <= 28.57 # Max hours on y per week
prob += x + y <= 40 # Hours per week 
prob

status=prob.solve()
LpStatus[status]

value(x), value(y), value(prob.objective)


# In[ ]:




