# Hyperparameters

def n_neighbors():
    print('N_NEIGHBORS(int): from 3 up to the list length. (default: 3 - recommended to input just odd numbers)')
    quantity = input("n_neighbors: ")
    n_neighbors_input = int(quantity)

    # VALIDATION:
    if n_neighbors_input < 2:
        n_neighbors_input = 3

    return n_neighbors_input


def metric():
    print('METRIC(str): cosine | euclidean | manhattan. (default: cosine)')
    metric_input = input("metric: ").lower()

    # VALIDATION:
    if metric_input != "euclidean" and metric_input != "manhattan":
        metric_input = "cosine"

    return metric_input


def algorithm():
    print('ALGORITHM(str): brute | ball_tree | kd_tree | auto. (default: brute)')
    algorithm_input = input("algorithm: ").lower()

    if algorithm_input != "ball_tree" and algorithm_input != "kd_tree" and algorithm_input != "auto":
        algorithm_input = "brute"

    return algorithm_input
