# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.random.rand(3, 3)
array3 = np.zeros((4, 4))

# %%
np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)

# %%
loaded_array1 = np.load('array1.npy')
print(loaded_array1)

# %%
try:
    logo = np.load('numpy-logo.npy')

    # Display
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("Numpy logo")
    plt.grid(False)

    dark_logo = 1 - logo

    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("Numpy logo")
    plt.grid(False)

except FileNotFoundError:
    print("numpy logo file not found")


