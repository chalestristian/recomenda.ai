import pandas as pd
import numpy as np


def cut_title(title):
    year = title[len(title) - 5:len(title) - 1]

    if year.isnumeric():
        title_no_year = title[:len(title) - 7]
        return title_no_year
    else:
        return title


def cut_year(title):
    year = title[len(title) - 5:len(title) - 1]

    if year.isnumeric():
        return int(year)
    else:
        return np.nan


def import_data():
    ratings = '/app/content_based_filtering/dataset/ratings.csv'
    movies = '/app/item_based_collaborative_filtering/dataset/movies.csv'

    ratings = pd.read_csv(ratings)
    movies = pd.read_csv(movies)

    movies.rename(columns={'title': 'title_year'}, inplace=True)
    movies['title_year'] = movies['title_year'].apply(lambda x: x.strip())
    movies['title'] = movies['title_year'].apply(cut_title)
    movies['year'] = movies['title_year'].apply(cut_year)
    movies = movies[~(movies['genres'] == '(no genres listed)')].reset_index(drop=True)
    movies['genres'] = movies['genres'].str.replace('Sci-Fi', 'SciFi')
    movies['genres'] = movies['genres'].str.replace('Film-Noir', 'Noir')

    merge = pd.merge(ratings, movies, on='movieId', how='inner')
    merge['rating'] = merge['rating'].astype(int)

    dataframe = pd.pivot_table(merge, values='rating', index='title', columns='userId', fill_value=0)
    return dataframe


def import_movies():
    movies = '/app/item_based_collaborative_filtering/dataset/movies.csv'
    movies = pd.read_csv(movies)

    movies.rename(columns={'title': 'title_year'}, inplace=True)
    movies['title_year'] = movies['title_year'].apply(lambda x: x.strip())
    movies['title'] = movies['title_year'].apply(cut_title)
    movies['year'] = movies['title_year'].apply(cut_year)
    movies = movies[~(movies['genres'] == '(no genres listed)')].reset_index(drop=True)
    movies['genres'] = movies['genres'].str.replace('Sci-Fi', 'SciFi')
    movies['genres'] = movies['genres'].str.replace('Film-Noir', 'Noir')

    return movies
