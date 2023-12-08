from item_based_collaborative_filtering.main import dataset
from sklearn.neighbors import NearestNeighbors


def main(n_neighbors, metric, algorithm, title_input):
    df = dataset.import_data()
    df_movie = dataset.import_movies()

    near = NearestNeighbors(metric=metric, algorithm=algorithm)
    near.fit(df.values)
    distances, indices = near.kneighbors(df.values, n_neighbors=n_neighbors)

    def recommend_movie_by_item(title, n_neighbors):
        recommendations = []

        index_user_likes = df.index.tolist().index(title)
        sim_movies = indices[index_user_likes].tolist()
        movie_distances = distances[index_user_likes].tolist()

        sim_movies = sim_movies[:n_neighbors]
        movie_distances = movie_distances[:n_neighbors]

        matching_movies = df_movie[df_movie['title'] == title]
        movie_genre = matching_movies['genres'].values[0]

        value_parameters = "n_neighbors: {} | metric: {} | algorithm: {}".format(n_neighbors, metric, algorithm)
        recommendation_data = {
            'parameters': value_parameters,
            'input_movie': title_input,
            'reference_genre': movie_genre,
            'similar_movies': []
        }

        for i, distance in zip(sim_movies, movie_distances):
            movie_title = df.index[i]
            matching_movies = df_movie[df_movie['title'] == movie_title]
            movie_genre = matching_movies['genres'].values[0]
            recommendation_data['similar_movies'].append({
                'title': movie_title,
                'genre': movie_genre,
                'distance': distance
            })

        recommendations.append(recommendation_data)

        return recommendations

    result = recommend_movie_by_item(title_input, n_neighbors)

    return result

