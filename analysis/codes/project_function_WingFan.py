import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    dfx = (
        pd.read_csv("../data/processed/wingfixed.csv")
        .sort_values("minimum_nights", ascending=False)
        .rename(columns={"minimum_nights": "minnights"})
        .query("minnights > 1")
        .reset_index(drop=True)
        .dropna()
    ) 

    dfy = (
        dfx
        .assign(
            rental_type=lambda x: pd.cut(x['minnights'], bins=5, labels=['short vaca', 'long vaca', 'short accomodation', 'long accomodation', 'long term rentals']),
            has_wifi=lambda x:x['amenities'].apply(lambda x : True if 'wifi' in x else False),
            long_term_available=lambda x:x['amenities'].apply(lambda x: True if 'Long term stays allowed' in x else False)
        ))

        

    return dfy

