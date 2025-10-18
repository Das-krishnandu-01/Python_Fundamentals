# Program 3.1: NumPy basics
import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
print("Original array:", arr)
print("\nUsing repr():")
print(repr(arr))

unique_elements, counts = np.unique(arr, return_counts=True)
print("\nUsing np.unique():")
print("Unique elements:", unique_elements)
print("Counts:", counts)