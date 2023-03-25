import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    dfx = (
        pd.read_csv('../data/processed/wingfixed.csv')
        .sort_values("minimum_nights", ascending=False)
        .rename(columns={"minimum_nights": "minnights"})
        .query("minnights > 1")
        .reset_index(drop=True))

    dfy = (dfx)
    
    return dfy

