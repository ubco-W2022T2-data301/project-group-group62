import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    dfm = (
    pd.read_csv('../data/processed/jeremy_process.csv', usecols= ['room_type', 'bathrooms_text', 'bedrooms','price'])
    .rename(columns={"room_type": "Rt"})
    .rename(columns={"bathrooms_text":"Bt"})
    .loc[lambda x: x['price']>2000]
    .reset_index(drop=True))
    
    df2 = (dfm)
    return df2
