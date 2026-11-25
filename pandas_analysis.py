import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')

# 1. First 5 and Last 5 rows
print(df.head())
print(df.tail())

# 2. Shape, Columns, Data Types
print(df.shape)
print(df.columns)
print(df.dtypes)

# 3. Info and Describe - Complete Summary
print(df.info())
print(df.describe())

# 4. Check Null Values
print(df.isnull().sum())

# 5. Unique Values - How many types are there
print(df['gender'].unique())
print(df['gender'].value_counts())
print(df['race/ethnicity'].value_counts())
print(df['parental level of education'].value_counts())

# 6. Filtering - Show Only Female Students
print(df[df['gender'] == 'female'].head())

# 7. Filtering - Students with Math Score More Than 90
print(df[df['math score'] > 90])

# 8. Sorting - Highest Math Score on Top
print(df.sort_values(by='math score', ascending=False).head())

# 9. GroupBy - Average by Gender
print(df.groupby('gender').mean(numeric_only=True))

# 10. GroupBy - Benefit of Test Preparation Course
print(df.groupby('test preparation course').mean(numeric_only=True))

# 11. GroupBy - By Lunch Type
print(df.groupby('lunch').mean(numeric_only=True))

# 12. Create New Column - Total and Average
df['total'] = df['math score'] + df['reading score'] + df['writing score']
df['average'] = df['total'] / 3
print(df[['math score','reading score','writing score','total','average']].head())

# 13. Loc and Iloc - Data of One Student
print(df.loc[0])
print(df.iloc[0:5, 0:3])

# 14. Rename Columns
df = df.rename(columns={'math score':'Math', 'reading score':'Reading'})
print(df.columns)