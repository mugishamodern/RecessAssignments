# Assignment Nine: Data Analysis with Pandas
# AfricaCupOfNationsMatches.csv & Series Exercises
# Name: ______________________
# Date: ______________________

import pandas as pd
import numpy as np

print("\n--- SERIES SECTION ---")
# 1. Compare elements of two Pandas series
s1 = pd.Series([4, 65, 436, 3, 9])
s2 = pd.Series([7, 0, 3, 897, 9])
print("Element-wise comparison:")
print("Equal:", s1 == s2)
print("Greater:", s1 > s2)
print("Less:", s1 < s2)

# 2. Add, subtract, multiply, divide two Pandas series
s3 = pd.Series([2, 4, 6, 8, 14])
s4 = pd.Series([1, 3, 5, 7, 9])
print("\nAdd:", s3 + s4)
print("Subtract:", s3 - s4)
print("Multiply:", s3 * s4)
print("Divide:", s3 / s4)

# 3. Convert a dictionary to a Pandas series
dictionary1 = {'Josh': 24, 'Sam': 36, 'Peace': 19, 'Charles': 65, 'Tom': 44}
series_dict = pd.Series(dictionary1)
print("\nDictionary to Series:")
print(series_dict)

# 4. Convert a given series to an array
s5 = pd.Series(['Love', 800, 'Joy', 789.9, 'Peace', True])
arr = s5.values
print("\nSeries to array:", arr)

# 5. Most frequent value in 'HomeTeamGoals' and replace others as 'Other'
df = pd.read_csv('AfricaCupofNationsMatches.csv')
most_freq = df['HomeTeamGoals'].mode()[0]
new_series = df['HomeTeamGoals'].apply(lambda x: x if x == most_freq else 'Other')
print("\nMost frequent value in 'HomeTeamGoals':", most_freq)
print(new_series.value_counts())

print("\n--- DATAFRAMES SECTION ---")
# 1. Read the given csv file (already loaded as df)
print("\nFirst 5 rows:")
print(df.head())

# 2. Get the first 7 rows
print("\nFirst 7 rows:")
print(df.head(7))

# 3. Select specific columns
print("\nSelected columns:")
print(df[['HomeTeam', 'AwayTeam', 'HomeTeamGoals', 'AwayTeamGoals']].head())

# 4. Select rows where Egypt appears
print("\nRows where Egypt appears:")
print(df[(df['HomeTeam'] == 'Egypt') | (df['AwayTeam'] == 'Egypt')])

# 5. Count rows and columns
print("\nRows and columns:")
print(df.shape)

# 6. Select rows where 'Attendance' is missing
print("\nRows with missing Attendance:")
print(df[df['Attendance'].isnull()])

# 7. Select rows where 'HomeTeamGoals' are between 3 and 6 inclusive
print("\nRows where HomeTeamGoals between 3 and 6:")
print(df[df['HomeTeamGoals'].between(3, 6)])

# 8. Change 'AwayTeamGoals' in the 3rd row to 10
df.at[2, 'AwayTeamGoals'] = 10
print("\nChanged AwayTeamGoals in 3rd row to 10:")
print(df.iloc[2])

# 9. Sort by 'HomeTeam' (asc) and 'HomeTeamScores' (desc)
if 'HomeTeamScores' in df.columns:
    sorted_df = df.sort_values(['HomeTeam', 'HomeTeamScores'], ascending=[True, False])
    print("\nSorted by HomeTeam and HomeTeamScores:")
    print(sorted_df.head())
else:
    print("\nColumn 'HomeTeamScores' not found for sorting.")

# 10. Get list from DataFrame column headers
print("\nColumn headers:")
print(list(df.columns))

# 11. Append a column of your choice
df['MatchType'] = 'Group'
print("\nAppended 'MatchType' column:")
print(df[['MatchType']].head())

# 12. Add 2 rows to your DataFrame
new_rows = pd.DataFrame({col: [np.nan, np.nan] for col in df.columns})
df = pd.concat([df, new_rows], ignore_index=True)
print("\nAdded 2 new rows:")
print(df.tail(3))

# 13. Change 'Uganda' to 'China' in 'AwayTeam'
df['AwayTeam'] = df['AwayTeam'].replace('Uganda', 'China')
print("\nChanged 'Uganda' to 'China' in AwayTeam:")
print(df['AwayTeam'].value_counts())

# 14. Reset index
df = df.reset_index(drop=True)
print("\nIndex reset.")

# 15. Check if 'Stadium' column is present
print("\nIs 'Stadium' column present?", 'Stadium' in df.columns)

# 16. Convert datatype of 'AwayTeamGoals' to float
df['AwayTeamGoals'] = df['AwayTeamGoals'].astype(float)
print("\nConverted 'AwayTeamGoals' to float:")
print(df['AwayTeamGoals'].dtype)

# 17. Remove last 10 rows
df = df.iloc[:-10]
print("\nRemoved last 10 rows. New shape:", df.shape)

# 18. Iterate over rows
print("\nIterating over first 3 rows:")
for idx, row in df.head(3).iterrows():
    print(row.to_dict())

# 19. Change order of columns
cols = list(df.columns)
if len(cols) > 1:
    new_order = cols[::-1]
    df = df[new_order]
    print("\nChanged order of columns:")
    print(df.head())

# 20. Delete rows where 'HomeTeamGoals' is 0
df = df[df['HomeTeamGoals'] != 0]
print("\nDeleted rows where HomeTeamGoals is 0. New shape:", df.shape) 