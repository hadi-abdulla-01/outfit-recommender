import pandas as pd

def recommend_outfit(occasion, weather):
    df = pd.read_csv('data/outfits.csv')
    result = df[(df['occasion'] == occasion) & (df['weather'] == weather)]
    if not result.empty:
        return result.iloc[0]['outfit']
    return "No recommendation available for this combination."
