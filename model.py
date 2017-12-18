# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:20:02 2017

@author: Paul
"""
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.

import random

# Set Up Varibles
#y0 = 50
#x0 = 50
# Extra Variable for Try2
#random_number = random.random()


#First Step Testing
#print (y0)
#print (x0)

#Random Walk one step. Try1
"""
if random.random() < 0.5:
    y0 = y0 + 1 
else:
    y0 = y0 -1

print (y0)
"""


#Random Walk one step. Try2 
"""
if random_number < 0.5:
    y0 += 1 
else:
    y0 -= 1
    
print (y0)
"""

#Random Walk one step. Try3 Combined y&x
"""
if random_number < 0.5:
    y0 += 1 
    x0 += 1
else:
    y0 -= 1
    x0 -= 1
    
print ("y is " + str(y0))
print ("x is " + str(x0))
"""

#Random Walk one step. Try4 
#y&x seperate so their individual changes are each random 
"""
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1 
else:
    x0 -= 1  

print ("y is " + str(y0) + " and x is " + str(x0))
"""
#trying the suggested print
#print (y0,x0)

#Random Walk one step. Try5
#Mulitple steps
#y Step 1
"""
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1
#y Step 2
if random.random() < 0.5:
    x0 += 1 
else:
    x0 -= 1  

#x Step 1
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1

#x Step 2
if random.random() < 0.5:
    x0 += 1 
else:
    x0 -= 1  
print ("y is " + str(y0) + " and x is " + str(x0))





# Set Up Varibles for Agent 2
y1 = 50
x1 = 50

#Random Walk one step. Try6
#Mulitple steps for Agent 2
#y Step 1
if random.random() < 0.5:
    y1 += 1 
else:
    y1 -= 1
#x Step 1
if random.random() < 0.5:
    x1 += 1 
else:
    x1 -= 1  

#y Step 2
if random.random() < 0.5:
    y1 += 1 
else:
    y1 -= 1
#x Step 2
if random.random() < 0.5:
    x1 += 1 
else:
    x1 -= 1  
print ("y1 is " + str(y1) + " and x1 is " + str(x1))


euclidiean_distance = (((y0-y1)**2)+((x0-x1)**2))**0.5

print ("The euclidiean distance between the two agents is " + str(euclidiean_distance))
"""








#Random Start postion with 100x100grid. code

# Set Up Varibles
#agent 1
y0 = random.randint(0,99)
x0 = random.randint(0,99)
#agent 2
y1 = random.randint(0,99)
x1 = random.randint(0,99)
print ("Start postion for agent 1 is - y " + str(y0) + " x " + str(x0))
print ("Start postion for agent 2 is - y " + str(y1) + " x " + str(x1))


#Move Agent 1 2 steps in random direction
#y Step 1
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1
#x Step 1
if random.random() < 0.5:
    x0 += 1 
else:
    x0 -= 1  

#y Step 2
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1

#x Step 2
if random.random() < 0.5:
    x0 += 1 
else:
    x0 -= 1  


#Move Agent 2 2 steps in random direction
#y Step 1
if random.random() < 0.5:
    y1 += 1 
else:
    y1 -= 1
#x Step 1
if random.random() < 0.5:
    x1 += 1 
else:
    x1 -= 1  

#y Step 2
if random.random() < 0.5:
    y1 += 1 
else:
    y1 -= 1

#x Step 2
if random.random() < 0.5:
    x1 += 1 
else:
    x1 -= 1  

print ("New postion for agent 1 is - y " + str(y0) + " x " + str(x0))
print ("New postion for agent 2 is - y " + str(y1) + " x " + str(x1))

#Calculate the distance between the two agents
#uses Y difference squared added to X difference squared then square rooted
euclidiean_distance = (((y0-y1)**2)+((x0-x1)**2))**0.5

print ("The euclidiean distance between the two agents is " + str(euclidiean_distance))
