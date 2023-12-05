import dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies = dataset.import_data()


tfidf_vector = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vector.fit_transform(movies['genres'])

sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)


def get_title_year_from_index(index):
    return movies[movies.index == index]['title_year'].values[0]


def get_index_from_title(title):
    return movies[movies.title == title].index.values[0]


def contents_based_recommender(movie_user_likes, how_many):
    movie_index = get_index_from_title(movie_user_likes)
    movie_list = list(enumerate(sim_matrix[int(movie_index)]))
    similar_movies = list(
        filter(lambda x: x[0] != int(movie_index), sorted(movie_list, key=lambda x: x[1], reverse=True)))
    print('MOVIES SIMILAR TO: ' + str(movie_user_likes) + '\n')

    for i, s in similar_movies[:how_many]:
        print(get_title_year_from_index(i))


contents_based_recommender('Toy Story', 10)