import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    dfx = (
    pd.read_csv('../data/processed/jeremy_process.csv', usecols= ['room_type', 'bathrooms_text', 'bedrooms','price'])
        .rename(columns={"room_type": "Rt", "bathrooms_text":"Bt"})
        .assign(bedrooms=lambda x: x['bedrooms'].round().astype(int))
        .assign(Bt=lambda x: x['Bt'].str.replace(r'\D', '', regex=True).dropna())
        .dropna(subset=['Bt'], axis=0)
        .loc[lambda x: x['price'] <= 2000]
        .reset_index(drop=True)
)

    dfy = (dfx
           .assign(average_price_for_Room_types=lambda x: x.groupby('Rt')['price'].transform('mean'))
           .assign(average_price_for_Bathrooms=lambda x: x.groupby('Bt')['price'].transform('mean'))
           .assign(average_price_for_Bedroom=lambda x: x.groupby('bedrooms')['price'].transform('mean'))
       )

 
    return dfy
