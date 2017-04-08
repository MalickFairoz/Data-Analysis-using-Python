
# coding: utf-8

# # Python Assignment - 3

# # Question 2_Part_2   - EMPLOYEE COMPENSATION ANALYSIS

# In[1]:

# Importing the Packages 
import csv
import pandas as pd
from pandas import DataFrame


# In[3]:

# To read the CSV file and to find the keys from the CSV file 
datafilePartB = pd.read_csv('Data/employee_compensation.csv')
print(datafilePartB.keys())


# In[4]:

# Filtering the column "Year Type" only to Calender
datafileParB_calenderyear = datafilePartB.loc[datafilePartB['Year Type'] == 'Calendar']


# In[5]:

# Filtering the other columns and using only the required columns by storing it in "datafileParB_fillercolumn"
datafileParB_fillercolumn = datafileParB_calenderyear[['Job Family', 'Employee Identifier', 'Salaries', 'Overtime', 'Other Salaries',
       'Total Salary', 'Retirement', 'Health/Dental', 'Other Benefits',
       'Total Benefits', 'Total Compensation' ]]


# In[6]:

# Grouping the "Employee Identifier" and taking the mean value on all salary columns
datafileParB_avgmean = datafileParB_fillercolumn.groupby(['Employee Identifier'])['Salaries', 'Overtime', 'Other Salaries',
       'Total Salary', 'Retirement', 'Health/Dental', 'Other Benefits',
       'Total Benefits', 'Total Compensation'].mean()


# In[7]:

# Filtering the employees who have received overtime salary more than 5% than regular salary
datafileParB_overtime = (datafileParB_avgmean.loc[datafileParB_avgmean['Overtime'] 
                                                  > (5/100)*datafileParB_avgmean['Salaries']]).reset_index()    


# In[8]:

#Filtering the columns 'Job Family', 'Employee Identifier' and removed duplicates
datafileParB_fillercolumnfamily = datafileParB_fillercolumn[['Job Family', 'Employee Identifier']].drop_duplicates()


# In[9]:

# Joining the family data with processed salary data
datafileParB_join = pd.merge(datafileParB_fillercolumnfamily,datafileParB_overtime, on = 'Employee Identifier' )


# In[10]:

# Grouping the "Job Family" and taking the mean value on 'Total Benefits' and 'Total Compensation'
datafileParB_familygroup = datafileParB_join.groupby(['Job Family'])['Total Benefits','Total Compensation'].mean()


# In[11]:

# Taking the percentage on total benifits to the Total compensation and storing it in the column "Percent_Total_Benifit"
datafileParB_familygroup['Percent_Total_Benifit'] = (datafileParB_familygroup['Total Benefits']
                                                     /datafileParB_familygroup['Total Compensation'])*100     


# In[12]:

# Sorting the percentage value from max to min and stored in datafileParB_finaloutput
datafileParB_finaloutput = datafileParB_familygroup.sort_values('Percent_Total_Benifit',ascending=[False])


# In[13]:

# Final Output is displayed
datafileParB_finaloutput.head()


# In[14]:

# Writing the output to a CSV file "Q2P2.csv"
import os
if not os.path.exists('Output/Q2/Part2'):
        os.makedirs('Output/Q2/Part2')
datafileParB_finaloutput.to_csv('Output/Q2/Part2/Q2P2.csv')


# In[ ]:



