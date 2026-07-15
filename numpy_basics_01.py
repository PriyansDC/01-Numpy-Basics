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


