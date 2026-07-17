# %% [markdown]
# Learn about numpy with chai aur code
# 

# %%
import numpy as np

# %% [markdown]
# creating array from list

# %%
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array: \n", arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array: \n", arr_2d)

# %% [markdown]
# List vs Numpy array

# %%
py_list = [1, 2, 3]
print("Python list multiplication: ", py_list*2)

np_arr = np.array([1, 2, 3]) # element wise mulitplication
print("Python array multiplication: ", np_arr*2)

import time
start = time.time()
py_list = [i*2 for i in range(1000000)]
print("\n List operation time: ", time.time() - start)

start = time.time()
np_arr = np.arange(1000000) * 2
print("\n Numpy operation time: ", time.time() - start)

# %%
arr = np.arange(10) # np.arange(start, stop, step)
print(arr)

# %% [markdown]
# Creating array from scratch

# %%
zeros = np.zeros((3, 4))
print("Zeros array: \n", zeros)

ones = np.ones((2, 3))
print("Ones array: \n", ones)

full = np.full((2, 2), 7)
print("Full array: \n", full)

random = np.random.random((2, 3))
print("Random array: \n", random)

sequence = np.arange(0, 11, 2)
print("Sequence array: \n", sequence)

# %% [markdown]
# Vector, Matrices and Tensor

# %%
vector = np.array([1, 2, 3])
print("Vector: \n", vector)

matrices = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("Matrices: \n", matrices)

tensor = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print("Tensor: \n", tensor)

# %% [markdown]
# Array properties

# %%
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array: \n", arr)
print("Shape: ", arr.shape)
print("Dimension: ", arr.ndim)
print("Size: ", arr.size)
print("Data type: ", arr.dtype)

# %% [markdown]
# Array Reshaping

# %%
arr = np.arange(12)
print("Original array: ", arr)

reshaped = arr.reshape((3, 4))
print("Reshaped array: \n", reshaped)

flattened = reshaped.flatten()
print("Flattened array: \n", flattened)

# ravel (returns view, instead of copy)
raveled = reshaped.ravel()
print("Raveled array: \n", raveled)

# Transpose
transpose = reshaped.T
print("Transpose array: \n", transpose)


