
# coding: utf-8

# # Python Assignment - 3

# # Question 1_Part_1   - NYC VEHICLE COLLISION ANALYSIS

# In[1]:

# Importing the Packages 
import csv
import pandas as pd
from pandas import DataFrame


# In[2]:

# To read the CSV file and to find the keys from the CSV file 
datafile = pd.read_csv('Data/vehicle_collisions.csv')
print(datafile.keys())


# In[3]:

#Extracting the month and year from the column DATE and stored it in a seperate column of 'datafile' 
#'MONTH' and 'YEAR' respectively

datafile['YEAR'] = pd.DatetimeIndex(datafile['DATE']).year
datafile['MONTH'] = pd.DatetimeIndex(datafile['DATE']).month


# In[4]:

# Extracting the data occured only in the year 2016 and stored in "datafile_NYC"

datafile_NYC = datafile.loc[datafile['YEAR'] == 2016]


# In[5]:

# Grouping and counting the data under the column 'Month' for NYC data

datafile_NYC_Month = datafile_NYC.groupby( ["MONTH"] ).count()


# In[6]:

# Extracting the data occured only in the year 2016 and stored in "datafile_MAN"

datafile_MAN = datafile_NYC.loc[datafile['BOROUGH'] == 'MANHATTAN']


# In[7]:

# Grouping and counting the data under the column 'MONTH'

datafile_MAN_Month = datafile_MAN.groupby( ["MONTH"] ).count()


# In[8]:

# concatinating the collision record from both NYC and Manhattan for calculation using the unique key column
datafile_MAN_NYC = pd.concat([datafile_MAN_Month['UNIQUE KEY'], datafile_NYC_Month['UNIQUE KEY']], axis=1)


# In[9]:

# Changing the column names as reqired
datafile_MAN_NYC.columns=['MANHATTAN','NYC']


# In[10]:

# Calculating the percentage of the MANHATTAN data to the total NYC data and stored it in a seperate column "PERCENTAGE"
datafile_MAN_NYC['PERCENTAGE'] = datafile_MAN_NYC['MANHATTAN']/datafile_MAN_NYC['NYC']


# In[11]:

# To provide the output more ligible the month name is added in a data
monthdata = pd.DataFrame({'MONTH':['NaN','Jan','Feb','Mar','Apl','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']})


# In[12]:

Final_Output = pd.concat([monthdata['MONTH'], datafile_MAN_NYC['MANHATTAN'],datafile_MAN_NYC['NYC'],
                          datafile_MAN_NYC['PERCENTAGE']], axis=1)


# In[13]:

# Removing the first row of the dataframe "Final_Output"
if(Final_Output.index[0]==0):
    Final_Output = Final_Output.drop(Final_Output.index[[0,0]])


# In[14]:

# Displaying the final output
print(Final_Output.head())


# In[15]:

# Writing the output to a CSV file "Q1P1.csv"
import os
if not os.path.exists('Output/Q1/Part1'):
        os.makedirs('Output/Q1/Part1')
Final_Output.to_csv('Output/Q1/Part1/Q1P1.csv', index=False)

