import pandas as pd


def import_data():
    ratings = '../../dataset/ratings.csv'
    movies = '../../dataset/movies.csv'

    ratings = pd.read_csv(ratings)
    movies = pd.read_csv(movies)

    merge = pd.merge(ratings, movies, on='movieId', how='inner')
    merge['rating'] = merge['rating'].astype(int)

    dataframe = pd.pivot_table(merge, values='rating', index='title', columns='userId', fill_value=0)
    return dataframe
