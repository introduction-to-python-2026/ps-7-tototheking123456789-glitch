import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
import pandas as pd
data = fetch_openml(name='california_housing', version=1, as_frame=True,parser='pandas')
print(data.DESCR)
