# Data_Summaries

# Exploring Student Data

Imagine that you work for a school district and have collected some data on local students and their parents. You’ve been tasked with answering some important questions:

How are students performing in their math classes?
What do students’ parents do for work?
How often are students absent from school?
In this project, you’ll explore and summarize some student data in order to answer these questions.

Data citation:

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. http://archive.ics.uci.edu/ml/datasets/Student+Performance

Paulo Cortez, University of Minho, Guimarães, Portugal, http://www3.dsi.uminho.pt/pcortez

Tasks

Initial exploration
1.

The provided dataframe (saved as students) includes the following variables/features:

address: the location of the student’s home ('U' for urban and 'R' for rural)
absences: the number of times the student was absent during the school year
Mjob: the student’s mother’s job industry
Fjob: the student’s father’s job industry
math_grade: the student’s final grade in math, ranging from 0 to 20
Use the pandas .head() method to inspect the first few rows of data.



2.
Use the pandas .describe() method to print out summary statistics for all five features in the dataset. Inspect the output. Do more students live in urban or rural locations?



Summarize a typical student grade
3.
Let’s start by trying to summarize the math_grade column. Calculate and print the mean value of math_grade.


4.
Next, calculate and print the median value of math_grade. Compare this value to the mean. Is it smaller? larger?



5.
Finally, calculate and print the mode of the math_grade column. What is the most common grade earned by students in this dataset? How different is this number from the mean and median?



Summarize the spread of student grades
6.
Next, let’s summarize the spread of student grades. Calculate and print the range of the math_grade column.



7.
Calculate and print the standard deviation of the math_grade column. About two thirds of values fall within one standard deviation of the mean. What does this number tell you about how much math grades vary?



8.
Finally, calculate the mean absolute deviation of the math_grade column. This is the mean difference between each students’s score and the average score.



Visualize the distribution of student grades

9.

Now that we’ve summarized student grades using statistics for central tendency and spread, let’s visualize the distribution using a histogram. Use the seaborn histplot() function to create a histogram of math_grade.

Note that we’ve provided code to show and clear each plot using:

plt.show()
plt.clf()
This ensures that the plots don’t get layered on top of each other. Make sure that you add your code to call sns.histplot() above plt.show().



10.
Another way to visualize the distribution of a quantitative variable is using a box plot. Use the seaborn boxplot() function to create a boxplot of math_grade.

Make sure to add this code after the first call to plt.clf() from the above plot and before the second call to plt.show().

Summarize mothers' jobs

11.
The Mjob column in the dataset contains information about what the students mothers do as a profession. Summarize the Mjob column by printing the number of students who have mothers with each job type.

Which value of Mjob is most common?



12.
Now, calculate and print the proportion of students who have mothers with each job type. What proportion of students have mothers who work in health?


Visualize the distribution of mothers' jobs
13.
Now that we’ve used summary statistics to understand the relative frequencies of different mothers’ jobs, let’s visualize the same information with a bar chart. Use the seaborn countplot() function to create a bar chart of the Mjob variable.



14.

We can also visualize the same information using a pie chart. Create a pie chart of the Mjob column.
