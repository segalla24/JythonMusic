# TitanicSonification.py
#
# Author:  Logan Segal
# Email:   segalla@g.cofc.edu
# Class:   CSCI 299/284   
# Assignment: Homework #3
# Due Date:  Feb. 20, 2023 
#
# Purpose: Demonstrates a way to create music from data
#
# Input:   Data about survival rates from the Titanic focusing on wheter or not 
#          the passenger surivived, their class, and their gender.
#
# Output:  Music using 3 differenet instruments, a stringed instruments to rep-
#          resent survival data, tubular bells to represent class data, and a
#          piano to create a background sound
#
# Sonification Design
#  Strings
#   * Survival values are mapped to pitch
#   * Gender values are mapped to dynamic
#  Tubular Bells 
#   * Class vales are mapped to pitch, pitch variation, duration, and dynamic
#   * Gender value is mapped to panning
#

from music import *
from string import *

#opening up the data and reading the file 
data = open("TitanicData.csv", "r")
#read and process every line of data
survivalData = []                   # holds survival information
classData = []                      # holds class information
genderData = []                     # holds gender information
for line in data:
   survival, status, gender = split(line,",")     # splitting the data into three values
   survival = float(survival)        # gathering survival values
   status = float(status)            # gathering social status values
   gender = rstrip(gender)           # gathering gender values
   survivalData.append(survival)        # grouping the survival data  
   classData.append(status)             # grouping the class/status data
   genderData.append(gender)            # grouping the gender data
data.close()      # done with file, closing time

# replacing gender values with numbers
for i in range(len(genderData)):
   # replace male with 0
   if genderData[i] == 'male':
      genderData[i] = float('0')
   # replace female with 1
   if genderData[i] == 'female':
      genderData[i] = float('1')

### defining the data structure (score, part, phrase)
titanicScore = Score("Titanic Sonification", 125)

classPart = Part(TUBULAR_BELLS, 0)
survivalPart = Part(STRINGS, 1)
pianoPart = Part(PIANO, 2)

classPhrase = Phrase()
survivalPhrase = Phrase()
pianoPhrase = Phrase()

# finding the range extremes
survivalMinVal = min(survivalData)
survivalMaxVal = max(survivalData)
classMinVal = min(classData)
classMaxVal = max(classData)
genderMinVal = min(genderData)
genderMaxVal = max(genderData)

# time to sonify
i = 0;               # starting value of the data
while i < len(genderData):       # while there are more values, loop
   ### survival data
   # map survival data to pitch 
   survivalPitch = mapScale(survivalData[i], survivalMinVal, survivalMaxVal, G3, AS5, DORIAN_SCALE)
   
   # map gender data to dynamic
   genderDynamic = mapValue(genderData[i], genderMinVal, genderMaxVal, 0, 115)
   
   # combining pitch and dynamic into a note
   survivalNote = Note(survivalPitch, QN, genderDynamic)
   
   # adding it to the melody 
   survivalPhrase.addNote(survivalNote)
   
   ### class/status data
   # map class data to pitch
   classPitch = mapScale(classData[i], classMinVal, classMaxVal, G7, C1, MAJOR_SCALE, D3)
   
   # map class data to pitch variation
   classVariation = mapScale(classData[i], classMinVal, classMaxVal, 0, 24)
   
   # map class data to dynamic
   classDynamic = mapValue(classData[i], classMinVal, classMaxVal, 0, 127)
   
   # creating duration using values from class data
   if classData[i] == 1.0:
      classDuration = EN
   elif classData[i] == 2.0:
      classDuration = QN
   else:
      classDuration = HN

   # combining pitch and dynamic into a note
   classNote = Note(classPitch + classVariation, classDuration, classDynamic, genderData[i])
   
   # adding it to the melody
   classPhrase.addNote(classNote)
   
   ### creating a background sound 
   # setting piano notes 
   pianoNotes = [C4, CS4, DS4, E4, F4, FS4, G4, GS4, A4, AS4, B4]
   
   # setting a duration for the piano
   duration = [HN] * 11
   
   # creating a dynimic for the piano
   pianoDynamic = [P] * 11
   
   # adding the piano components to the melody
   pianoPhrase.addNoteList(pianoNotes, duration,pianoDynamic)
   
   # moving to the next value in the data
   i = i + 1
   
# everything is now sonified, almost there 

### combining everything
pianoPart.addPhrase(pianoPhrase)
classPart.addPhrase(classPhrase)         
survivalPart.addPhrase(survivalPhrase)      
titanicScore.addPart(classPart)           
titanicScore.addPart(survivalPart) 
titanicScore.addPart(pianoPart)      

# play time
Play.midi(titanicScore)
