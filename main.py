# main.py
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
plt

