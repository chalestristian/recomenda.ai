import dataset
import hyperparameters as hp
from sklearn.neighbors import NearestNeighbors

df = dataset.import_data()
df_movie = dataset.import_movies()

print('============================================================================\n')
print('HYPERPARAMETERS OPTIONS: \n')
n_neighbors = hp.n_neighbors()
print('\n')
metric = hp.metric()
print('\n')
algorithm = hp.algorithm()
print('\n')
print('============================================================================\n')
title_input = input("MOVIE TITLE (str): ")

near = NearestNeighbors(metric=metric, algorithm=algorithm)
near.fit(df.values)
distances, indices = near.kneighbors(df.values, n_neighbors=n_neighbors)


def recommend_movie_by_item(title):
    index_user_likes = df.index.tolist().index(title)
    sim_movies = indices[index_user_likes].tolist()
    movie_distances = distances[index_user_likes].tolist()

    sim_movies.remove(index_user_likes)
    movie_distances = movie_distances[1:]

    matching_movies = df_movie[df_movie['title'] == title]
    movie_genre = matching_movies['genres'].values[0]

    print("MOVIES SIMILAR TO [ " + str(title) + " ] [ " + str(movie_genre) + " ] - "
          "(n_neighbors: " + str(n_neighbors) +
          " | metric: " + str(metric) +
          " | algorithm: " + str(algorithm) + " ) \n"
          )
    j = 1

    for i, distance in zip(sim_movies, movie_distances):
        movie_title = df.index[i]
        matching_movies = df_movie[df_movie['title'] == movie_title]
        movie_genre = matching_movies['genres'].values[0]
        print(f"[Distance: {distance} ] - {movie_title} | [ {movie_genre} ]")
        j = j + 1


recommend_movie_by_item(title_input)
