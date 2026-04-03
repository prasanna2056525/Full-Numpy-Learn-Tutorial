import pandas as pd 
import numpy as np 

df = pd.read_csv(r'C:\Users\prasa\OneDrive\Desktop\Full Numpy Tutorial Learn\Full-Numpy-Learn-Tutorial\Dataset Cleaning project\imdb_1000.csv')
print(df.head())

print(df.isnull().sum())
df['content_rating']=df['content_rating'].fillna(df['content_rating'].mode()[0],)
df.replace([np.inf,-np.inf], np.nan, inplace=True)
df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

df.drop_duplicates(inplace=True)
print(df.isnull().sum())

df.to_csv('Cleaned_data.csv')
