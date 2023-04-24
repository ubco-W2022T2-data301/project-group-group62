import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def load_and_process(url):

    df = (
        pd.read_csv(url)
        .loc[:, ['neighbourhood_cleansed', 'review_scores_value', 'review_scores_location', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_communication', 'price', 'accommodates']]
        .dropna(subset=['review_scores_value', 'review_scores_location', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_communication'])
        .assign(average_rating=lambda x: x[['review_scores_value', 'review_scores_location', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_communication']].mean(axis=1),
                price_per_person=lambda x: (x['price'].astype(float) / x['accommodates']).round(2))
        .drop(columns=['price', 'accommodates'])
        .loc[lambda x: x['average_rating'] != 0]
        .reset_index(drop=True)
    )

    low_pct, below_avg_pct, avg_pct, above_avg_pct, high_pct = np.percentile(df['average_rating'], [5, 30, 50, 70, 95])
    bins = [0, low_pct, below_avg_pct, avg_pct, above_avg_pct, high_pct, 5]
    labels = ['Low', 'Below Average', 'Average', 'Above Average', 'High']

    quantiles = [0, 0.1, 0.35, 0.75, 0.9, 1]
    price_labels = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']

    df = (
        df.assign(
            rating_category=lambda x: pd.cut(x['average_rating'], bins=bins, labels=labels, include_lowest=True, duplicates='drop'),
            price_level=lambda x: pd.qcut(x['price_per_person'], q=quantiles, labels=price_labels),
            price_range=lambda x: pd.qcut(x['price_per_person'], q=quantiles),
        )
    )

    return df
