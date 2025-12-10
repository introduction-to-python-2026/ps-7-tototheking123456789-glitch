import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
import pandas as pd
data = fetch_openml(name='california_housing', version=1, as_frame=True,parser='pandas')
print(data.DESCR)
df = data.frame

df.sample(5)

df.describe()


df.dtypes



features = list(df.columns)
print("Available features:", features)
selected_features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population']
print("Selected features: ", selected_features)


fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)


reference_feature = selected_features[0]  
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()
