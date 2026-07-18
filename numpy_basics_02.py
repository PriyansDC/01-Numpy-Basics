# %% [markdown]
# Numpy Array operations

# %%
import numpy as np

# %%
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Basic Slicing: ", arr[2:7])
print("With Step: ", arr[1:8:2])
print("Negative Indexing: ", arr[-3])
print("Negative Slicing: ", arr[:-3])

# %% [markdown]
# 2D Array Indexing/Slicing

# %%
arr_2d = np.array([[1, 2, 3], # 0th row
                   [4, 5, 6], # 1st row
                   [7, 8, 9]]) # 2nd row
print("Specific Element: ", arr_2d[1, 2]) # arr_2d[row, col/element]
print("Entire row: ", arr_2d[1])
print("Entire row: ", arr_2d[:, 1])

# %% [markdown]
# Sorting

# %%
unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Sorted array: ", np.sort(unsorted))

arr_2d_unsorted = np.array([[3, 1], [1, 2], [2, 3]])
print("Sorted 2d array by column: \n", np.sort(arr_2d_unsorted, axis=0)) # axis=0 means column wise sorting (top to bottom)
print("Sorted 2d array by row: \n", np.sort(arr_2d_unsorted, axis=1)) # axis=1 means row wise sorting (left to right)

# %% [markdown]
# Filter

# %%
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_no = numbers[numbers % 2 == 0]
print("Even number: ", even_no)

# %% [markdown]
# Filter with mask

# %%
mask = numbers > 5
print(mask)
print("Numbers greater than 5: ", numbers[mask])

# %% [markdown]
# Fancy Indexing vs np.where

# %%
indices = [0, 2, 4]
print(numbers[indices])

where_result = np.where(numbers > 5)
print(where_result)
print("NP where: ", numbers[where_result])

# %%
condition_array = np.where(numbers > 5, numbers*2, numbers) # np.where(condition, execution (if), execution (else))

# the above can be written as: 
# if (numbers > 5):
    # numbers*2
# else:
#   numbers

print(condition_array)

# Another example
condition = np.where(numbers > 5, "true", "false")
print(condition)

# %% [markdown]
# Adding and removing data

# %%
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

combined = np.concatenate((arr1, arr2))
print(combined)

# %% [markdown]
# Array compatibility

# %%
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

print("Compatibility shapes: ", a.shape == b.shape == c.shape)

# %%
original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

with_new_row = np.vstack((original, new_row)) # vstack adds row
print("Original: \n", original)
print("With New row: \n", with_new_row)

new_col = np.array([[7], [8]])
with_new_col = np.hstack((original, new_col))
print("With New column: \n", with_new_col)

# %%
arr = np.array([1, 2, 3, 4, 5])
deleted = np.delete(arr, 2)
print("Array after deletion: ", deleted)


