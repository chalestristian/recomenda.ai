import dataset
import hyperparameters

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

movies = dataset.import_data()
stop = hyperparameters.stop_words()
metric = hyperparameters.metric()
quantity = hyperparameters.how_many()

print('\n============================================================================\n')
title_input = input("MOVIE TITLE (str): ")

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


print('============================================================================\n')


def contents_based_recommender(movie_user_likes, how_many):
    movie_index = get_index_from_title(movie_user_likes)
    movie_list = list(enumerate(sim_matrix[int(movie_index)]))
    similar_movies = list(
        filter(lambda x: x[0] != int(movie_index), sorted(movie_list, key=lambda x: x[1], reverse=True)))
    print("MOVIES SIMILAR TO [ " + str(movie_user_likes) + " ] - "
                                                           " | metric: " + str(metric) +
          " | stop_word: " + str(stop) +
          " | quantity: " + str(quantity) +
          "\n"
          )

    for i, s in similar_movies[:how_many]:
        print(get_title_year_from_index(i))


contents_based_recommender(title_input, quantity)
