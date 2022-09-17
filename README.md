# school_district_analysis
PySchool Analysis 

# Data Cleanup

The source file read in with a total of 19514 records.  Once data review and cleanup was completed, 14831 records remained.  The following cleanup was done: 

    *  1968 records had a NaN for a reading_score
    *  982 records had a NaN for a math_score.  
    
14.6% of the original records were removed due to missing data, resulting in 16667 records being available for the next step in processing.  After reviewing for duplicates, 11.0% of the records were removed, leaving a total number of 14831 records for analysis.  This is a fairly substantial number of records that are excluded from the reporting, and it is recommended that the data is reviewed for completion and accuracy prior to any future analysis being done. 

# Data Review 
The initial review only looked at 5 of the records that were loaded in (head()).  It showed that data did load correctly, however, was a small sampling that did not show the true number of records that could possibly be impacted by cleanup activities.  When running the head() statement using head(15), you did see a more descriptive picture of the data in the dataset.  For larger datasets, I would recommend using a larger head() or tail() definition to see more of the data to determine if records should be removed, or missing data should be replaced in order to provide more accurate reporting and analysis. 

Part of the activities involved converting the grade column from a string to an integer value.  While not strictly a necessary effort, having the value as an integer does make it easier to filter on values that are greater than 10 when you want to just see data related to 11th and 12th grade students. 

The lowest reading score for this data set was 10.5 and the lowest math score for the data set was 3.7.  The highest score for both was 100.0

# Data Drill Down 
The first step was to drill down to grade 9 and obtain a high level description of the data for this subset of records.   The lowest reading score for this subset was 17.9, and the lowest math score was 5.3.  Both of these are above the minimum values for the overall data set, but are still concerning. 

Next, we were asked to pull the reading score for 11th and 12th year students and determine the mean of those scores.  This was 74.9.  Note, the original starter code indicated the result should be 63.25853039200117.  However, after multiple permutations of code, I was not able to reach this target number.  (I think it may be inaccurate, but am not certain)  The code as it is currently written returns a value of 74.900381 for reading scores for 11th and 12th year students.  
~~~
all_11_12 = clean_student_df.loc[(clean_student_df["grade"] > 10)]
reading_11_12 =all_11_12.loc[:,["reading_score"]]
reading_11_12.mean()
~~~

# Data Comparisons 
Breaking out the school types (Public vs Charter) shows fairly close average scores for reading scores (72.281 vs 72.450) and lower performance on math scores for public schools when compared to charter (62.951 vs 66.762).  

Breaking test results out by grade shows a similar distribution, with charter schools performing better for both test types in all grade levels.  

It is of note that the budget for public schools is higher than that for charter schools  911195.56 vs 872625.66.  This may be due to larger student populations in public schools.  However, additional analysis could be done to assess per capita expenditure per student and relate that to the scores that each type of school returns.  This could be a starting point for deeper analysis into how schools invest in student education results in improved test scores.  
