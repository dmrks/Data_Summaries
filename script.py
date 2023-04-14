# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head(5))

# Print summary statistics for all columns
print(students.describe(include = "all"))

#Answer: More Students live in urban areasn because top = U

# Calculate mean = 10.415189873417722
print(students.math_grade.mean())

# Calculate median = 11.0

print(students.math_grade.median())

# Calculate mode = 10

print(students.math_grade.mode())

# Calculate range = 20

math_grade = students.math_grade.max()- students.math_grade.min()
print(math_grade)

# Calculate standard deviation =  Most Students are Earning Grade between AVG(10.41) - STD(4.48) and AVG(10.41) + STD(4.48) 

print(students.math_grade.std())

# Calculate MAD = 3.4289889440794745

print(students.math_grade.mad())

# Create a histogram of math grades
sns.histplot(x = "math_grade", data = students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x = "math_grade", data = students)

plt.show()
plt.clf()

# Calculate number of students with mothers in each job category = Other is the most common category

print(students.Mjob.value_counts())

# Calculate proportion of students with mothers in each job category // PropMothers in Health = 0.08607594936708861

print(students.Mjob.value_counts(normalize = True))

# Create bar chart of Mjob
sns.countplot(x = "Mjob", data = students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()