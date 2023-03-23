# TitanicVisualization.py
#
# Author:  Logan Segal
# Email:   segalla@g.cofc.edu
# Class:   CSCI 299/284   
# Assignment: Homework #3
# Due Date:  Feb. 27, 2023 
#
# Purpose: Demonstrates a visulaization so we can better understand that gender and class did have an effect on survival ratings. 
#
# Input:   Data about survival rates from the Titanic focusing on wheter or not 
#          the passenger surivived, their class, and their gender.
#
# Output:  A visualization showing how gender and class had an effect on survival rates. Keeping a water theme, using bubbles to represent
#          people, but using size, placement, and color to represent the data. The upper half of the display represents the people that survived
#          hence the larger bubble sizes, while the bottom half represetns people who didn't survive using smaller sized bubbles. 
#
# Visualization Design
#  * color represents gender
#     - blue for male
#     - pink for female
#  * size represents social status
#     - big for 1st class
#     - medium for 2nd class
#     - small for 3rd class
#  * placement for survival
#     - upper half (baby blue) they survived
#     - bottom half (deep sea blue) they did not survive
#  * passenger names appears when you hover over the bubble
#

from gui import*
from string import*
from random import*

#opening up the data and reading the file 
data = open("TitanicDataVis.csv", "r")
#read and process every line of data
survivalData = []                   # holds survival information
classData = []                      # holds class information
nameData = []                       # hold name information
genderData = []                     # holds gender information
for line in data:
   survival, status, name, gender = split(line,",")     # splitting the data into four values
   survival = int(survival)        # gathering survival values
   status = int(status)            # gathering social status values
   gender = rstrip(gender)           # gathering gender values
   name = replace(name, ":", ",")    # replacing : with , in the name
   survivalData.append(survival)        # grouping the survival data  
   classData.append(status)             # grouping the class/status data
   nameData.append(name)                # appending the name 
   genderData.append(gender)            # grouping the gender data
data.close()      # done with file, closing time

# replacing gender values with numbers
for i in range(len(genderData)):
   # replace male with 0
   if genderData[i] == 'male':
      genderData[i] = int('0')
   # replace female with 1
   if genderData[i] == 'female':
      genderData[i] = int('1')

# creating the display
d = Display("The Effects of Gender and Class on Survival Ratings from the Titanic", 1440,775)
d.setColor(Color(0,60,95))                         # background color 
recColor = Color(139, 206, 235)                    # rectangle color
r = Rectangle(0, 0, 1440, 387, recColor, True)     # left-top and right-bottom corners
d.add(r)                                           # adding the rectangle to the display

# amount of circles to draw
numberOfCircles = len(genderData)

# draw various circles based on gender, class, and survival
for i in range(numberOfCircles):
   
   # create a random circle, and place it on the display
   
   # posititon based on survival  
   if survivalData[i] == 0:                     # did not survive (bottom)
      x = randint(0, d.getWidth()-1)            # x may be anywhere on display
      y = randint(410, d.getHeight()-1)         # y may be anywhere on the bottom half 
      
      # creating different radii based on status values
      if classData[i] == 1.0:                   # 1st class
         radius = 5                                # setting the radius
      elif classData[i] == 2.0:                 # 2nd class
         radius = 10                                # setting the radius
      elif classData[i] == 3.0:                 # 3rd class
         radius = 15                               # setting the radius
         
      # setting the color of the circle based on gender
      if genderData[i] == 1:                    # female 
         color = Color(255,192,203)                # set the color to light pink 
      elif genderData[i] == 0:                  # male
         color = Color(108,160,220)                # set the color to baby blue
      
      c = Circle(x, y, radius, color)           # create a circle from various values
      c.setToolTipText(nameData[i])             # setting a tool tip to dislplay the names
      d.add(c)                                  # adding the circle to the diplay
   
   # posititon based on survival
   else:                                     # survived (top)
      x = randint(0, d.getWidth()-1)         # x may be anywhere on display
      y = randint(0, 360)                    # y may be anywhere on the upper half 
      
      # creating different radii based on status values
      if classData[i] == 1.0:                # 1st class          
         radius = 5                             # setting the radius
      elif classData[i] == 2.0:              # 2nd class
         radius = 10                            # setting the raidus 
      elif classData[i] == 3.0:              # 3rd class
         radius = 15                            # setting the radius
      
      # setting the color of the circle based on gender
      if genderData[i] == 1:                 # female
         color = Color(243,83,144)              # hot pink
      elif genderData[i] == 0:               # male
         color = Color(65,105,225)              # royal blue
      
      c = Circle(x, y, radius, color)        # create a circle from various values
      c.setToolTipText(nameData[i])          # setting a tool tip to dislplay the names
      d.add(c)                               # adding the circle to the diplay


      
   