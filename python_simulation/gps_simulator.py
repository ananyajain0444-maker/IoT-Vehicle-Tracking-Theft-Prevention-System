import pandas as pd

def get_coordinates():
    data = pd.read_csv('data/sample_coordinates.csv')

    for _, row in data.iterrows():
        yield row['latitude'], row['longitude']
