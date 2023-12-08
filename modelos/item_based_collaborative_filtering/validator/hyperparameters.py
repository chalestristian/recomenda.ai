# Hyperparameters

def n_neighbors(value):
    n_neighbors_input = int(value)

    # VALIDATION:
    if n_neighbors_input < 2:
        n_neighbors_input = 9

    if n_neighbors_input % 2 == 0:
        n_neighbors_input -= 1

    return n_neighbors_input


def metric(value):
    metric_input = value.lower()

    # VALIDATION:
    if metric_input != "euclidean" and metric_input != "manhattan":
        metric_input = "cosine"

    return metric_input


def algorithm(value):
    algorithm_input = value.lower()

    if algorithm_input != "ball_tree" and algorithm_input != "kd_tree" and algorithm_input != "auto":
        algorithm_input = "brute"

    return algorithm_input
