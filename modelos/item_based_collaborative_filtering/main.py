import dataset
from sklearn.neighbors import NearestNeighbors

df = dataset.import_data()

# Hyperparameters
print('========================')
print('HYPERPARAMETERS OPTIONS: \n')

print('N_NEIGHBORS(int): from 2 up to the list length. (default: 3)')
quantity = input("n_neighbors: ")
n_neighbors_input = int(quantity)
print('\n')

print('METRIC(str): cosine | euclidean | manhattan. (default: cosine)')
metric_input = input("metric: ")
print('\n')

print('ALGORITHM(str): brute | ball_tree | kd_tree | auto. (default: brute)')
algorithm_input = input("algorithm: ")

metric_input = metric_input.lower()
algorithm_input = algorithm_input.lower()

print('========================\n')

title_input = input("TITLE (str): ")

# VALIDATION:
if n_neighbors_input < 2:
    n_neighbors_input = 3

if metric_input != "euclidean" and metric_input != "manhattan":
    metric_input = "cosine"

if algorithm_input != "ball_tree" and algorithm_input != "kd_tree" and algorithm_input != "auto":
    algorithm_input = "brute"

near = NearestNeighbors(metric=metric_input, algorithm=algorithm_input)
near.fit(df.values)
distances, indices = near.kneighbors(df.values, n_neighbors=n_neighbors_input)


def recommend_movie_by_item(title):
    index_user_likes = df.index.tolist().index(title)
    sim_movies = indices[index_user_likes].tolist()
    movie_distances = distances[index_user_likes].tolist()
    print('==============================================')
    print('MOVIES SIMILAR TO [ ' + str(title) + " ] - "
          "(n_neighbors: " + str(n_neighbors_input) +
          " | metric: " + str(metric_input) +
          " | algorithm: " + str(algorithm_input) + ' ) \n')
    j = 1

    for i, distance in zip(sim_movies, movie_distances):
        print(str(j) + ': ' + str(df.index[i]) + ' | [Distance: ' + str(distance) + ' ]')
        j = j + 1
    print('\n')


recommend_movie_by_item(title_input)