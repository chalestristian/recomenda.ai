from flask import Flask
from flask_restx import Api, Resource, reqparse
from main import main as m
from validator import hyperparameters as hp

app = Flask(__name__)
api = Api(app, version='1.0', title='recomenda.ai', description='API For movies recommendation', doc='/')
content_based_namespace = api.namespace('content_based_filtering', description='Endpoint responsible for making the recommendation based on ContentBasedFiltering model')


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

        value_stop = hp.stop_words(stop_param)
        value_metric = hp.metric(metric_param)
        value_how_many = hp.how_many(how_many_param)

        result = m.main(value_stop, value_metric, value_how_many, movie_title_param)

        return {'recommendations': result}


if __name__ == '__main__':
    app.run(debug=True)
