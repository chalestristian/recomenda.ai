from flask import Flask
from flask_restx import Api, Resource, reqparse
from content_based_filtering.main import main as content_based_main
from item_based_collaborative_filtering.main import main as item_based_main
from content_based_filtering.validator import hyperparameters as content_hp
from item_based_collaborative_filtering.validator import hyperparameters as item_hp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app, version='1.0', title='recomenda.ai', description='API For movies recommendation')
namespace = api.namespace('movies_recommendation', description='Movie recommendation system with models based on Item and Content')

#api.add_namespace(content_namespace)

@app.route('/swagger.json')
def swagger_json():
    return api.as_postman(urlvars=False, swagger=True)


SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "recomenda.ai",
        'docExpansion': 'full'
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@namespace.route('/content_based_filtering')
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


@namespace.route('/item_based_collaborative_filtering')
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
    app.run(host='0.0.0.0', debug=False)
