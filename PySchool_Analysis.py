#!/usr/bin/env python
# coding: utf-8

# ### Import required dependencies

# In[25]:


import pandas as pd
import os


# ## Deliverable 1: Collect the Data
# 
# To collect the data that you’ll need, complete the following steps:
# 
# 1. Using the Pandas `read_csv` function and the `os` module, import the data from the `new_full_student_data.csv` file, and create a DataFrame called student_df. 
# 
# 2. Use the head function to confirm that Pandas properly imported the data.
# 

# In[29]:


# Create the path and import the data

# set the path for the source file. 
full_student_data = os.path.join('../Resources/new_full_student_data.csv')

# read the source file into a data frame 
student_df = pd.read_csv(full_student_data)

# count of total number of records 
student_df.count()


# In[27]:


# Verify that the data was properly imported

#use head() function to read first 5 records of dataset to validate it read in correctly. 
student_df.head()


# ## Deliverable 2: Prepare the Data
# 
# To prepare and clean your data for analysis, complete the following steps:
#     
# 1. Check for and remove all rows with `NaN`, or missing, values in the student DataFrame. 
# 
# 2. Check for and remove all duplicate rows in the student DataFrame.
# 
# 3. Use the `str.replace` function to remove the "th" from the grade levels in the grade column.
# 
# 4. Check data types using the `dtypes` property.
# 
# 5. Remove the "th" suffix from every value in the grade column using `str` and `replace`.
# 
# 6. Change the grade colum to the `int` type and verify column types.
# 
# 7. Use the head (and/or the tail) function to preview the DataFrame.

# In[28]:


# Check for null values

#use .isnull() to identify null values and .sum() to count records
student_df.isnull().sum()


# In[30]:


# Drop rows with null values and verify removal

#drops records with null columns and casts to new dataframe
student_df_nonull = student_df.dropna()

#validates nulls have been removed 
student_df_nonull.isnull().sum() 


# In[59]:


student_df_nonull.count()


# In[6]:


# Check for duplicated rows

#use .duplicated() to identify and .sum() to count the number of duplicated rows.  
student_df_nonull.duplicated().sum()


# In[7]:


# Drop duplicated rows and verify removal

#use .drop_duplicates() to drop duplicate records and cast to new data frame. 
student_df_nodupes=student_df_nonull.drop_duplicates()

#validate that duplicates have been removed 
student_df_nodupes.duplicated().sum()


# In[8]:


# Check data types

#use .dtypes to check for the types of data in each column 
student_df_nodupes.dtypes


# In[9]:


# Examine the grade column to understand why it is not an int
student_df_nodupes['grade'] #it has alphanumerics in the column - not just numbers - cannot be converted to an int. 


# In[10]:


#cast a copy to new dataframe to preserve nodupes
student_df_noth = student_df_nodupes.copy()
student_df_noth


# In[31]:


# Remove the non-numeric characters and verify the contents of the column
#note - there is a warning on this code if a .copy() is NOT used in the above statement 
#use .str.replace() to remove th from the grade column. 
student_df_noth['grade'] = student_df_noth['grade'].str.replace('th', '')
student_df_noth


# In[12]:


# Change the grade column to the int type and verify column types
# copy to a new dataframe to preserve previous data frame. 
clean_student_df = student_df_noth.copy() 
# use astype(int) to convert grade from str to int. 
clean_student_df['grade'] = clean_student_df['grade'].astype(int)
clean_student_df.dtypes



# ## Deliverable 3: Summarize the Data
# 
# Describe the data using summary statistics on the data as a whole and on individual columns.
# 
# 1. Generate the summary statistics for each DataFrame by using the `describe` function.
# 
# 2. Display the mean math score using the `mean` function. 
# 
# 2. Store the minimum reading score as `min_reading_score`.

# In[13]:


# Display summary statistics for the DataFrame

#use .describe() to show summary statistics for Dataframe 
clean_student_df.describe()


# In[33]:


# Display the mean math score using the mean function

#use mean to determine the mean math score. 
clean_student_df["math_score"].mean()


# In[15]:


# Store the minimum reading score as min_reading_score

#use .min() to determine the minimum readingscore. 
min_reading_score = clean_student_df["reading_score"].min()
min_reading_score


# ## Deliverable 4: Drill Down into the Data
# 
# Drill down to specific rows, columns, and subsets of the data.
# 
# To drill down into the data, complete the following steps:
# 
# 1. Use `loc` to display the grade column.
# 
# 2. Use `iloc` to display the first 3 rows and columns 3, 4, and 5.
# 
# 3. Show the rows for grade nine using `loc`.
# 
# 4. Store the row with the minimum overall reading score as `min_reading_row` using `loc` and the `min_reading_score` found in Deliverable 3.
# 
# 5. Find the reading scores for the school and grade from the output of step three using `loc` with multiple conditional statements.
# 
# 6. Using conditional statements and `loc` or `iloc`, find the mean reading score for all students in grades 11 and 12 combined.

# In[16]:


# Use loc to display the grade column
#clarification on structure from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html?highlight=loc
#use .loc to show all records in the Grade column. 
grade_data_df = clean_student_df.loc[:,'grade']
grade_data_df 


# In[17]:


# Use `iloc` to display the first 3 rows and columns 3, 4, and 5.

#use .iloc to select specific columns and rows for display. 
selected_clean_student_df = clean_student_df.iloc[0:3, 2:5]
selected_clean_student_df 


# In[18]:


# Select the rows for grade nine and display their summary statistics using `loc` and `describe`.

#select all grade 9 records 
grade_nine = clean_student_df.loc[clean_student_df["grade"]==9]

#use .describe() to show grade 9 details. 
grade_nine.describe()


# In[19]:


# Store the row with the minimum overall reading score as `min_reading_row`
# using `loc` and the `min_reading_score` found in Deliverable 3.

#min_reading_score = clean_student_df["reading_score"].min()
min_reading_row = clean_student_df.loc[clean_student_df["reading_score"]==min_reading_score]

min_reading_row




# In[20]:


# Use loc with conditionals to select all reading scores from 10th graders at Dixon High School.

# use .loc with conditionals to filter grade 10 and Dixon highschool. 
Dixon_10 = clean_student_df.loc[(clean_student_df["grade"] == 10) & (clean_student_df["school_name"] == "Dixon High School")]

# use .loc to show all reading scores from above filter. (cast to new df)
Dixon_reading_10 = Dixon_10.loc[:,["reading_score"]]

Dixon_reading_10


# In[21]:


# Find the mean reading score for all students in grades 11 and 12 combined.

all_11_12 = clean_student_df.loc[(clean_student_df["grade"] > 10)]
reading_11_12 =all_11_12.loc[:,["reading_score"]]
reading_11_12.mean()

#note - calcuation here (74.900381) does not match what is in the original display below from the starter code (63.29)


# ## Deliverable 5: Make Comparisons Between District and Charter Schools
# 
# Compare district vs charter schools for budget, size, and scores.
# 
# Make comparisons within your data by completing the following steps:
# 
# 1. Using the `groupby` and `mean` functions, look at the average reading and math scores per school type.
# 
# 1. Using the `groupby` and `count` functions, find the total number of students at each school.
# 
# 2. Using the `groupby` and `mean` functions, find the average budget per grade for each school type.

# In[22]:


# Use groupby and mean to find the average reading and math scores for each school type.

#create a new df that includes the mean reading and math scores grouped by school types 
average_reading_math = clean_student_df.groupby(["school_type"]).mean().copy()

#use .loc to display reading and math score averages 
average_reading_math_report = average_reading_math.loc[:,["reading_score", "math_score"]]
average_reading_math_report


# In[23]:


# Use the `groupby`, `count`, and `sort_values` functions to find the
# total number of students at each school and sort from most students to least students.

#group by school_name 
student_demo = clean_student_df.groupby(["school_name"]).count().copy()

#rename student ID column to student count to identify count of records. 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html
student_demo_sort = student_demo.rename(columns = {"student_id":"student_count"}).copy()

#sort descending student count 
student_demo_filter = student_demo_sort.sort_values("student_count", ascending=False)

#create DF with just student count 
student_demo_final = student_demo_filter.loc[:,["student_count"]]

student_demo_final



# In[48]:


#no text in this block,am assuming the task is to determine the average math score for grade between school types 

#group by school type and grade 
School_type = clean_student_df.groupby(["school_type", "grade"]).mean().copy()

#copy to a new dataframe 
School_type_math = School_type.copy()

#select only the average math scores to display 
School_type_math_final = School_type_math.loc[:,["math_score"]]

#format to display 2 decimal points
display_school_type_math = School_type_math_final.round(2)

display_school_type_math


# In[40]:


#the instructions in the module had additional requirements regarding school budgets.  Those requirements are addressed below: 

#display average budget for each school type by
#group by school type 
school_budgets = clean_student_df.groupby(["school_type"]).mean()
#select ONLY school_budget 
school_budgets_final = school_budgets[("school_budget")]
#display School_budgets
school_budgets_final


# In[50]:


#find the total number of students at each school - sort from largest to smallest (this was done above - commented here for reference) 

# Use the `groupby`, `count`, and `sort_values` functions to find the
# total number of students at each school and sort from most students to least students.

#group by school_name 
#student_demo = clean_student_df.groupby(["school_name"]).count().copy()

#rename student ID column to student count to identify count of records. 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html
#student_demo_sort = student_demo.rename(columns = {"student_id":"student_count"}).copy()

#sort descending student count 
#student_demo_filter = student_demo_sort.sort_values("student_count", ascending=False)

#create DF with just student count 
#student_demo_final = student_demo_filter.loc[:,["student_count"]]

student_demo_final


# In[51]:


#find the average math score for each school type by usingi groupby and mean 

# This was done above, commented here for reference 
# #group by school type and grade 
# School_type = clean_student_df.groupby(["school_type", "grade"]).mean().copy()

# #copy to a new dataframe 
# School_type_math = School_type.copy()

# #select only the average math scores to display 
# School_type_math_final = School_type_math.loc[:,["math_score"]]

# #format to display 2 decimal points
# display_school_type_math = School_type_math_final.round(2)

display_school_type_math


# # Deliverable 6: Summarize Your Findings
# In the cell below, write a few sentences to describe any discoveries you made while performing your analysis along with any additional analysis you believe would be worthwhile.

# # Data Cleanup
# 
# The source file read in with a total of 19514 records.  Once data review and cleanup was completed, 14831 records remained.  The following cleanup was done: 
# 
#     *  1968 records had a NaN for a reading_score
#     *  982 records had a NaN for a math_score.  
#     
# 14.6% of the original records were removed due to missing data, resulting in 16667 records being available for the next step in processing.  After reviewing for duplicates, 11.0% of the records were removed, leaving a total number of 14831 records for analysis.  This is a fairly substantial number of records that are excluded from the reporting, and it is recommended that the data is reviewed for completion and accuracy prior to any future analysis being done. 
# 
# # Data Review 
# The initial review only looked at 5 of the records that were loaded in (head()).  It showed that data did load correctly, however, was a small sampling that did not show the true number of records that could possibly be impacted by cleanup activities.  When running the head() statement using head(15), you did see a more descriptive picture of the data in the dataset.  For larger datasets, I would recommend using a larger head() or tail() definition to see more of the data to determine if records should be removed, or missing data should be replaced in order to provide more accurate reporting and analysis. 
# 
# Part of the activities involved converting the grade column from a string to an integer value.  While not strictly a necessary effort, having the value as an integer does make it easier to filter on values that are greater than 10 when you want to just see data related to 11th and 12th grade students. 
# 
# The lowest reading score for this data set was 10.5 and the lowest math score for the data set was 3.7.  The highest score for both was 100.0
# 
# # Data Drill Down 
# The first step was to drill down to grade 9 and obtain a high level description of the data for this subset of records.   The lowest reading score for this subset was 17.9, and the lowest math score was 5.3.  Both of these are above the minimum values for the overall data set, but are still concerning. 
# 
# Next, we were asked to pull the reading score for 11th and 12th year students and determine the mean of those scores.  This was 74.9.  Note, the original starter code indicated the result should be 63.25853039200117.  However, after multiple permutations of code, I was not able to reach this target number.  (I think it may be inaccurate, but am not certain)  The code as it is currently written returns a value of 74.900381 for reading scores for 11th and 12th year students.  
# ~~~
# all_11_12 = clean_student_df.loc[(clean_student_df["grade"] > 10)]
# reading_11_12 =all_11_12.loc[:,["reading_score"]]
# reading_11_12.mean()
# ~~~
# 
# # Data Comparisons 
# Breaking out the school types (Public vs Charter) shows fairly close average scores for reading scores (72.281 vs 72.450) and lower performance on math scores for public schools when compared to charter (62.951 vs 66.762).  
# 
# Breaking test results out by grade shows a similar distribution, with charter schools performing better for both test types in all grade levels.  
# 
# It is of note that the budget for public schools is higher than that for charter schools  911195.56 vs 872625.66.  This may be due to larger student populations in public schools.  However, additional analysis could be done to assess per capita expenditure per student and relate that to the scores that each type of school returns.  This could be a starting point for deeper analysis into how schools invest in student education results in improved test scores.  
# 

# In[ ]:




