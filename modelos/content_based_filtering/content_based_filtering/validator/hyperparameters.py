
def stop_words(value):
    stop = value.lower()

    # VALIDATION:
    if stop != 'none' and stop != 'english':
        stop = 'english'

    if stop == 'none':
        stop = 'None'

    return stop


def metric(value):
    metric_value = value.lower()

    # VALIDATION:
    if metric_value != "linear_kernel" and metric_value != "cosine_similarity":
        metric_value = "linear_kernel"

    return metric_value


def how_many(value):
    quantity = int(value)

    # VALIDATION:
    if quantity < 2:
        quantity = 3

    return quantity
