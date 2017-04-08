
# coding: utf-8

# # Python Assignment - 3

# # Question 3_Part_1   -  Cricket Matches Analysis

# In[1]:

# Importing the Packages 
import csv
import pandas as pd
from pandas import DataFrame


# In[2]:

# To read the CSV file and to find the keys from the CSV file 
datafile = pd.read_csv('Data/cricket_matches.csv')
print(datafile.keys())


# In[3]:

# Taking the host team who have won the game
datafile_hostwinner = datafile.loc[datafile['home'] == datafile['winner']]


# In[4]:

# Taking the host team who have won the match in first innings
datafile_hostwinner_ING1 = datafile_hostwinner.loc[datafile_hostwinner['home'] == datafile_hostwinner['innings1']]


# In[5]:

# Taking the host team and thier score who have won the match in first innings
datafile_hostwinner_ING1 = datafile_hostwinner_ING1[['home','innings1_runs']]


# In[6]:

# Remaing the columns as required 
datafile_hostwinner_ING1.columns = ['home','score']


# In[7]:

# Taking the host team who have won the match in second innings
datafile_hostwinner_ING2 = datafile_hostwinner.loc[datafile_hostwinner['home'] == datafile_hostwinner['innings2']]


# In[8]:

# Taking the host team and thier score who have won the match in second innings
datafile_hostwinner_ING2 = datafile_hostwinner_ING2[['home','innings2_runs']]


# In[9]:

# Remaing the columns as required 
datafile_hostwinner_ING2.columns = ['home','score']


# In[10]:

# Making the output from first and second innings into frame
frames = [datafile_hostwinner_ING1,datafile_hostwinner_ING2]


# In[11]:

# Joining both first and second inning score 
datafile_hostwinner_combine = pd.concat(frames)


# In[12]:

# Goruping the team and getting the average value of score 
datafile_hostwinner_average = datafile_hostwinner_combine.groupby(['home'])['score'].mean().reset_index()


# In[13]:

#Print the output with first five records
datafile_hostwinner_average.head()


# In[14]:

# Writing the output to a CSV file "Q3P1.csv"
import os
if not os.path.exists('Output/Q3/Part1'):
        os.makedirs('Output/Q3/Part1')
datafile_hostwinner_average.to_csv('Output/Q3/Part1/Q3P1.csv', index = True)

