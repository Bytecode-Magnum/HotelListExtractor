import pandas as pd
from transformers import pipeline
from tqdm import tqdm


df1=pd.read_csv(r'C:\Users\ankit\Desktop\HotelList\artifacts\data\shojareviews.csv')
df2=pd.read_csv(r'C:\Users\ankit\Desktop\HotelList\artifacts\data\CleanedShojaHotel.csv')
print(df1.dtypes)
print(df2.dtypes)