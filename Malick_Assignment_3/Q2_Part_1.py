
# coding: utf-8

# # Python Assignment - 3

# # Question 2_Part_1   - EMPLOYEE COMPENSATION ANALYSIS

# In[1]:

# Importing the Packages 
import csv
import pandas as pd
from pandas import DataFrame


# In[2]:

# To read the CSV file and to find the keys from the CSV file 
datafile = pd.read_csv('Data/employee_compensation.csv')
print(datafile.keys())


# In[3]:

# Filtering the other columns and using only the required columns by storing it in "datafile_filter"
datafile_filter = datafile[['Organization Group', 'Department', 'Total Compensation' ]]


# In[4]:

# Grouping the columns "Organization Group, Department" and taking the mean on column "Total Compensation"
datafile_mean = pd.DataFrame(datafile_filter.groupby(['Organization Group', 'Department'])['Total Compensation'].mean())


# In[5]:

# To sort the Total compensation from max to min and then grouping again 
datafile_sorting = datafile_mean['Total Compensation'].groupby(level=0, group_keys=False)


# In[6]:

# converting it to DataFrame
datafile_final_output = pd.DataFrame(datafile_sorting.nlargest())


# In[7]:

# Final output in with first 5 records
datafile_final_output.head()


# In[8]:

# Writing the output to a CSV file "Q2P1.csv"
import os
if not os.path.exists('Output/Q2/Part1'):
        os.makedirs('Output/Q2/Part1')
datafile_final_output.to_csv('Output/Q2/Part1/Q2P1.csv')

