# Program 4.1: Pandas Series
import pandas as pd

# a. Create and display a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("One-dimensional array-like object (Pandas Series):")
print(series)

# b. Convert Series to Python list
py_list = series.tolist()
print("\nConverted Python list:", py_list)
print("Type of the converted object:", type(py_list))