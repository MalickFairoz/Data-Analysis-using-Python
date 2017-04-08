
# coding: utf-8

# # Python Assignment - 3

# # Question 4_Part_1   -  Movie Awards Analysis

# In[131]:

# Importing the Packages 
import csv
import pandas as pd
from pandas import DataFrame


# In[132]:

# To read the CSV file and to find the keys from the CSV file 
datafileQ4 = pd.read_csv('Data/movies_awards.csv')
print(datafileQ4.keys())


# In[133]:

# Extracting Awards column and droping the NaN values then resetting the index
datafile_movie = datafileQ4[['Awards']].dropna().reset_index()


# In[134]:

# Extracting Awards column
datafile_movieawards = datafile_movie[['Awards']]


# In[135]:

# created two columns for won and nomination and filling values based on the data from column "Awards"
datafile_movieawards['Awards_Won_Total']=datafile_movieawards['Awards'].str.extract('(\d+) win',expand = False).fillna(0).astype(int)
datafile_movieawards["Awards_Nominated_Total"]=datafile_movieawards["Awards"].str.extract('(\d+) nomination',expand = False).fillna(0).astype(int)


# In[136]:

# created four columns for nomination categories and filling values based on the data from column "Awards"
datafile_movieawards["Primetime_Awards_Nominated"]=datafile_movieawards["Awards"].str.extract('Nominated for (\d+) Primetime',expand = False).fillna(0).astype(int)
datafile_movieawards["Oscar_Awards_Nominated"]=datafile_movieawards["Awards"].str.extract('Nominated for (\d+) Oscar',expand = False).fillna(0).astype(int)
datafile_movieawards["Golden_Globe_Awards_Nominated"]=datafile_movieawards["Awards"].str.extract('Nominated for (\d+) Golden Globe',expand = False).fillna(0).astype(int)
datafile_movieawards["BAFTA Film_Awards_Nominated"]=datafile_movieawards["Awards"].str.extract('Nominated for (\d+) BAFTA Film',expand = False).fillna(0).astype(int)


# In[137]:

# created four columns for won categories and filling values based on the data from column "Awards"
datafile_movieawards["Primetime_Awards_Won"]=datafile_movieawards["Awards"].str.extract('Won (\d+) Primetime',expand = False).fillna(0).astype(int)
datafile_movieawards["Oscar_Awards_Won"]=datafile_movieawards["Awards"].str.extract('Won (\d+) Oscar',expand = False).fillna(0).astype(int)
datafile_movieawards["Golden Globe_Awards_Won"]=datafile_movieawards["Awards"].str.extract('Won (\d+) Golden Globe',expand = False).fillna(0).astype(int)
datafile_movieawards["BAFTA Film_Awards_Won"]=datafile_movieawards["Awards"].str.extract('Won (\d+) BAFTA Film',expand = False).fillna(0).astype(int)


# In[138]:

# As per the output the category values should be added to the columns "Awards_Won" and "Awards_Nominated" 
#which is the total won and total nomination
datafile_movieawards['Awards_Won_Total']=datafile_movieawards['Awards_Won_Total']+datafile_movieawards["Primetime_Awards_Won"]+datafile_movieawards["Oscar_Awards_Won"]+datafile_movieawards["Golden Globe_Awards_Won"]+datafile_movieawards["BAFTA Film_Awards_Won"]
datafile_movieawards["Awards_Nominated_Total"]=datafile_movieawards["Awards_Nominated_Total"]+datafile_movieawards["Primetime_Awards_Nominated"]+datafile_movieawards["Oscar_Awards_Nominated"]+datafile_movieawards["Golden_Globe_Awards_Nominated"]+datafile_movieawards["BAFTA Film_Awards_Nominated"]   


# In[139]:

# The final ouput is displayed with first 5 records
datafile_movieawards.head()


# In[140]:

# Writing the output to a CSV file "Q4P1.csv"
import os
if not os.path.exists('Output/Q4/Part1'):
        os.makedirs('Output/Q4/Part1')
datafile_movieawards.to_csv('Output/Q4/Part1/Q4P1.csv', index = True)


# In[ ]:



