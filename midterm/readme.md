# DATA ANALYSIS USING PYTHON

# Introduction
- This read me file is presented for the midterm exam of the Data Analysis using Python
- There are 2 parts of question in this exam
- Each part has 3 types of Analysis including the data gathering and storing
- For the first question the data has been downloaded from the Enron scandal Summary zip file
- For the second question the data has been downloaded from the NYT API Documentation


# First Question

- The data is collected from the zip file which was downloaded from the provided link with the question. 
- This data is the collection of email which has been used for the Enron Scandal
- This data is structure in the hierarchy of folders for totally 150 person
- Initailly all the requeired libraries are imported
- The Data is scanned by folder by folder then gathered the required data like **From, To, Cc, Bcc, Subject, Date**
- These gathered data is stored in individual list
- With these data the 3 analyzation part of this question will be performed

### Analysis - 1

- To get a person's email ID which has been used to send the maximum number of emails to others 
- Along with that the top 10 frequency of emails received and sent has been collected
- This is performed by the email keyword **From, To, Cc, Bcc**
- The total count email from these key are gathered and equaly distributed based on their frequency using Frequency Distribution from NLTK
- Listing the top 10 high frequenced email for the above mentioned keywords
- Storing all the data together in one CSV file
- Form the top ten of the From keyword the most frequently sent email ID of the person is identified and given rank 1 position
- This is the output of the analysis_1 
