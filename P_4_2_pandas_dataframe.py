# Program 4.2: Pandas DataFrame
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create and display a DataFrame
df = pd.DataFrame(exam_data, index=labels)
print("Original DataFrame:")
print(df)

# Change a value: 'James' to 'Suresh'
df.loc['d', 'name'] = 'Suresh'
print("\nDataFrame after changing 'James' to 'Suresh':")
print(df)

# Insert a new column
df['age'] = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print("\nDataFrame after adding 'age' column:")
print(df)

# Get column headers as a list
col_list = df.columns.tolist()
print("\nList of column headers:")
print(col_list)