import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)
df = data.frame
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())
features = ["MedInc", "AveRooms", "AveBedrms", "Population", "MedHouseVal"]
df_subset = df[features]
plt.figure(figsize=(12, 8))
df_subset.hist(bins=30, figsize=(12, 8))
pltimport matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
df = housing.frame

print("First rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

features = ["MedInc", "AveRooms", "AveBedrms", "Population", "MedHouseVal"]
df_selected = df[features]

df_selected.hist(figsize=(12, 8), bins=30)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df["MedInc"], df["MedHouseVal"], alpha=0.4)
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Median Income vs Median House Value")
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df["AveRooms"], df["MedHouseVa]()


