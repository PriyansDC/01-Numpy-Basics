# %% [markdown]
# Advance operation with Business examples

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], # Paradise Biryani
    [2, 120000, 140000, 160000, 190000], # Beijing Bites
    [3, 200000, 230000, 260000, 300000], # Pizza Hub
    [4, 180000, 210000, 240000, 270000], # Burger Point
    [5, 160000, 185000, 205000, 230000]  # Chai Point
])

print("==== Zomato Sales analysis ====")
print("\n Sales data shape: ", sales_data.shape)
print("\n Sample data for 1st 3 restaurant: \n", sales_data[:3])

# %%
# Total sales per year
print(np.sum(sales_data, axis=0))
yearly_total = np.sum(sales_data[:, 1:], axis=0) # sales_data[:, 1:] -> sales_data[start:end(all rows), from first col: to end ]
print(yearly_total)

# Minimum sales per restaurant
min_sales = np.min(sales_data[:, 1:], axis= 1)
print(min_sales)

# Maximum sales per year
max_sales = np.max(sales_data[:, 1:], axis= 0)
print(max_sales)

# Average sales per restaurant
avg_sales = np.average(sales_data[:, 1:], axis= 1)
print(avg_sales)

# %%
# Cummilative sales per restaurant
cumsum = np.cumsum(sales_data[:, 1:], axis= 1)
print(cumsum)

plt.figure(figsize=(8, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Average cummilative sales across all restaurant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# %%
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

print("Vector Addition: ", vector1 + vector2)
print("Multiplication vector: ", vector1 * vector2)
print("Dot Product: ", np.dot(vector1, vector2))

angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)

# %%
restaurant_types = np.array(['biryani', 'chinese', 'pizza', 'burger', 'cafe']) # Vectorize
vectorized_upper = np.vectorize(str.upper)
print("Vectorized upper: ", vectorized_upper(restaurant_types))

# %%
monthly_avg = sales_data[:, 1:] / 12 # Broadcasting

print("Monthly average: ", monthly_avg)


