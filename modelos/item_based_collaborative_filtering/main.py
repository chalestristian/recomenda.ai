import dataset
from sklearn.neighbors import NearestNeighbors

title_input = input("TITLE: ")
quantity = input("QUANTITY: ")
quantity_input = int(quantity)

df = dataset.import_data()

near = NearestNeighbors(metric='cosine', algorithm='brute')
near.fit(df.values)
distances, indices = near.kneighbors(df.values, n_neighbors=quantity_input)

def recommend_movie_by_item(title):
    index_user_likes = df.index.tolist().index(title)
    sim_movies = indices[index_user_likes].tolist()
    movie_distances = distances[index_user_likes].tolist()

    print('Similar Movies to ' + str(title) + ':\n')

    j = 1

    for i, distance in zip(sim_movies, movie_distances):
        print(str(j) + ': ' + str(df.index[i]) + ', the distance with ' + str(title) + ': ' + str(distance))
        j = j + 1

    print('\n')

recommend_movie_by_item(title_input)

