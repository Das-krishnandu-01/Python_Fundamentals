# Program 3.2: NumPy array analysis
import numpy as np

arr = np.array([4, 7, 2, 9, 2, 7, 5, 9, 2])
print("Array:", arr)

value = 5
greater_than_value = arr[arr > value]
less_than_value = arr[arr < value]

print("\nNumbers greater than", value, ":", greater_than_value)
print("Numbers less than", value, ":", less_than_value)

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("\nIndex of Maximum Value:", max_index)
print("Index of Minimum Value:", min_index)