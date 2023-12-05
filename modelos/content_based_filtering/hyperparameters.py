# Hyperparameters

def stop_words():
    print('STOPWORDS(str): english, none | (default: english)')
    stop = input("stopwords: ").lower()

    # VALIDATION:

    if stop != 'none' and stop != 'english':
        stop = 'english'

    if stop == 'none':
        stop = 'None'

    return stop


def metric():
    print('METRIC(str): linear_kernel | cosine_similarity | (default: linear_kernel)')
    metric_input = input("metric: ").lower()

    # VALIDATION:
    if metric_input != "linear_kernel" and metric_input != "cosine_similarity":
        metric_input = "linear_kernel"

    return metric_input


def how_many():
    print('RECOMENDATION QUANTITY(int): from 3 up to the list length. (default: 5)')
    quantity = input("quantity: ")
    value = int(quantity)

    # VALIDATION:
    if value < 2:
        value = 3

    return value
