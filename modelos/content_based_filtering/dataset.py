import pandas as pd
import numpy as np


def import_data():
    movies = '../../dataset/movies.csv'
    movies = pd.read_csv(movies)

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

    movies.rename(columns={'title': 'title_year'}, inplace=True)
    movies['title_year'] = movies['title_year'].apply(lambda x: x.strip())
    movies['title'] = movies['title_year'].apply(cut_title)
    movies['year'] = movies['title_year'].apply(cut_year)
    r, c = movies[movies['genres'] == '(no genres listed)'].shape
    movies = movies[~(movies['genres'] == '(no genres listed)')].reset_index(drop=True)
    movies['genres'] = movies['genres'].str.replace('Sci-Fi', 'SciFi')
    movies['genres'] = movies['genres'].str.replace('Film-Noir', 'Noir')

    return movies
