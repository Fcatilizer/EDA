import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.head()

len(df)
df.shape

df.info()
df.describe()
df.isnull().sum()

df.isnull.mean()*100

#bargraph of gender
df['gender'].value_counts().plot(kind='bar')