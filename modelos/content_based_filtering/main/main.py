from content_based_filtering.main import dataset

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


def main(stop, metric, how_many, titles_input):
    movies = dataset.import_data()

    titles_list = [title.strip() for title in titles_input.split('|')]

    if stop == 'None':
        tfidf_vector = TfidfVectorizer(stop_words=None)
    else:
        tfidf_vector = TfidfVectorizer(stop_words=stop)

    tfidf_matrix = tfidf_vector.fit_transform(movies['genres'])

    if metric == 'linear_kernel':
        sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    elif metric == 'cosine_similarity':
        sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def get_title_year_from_index(index):
        return movies[movies.index == index]['title_year'].values[0]

    def get_index_from_title(title):
        return movies[movies.title == title].index.values[0]

    def contents_based_recommender(movie_user_likes, how_many):
        recommendations = []

        for title_input in movie_user_likes:
            movie_index = get_index_from_title(title_input)
            movie_list = list(enumerate(sim_matrix[int(movie_index)]))
            similar_movies = list(
                filter(lambda x: x[0] != int(movie_index), sorted(movie_list, key=lambda x: x[1], reverse=True)))
            reference_genre = movies.loc[movies.index == int(movie_index), 'genres'].values[0]
            value_parameters = "metric: {} | stop_word: {} | how_many: {}".format(metric, stop, how_many)
            recommendation_data = {
                'parameters': value_parameters,
                'input_movie': title_input,
                'reference_genre': reference_genre,
                'similar_movies': []
            }

            for i, s in similar_movies[:how_many]:
                similar_title = get_title_year_from_index(i)
                similar_genre = movies.loc[movies.index == i, 'genres'].values[0]
                recommendation_data['similar_movies'].append({
                    'title': similar_title,
                    'genre': similar_genre
                })

            recommendations.append(recommendation_data)

        return recommendations

    result = contents_based_recommender(titles_list, how_many)

    return result
