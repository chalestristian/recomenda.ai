import dataset
from sklearn.neighbors import NearestNeighbors

df = dataset.import_data()

title_input = input("TITLE (str): ")
quantity = input("RECOMMENDATIONS TO GET (int): ")
quantity_input = int(quantity)

near = NearestNeighbors(metric='cosine', algorithm='brute')
near.fit(df.values)
distances, indices = near.kneighbors(df.values, n_neighbors=quantity_input)

def recommend_movie_by_item(title):
    index_user_likes = df.index.tolist().index(title)
    sim_movies = indices[index_user_likes].tolist()
    movie_distances = distances[index_user_likes].tolist()
    print('==============================================')
    print('MOVIES SIMILAR TO: ' + str(title) + ':\n')
    j = 1

    for i, distance in zip(sim_movies, movie_distances):
        print(str(j) + ': ' + str(df.index[i]) + ' | [Distance: ' + str(distance) + ' ]')
        j = j + 1
    print('\n')

recommend_movie_by_item(title_input)

