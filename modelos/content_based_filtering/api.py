from flask import Flask
from flask_restx import Api, Resource, reqparse
from content_based_filtering.main import main as content_based_main
from item_based_collaborative_filtering.main import main as item_based_main
from content_based_filtering.validator import hyperparameters as content_hp
from item_based_collaborative_filtering.validator import hyperparameters as item_hp

app = Flask(__name__)
api = Api(app, version='1.0', title='recomenda.ai', description='API For movies recommendation', doc='/')
content_based_namespace = api.namespace('content_based_filtering', description='Endpoint responsible for making the recommendation based on ContentBasedFiltering model')
item_based_collaborative_namespace = api.namespace('item_based_collaborative_namespace', description='Endpoint responsible for making the recommendation based on ItemBasedCollaborative model')


@content_based_namespace.route('/movie_recomendation')
class ContentBasedFiltering(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('stop_words', type=str, help='stopwords: english | none | (default: english)')
    parser.add_argument('metric', type=str, help='metric: linear_kernel | cosine_similarity | (default: linear_kernel)')
    parser.add_argument('how_many', type=int, help='how_many: from 3 up to the list length | (default: 3)')
    parser.add_argument('movie_title', type=str, help='movie_title: if more than one, separate with a pipe: |')

    @api.doc(params={'stop_words': 'stop_words: english | none | (default: english)',
                     'metric': 'metric: linear_kernel | cosine_similarity | (default: linear_kernel)',
                     'how_many': 'how_many: from 3 up to the list length | (default: 3)',
                     'movie_title': 'movie_title:  if more than one, separate with a pipe: |'})
    @api.expect(parser)
    def get(self):
        args = self.parser.parse_args()
        stop_param = args.get('stop_words')
        metric_param = args.get('metric')
        how_many_param = args.get('how_many')
        movie_title_param = args.get('movie_title')

        value_stop = content_hp.stop_words(stop_param)
        value_metric = content_hp.metric(metric_param)
        value_how_many = content_hp.how_many(how_many_param)

        result = content_based_main.main(value_stop, value_metric, value_how_many, movie_title_param)

        return {'recommendations': result}


@item_based_collaborative_namespace.route('/movie_recomendation')
class ItemBasedCollaborativeFiltering(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('algorithm', type=str, help='algorithm: brute | ball_tree | kd_tree | auto. (default: brute)')
    parser.add_argument('metric', type=str, help='metric: cosine | euclidean | manhattan. (default: cosine)')
    parser.add_argument('n_neighbors', type=int, help='n_neighbors: from 3 up to the list length. (default: 9 [just odd numbers, rounding down]')
    parser.add_argument('movie_title', type=str, help='movie_title: just one is allowed')

    @api.doc(params={'algorithm': 'algorithm: brute | ball_tree | kd_tree | auto. (default: brute)',
                     'metric': 'metric: cosine | euclidean | manhattan. (default: cosine)',
                     'n_neighbors': 'n_neighbors: from 3 up to the list length. (default: 9 [just odd numbers, rounding down]',
                     'movie_title': 'movie_title: just one is allowed'})
    @api.expect(parser)
    def get(self):
        args = self.parser.parse_args()
        algorithm_param = args.get('algorithm')
        metric_param = args.get('metric')
        n_neighbors_param = args.get('n_neighbors')
        movie_title_param = args.get('movie_title')

        value_algorithm = item_hp.algorithm(algorithm_param)
        value_metric = item_hp.metric(metric_param)
        value_n_neighbors = item_hp.n_neighbors(n_neighbors_param)

        result = item_based_main.main(value_n_neighbors, value_metric, value_algorithm, movie_title_param)

        return {'recommendations': result}


if __name__ == '__main__':
    app.run(debug=True)
