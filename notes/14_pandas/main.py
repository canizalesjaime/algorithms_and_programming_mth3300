import pandas as pd

df = pd.read_csv("students.csv")

print(df)

#print(df.info())

#print(df["Score"].mean())

print(df.describe())