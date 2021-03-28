#!/usr/bin/env python
# coding: utf-8

# ## PROBLEM STATEMENT

# Consider a consulting company has four jobs (Operations, E-Commerce, and Developer) and four persons (ARUN,SANJAY,MONICA,KEERTHI). The persons take different number of  days for completing each job is shown in the Table.
# Company wants to minimize the total number of days needed to complete the three jobs 

# In[1]:


get_ipython().run_line_magic('pip', 'install -i https://pypi.gurobi.com gurobipy')


# In[2]:


from gurobipy import *


# # Mathematical optimization
# Mathematical optimization (which is also known as mathematical programming) is a declarative approach where the modeler formulates an optimization problem that captures the key features of a complex decision problem.
# 
# A mathematical optimization model has five components:
# 
# * Sets
# * Parameters
# * Decision variables
# * Constraints
# * Objective function(s)

# In[3]:


# Defining Sets
persons = ["LIKI","MONICA","SANJAY","KEERTHI"]
jobs = ["Operations","E-Commerce","Developer","consultant"]

I = range(len(persons))
J = range(len(jobs))


# In[4]:


# parameters
Days = [
    [2,10,9,7],
    [15,4,14,8],
    [13,14,16,11],
    [3,15,13,8]
]


# In[5]:


# Model
m = Model("Assignment Model")


# # Defining the variable
# 
# 

# In[6]:


# Defining the Variable
X = {}
for i in I:
    for j in J:
       X[i,j] = m.addVar(vtype= GRB.BINARY)


# # OBJECTIVE FUNCTION

# In[7]:


#Objective Function
m.setObjective(quicksum(Days[i][j]*X[i,j] for i in I for j in J),
               GRB.MINIMIZE)


# # CONSTRAINTS

# In[8]:


#Constraint-1
for i in I:
     m.addConstr(quicksum(X[i,j] for j in J) <= 1)
#Constraint-2
for j in J:
    m.addConstr(quicksum(X[i,j] for i in I) == 1)


# In[9]:


m.optimize()
print("Optimum Solution is: ",m.objVal, "Days")


# In[10]:


for i in I:  
    for j in J:
        if X[i,j].x ==1:
            print(persons[j],": Assigned to ",jobs[i])
        


# In[ ]:




