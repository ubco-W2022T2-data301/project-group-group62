def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .loc[:, ['neighbourhood_cleansed', 'review_scores_value', 'review_scores_location', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_communication', 'price', 'accommodates']]
        .dropna(subset=['review_scores_value', 'review_scores_location', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_communication'])
        .assign(average_rating=lambda x: x[['review_scores_value', 'review_scores_location', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_communication']].mean(axis=1),
                price_per_person=lambda x: (x['price'].astype(float) / x['accommodates']).round(2))
        .drop(columns=['price', 'accommodates'])
        .loc[lambda x: x['average_rating'] != 0]
        .reset_index(drop=True)
    )

    # Method Chain 2 
    low_pct, below_avg_pct, avg_pct, above_avg_pct, high_pct = np.percentile(df1['average_rating'], [5, 30, 50, 70, 95])
    bins = [0, low_pct, below_avg_pct, avg_pct, above_avg_pct, high_pct, 5]
    labels = ['Low', 'Below Average', 'Average', 'Above Average', 'High']
    df2 = (
        df1.assign(rating_category=lambda x: pd.cut(x['average_rating'], bins=bins, labels=labels, include_lowest=True, duplicates='drop'))
    )

    return df2
