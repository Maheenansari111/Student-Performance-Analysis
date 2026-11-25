import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')

# NUMPY - All Calculations

# 1. Mean, Median, Min, Max, Standard Deviation for Math
print("Math Mean:", np.mean(df['math score']))
print("Math Median:", np.median(df['math score']))
print("Math Max:", np.max(df['math score']))
print("Math Min:", np.min(df['math score']))
print("Math Standard Deviation:", np.std(df['math score']))

# 2. Mean for Reading and Writing
print("Reading Mean:", np.mean(df['reading score']))
print("Writing Mean:", np.mean(df['writing score']))

# 3. Total and Average using Numpy
df['total'] = np.add(np.add(df['math score'], df['reading score']), df['writing score'])
df['average'] = np.divide(df['total'], 3)
print(df[['math score', 'reading score', 'writing score', 'total', 'average']].head())

# 4. Numpy Array - First 10 Math Marks
marks_array = np.array(df['math score'])
print("First 10 Marks Array:", marks_array[:10])

# 5. Pass / Fail using np.where
df['result'] = np.where(df['average'] >= 50, 'Pass', 'Fail')
print(df[['average', 'result']].head(10))
print(df['result'].value_counts())

# 6. Highest Total Marks Student
print("Highest Total Marks:", np.max(df['total']))
print(df[df['total'] == np.max(df['total'])])