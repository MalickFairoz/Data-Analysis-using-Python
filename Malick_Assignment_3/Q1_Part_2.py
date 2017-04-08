
# coding: utf-8

# # Python Assignment - 3

# # Question 1_Part_2   - NYC VEHICLE COLLISION ANALYSIS

# In[14]:

# Importing the Packages 
import csv
import pandas as pd
from pandas import DataFrame


# In[15]:

# To read the CSV file and to find the keys from the CSV file 
datafile = pd.read_csv('Data/vehicle_collisions.csv')
print(datafile.keys())


# In[17]:

#Extracting the month and year from the column DATE and stored it in a seperate column of 'datafile' 
#'MONTH' and 'YEAR' respectively

datafile['YEAR'] = pd.DatetimeIndex(datafile['DATE']).year
datafile['MONTH'] = pd.DatetimeIndex(datafile['DATE']).month


# In[18]:

# Extracting the data occured in 2015 and later then stored in "datafile_year"

datafile_year = datafile.loc[datafile['YEAR'] >= 2015]


# In[19]:

# For Column 'VEHICLE 1 TYPE'
# Convert the data to string 1 and replacing the NaN as 0 and then changing the datatype as interger 
datafile_year['VEHICLE 1 TYPE'] = datafile_year['VEHICLE 1 TYPE'].str.replace('.*', '1')
datafile_year['VEHICLE 1 TYPE'] = datafile_year['VEHICLE 1 TYPE'].fillna(0)
datafile_year['VEHICLE 1 TYPE'] = datafile_year['VEHICLE 1 TYPE'].astype(int)
print(datafile_year['VEHICLE 1 TYPE'].count())


# In[20]:

# For Column 'VEHICLE 2 TYPE'
# Convert the data to string 1 and replacing the NaN as 0 and then changing the datatype as interger 
datafile_year['VEHICLE 2 TYPE'] = datafile_year['VEHICLE 2 TYPE'].str.replace('.*', '1')
datafile_year['VEHICLE 2 TYPE'] = datafile_year['VEHICLE 2 TYPE'].fillna(0)
datafile_year['VEHICLE 2 TYPE'] = datafile_year['VEHICLE 2 TYPE'].astype(int)
print(datafile_year['VEHICLE 2 TYPE'].count())


# In[21]:

# For Column 'VEHICLE 3 TYPE'
# Convert the data to string 1 and replacing the NaN as 0 and then changing the datatype as interger 
datafile_year['VEHICLE 3 TYPE'] = datafile_year['VEHICLE 3 TYPE'].str.replace('.*', '1')
datafile_year['VEHICLE 3 TYPE'] = datafile_year['VEHICLE 3 TYPE'].fillna(0)
datafile_year['VEHICLE 3 TYPE'] = datafile_year['VEHICLE 3 TYPE'].astype(int)
print(datafile_year['VEHICLE 3 TYPE'].count())


# In[22]:

# For Column 'VEHICLE 4 TYPE'
# Convert the data to string 1 and replacing the NaN as 0 and then changing the datatype as interger 
datafile_year['VEHICLE 4 TYPE'] = datafile_year['VEHICLE 4 TYPE'].str.replace('.*', '1')
datafile_year['VEHICLE 4 TYPE'] = datafile_year['VEHICLE 4 TYPE'].fillna(0)
datafile_year['VEHICLE 4 TYPE'] = datafile_year['VEHICLE 4 TYPE'].astype(int)
print(datafile_year['VEHICLE 4 TYPE'].count())


# In[23]:

# For Column 'VEHICLE 5 TYPE'
# Convert the data to string 1 and replacing the NaN as 0 and then changing the datatype as interger 
datafile_year['VEHICLE 5 TYPE'] = datafile_year['VEHICLE 5 TYPE'].str.replace('.*', '1')
datafile_year['VEHICLE 5 TYPE'] = datafile_year['VEHICLE 5 TYPE'].fillna(0)
datafile_year['VEHICLE 5 TYPE'] = datafile_year['VEHICLE 5 TYPE'].astype(int)
print(datafile_year['VEHICLE 5 TYPE'].count())


# In[24]:

# Adding all the vehicle type to identify the overall collision scale and stored in column "COLLISION_INVOLVED_VEHICLE"
datafile_year['COLLISION_INVOLVED_VEHICLE'] = datafile_year['VEHICLE 1 TYPE'] + datafile_year['VEHICLE 2 TYPE'] + datafile_year['VEHICLE 3 TYPE'] + datafile_year['VEHICLE 4 TYPE'] + datafile_year['VEHICLE 5 TYPE']  


# In[25]:

# Grouped by the column "BOROUGH" and "COLLISION_INVOLVED_VEHICLE" 
datafile_grouped = datafile_year.groupby(['BOROUGH', 'COLLISION_INVOLVED_VEHICLE']).count().reset_index()


# In[26]:

# Creating a pivot table and filled 0 in place of NaN
datafile_pivot = datafile_grouped.pivot(index='BOROUGH',columns='COLLISION_INVOLVED_VEHICLE', values='UNIQUE KEY').fillna(0)


# In[27]:

# Changing the column name as per requirement
datafile_pivot.columns = ['ZERO','ONE_VEHICLE_INVOLVED','TWO_VEHICLE_INVOLVED','THREE_VEHICLE_INVOLVED','FOUR_VEHICLE_INVOLVED','FIVE_VEHICLE_INVOLVED']


# In[28]:

# Reseting the index and stored it in "datafile_final_output"
datafile_final_output = datafile_pivot.reset_index()


# In[29]:

# Adding the "FOUR_VEHICLE_INVOLVED" and "FIVE_VEHICLE_INVOLVED" to form "MORE_VEHICLE_INVOLVED"
datafile_final_output['MORE_VEHICLE_INVOLVED'] = datafile_final_output['FOUR_VEHICLE_INVOLVED'] + datafile_final_output['FIVE_VEHICLE_INVOLVED']


# In[30]:

# After adding the last two data column into a new column "MORE_VEHICLE_INVOLVED" it can be deleted 
del datafile_final_output['FOUR_VEHICLE_INVOLVED']
del datafile_final_output['FIVE_VEHICLE_INVOLVED']
del datafile_final_output['ZERO']


# In[31]:

# Final output is displayed here
print(datafile_final_output.head())


# In[32]:

# Writing the output to a CSV file "Q1P2.csv"
import os
if not os.path.exists('Output/Q1/Part2'):
        os.makedirs('Output/Q1/Part2')
datafile_final_output.to_csv('Output/Q1/Part2/Q1P2.csv', index=False)

