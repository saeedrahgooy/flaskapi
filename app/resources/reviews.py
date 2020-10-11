from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse, inputs
from app.models import models


class ReviewList(Resource):
    def __init__(self):
        self.reqpare = reqparse.RequestParser()
        self.reqpare.add_argument(
            'course',
            type=inputs.positive,
            required=True,
            help='No Course Provider',
            location=['json', 'form']
        )
        self.reqpare.add_argument(
            'rating',
            type=inputs.int_range(1, 5),
            required=True,
            help='No rating Provided',
            location=['json', 'form']
        )
        self.reqpare = reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            location=['json', 'form'],
            default=''
        )
        super().__init__()

    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})


class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})


reviews_api = Blueprint('resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)
api.add_resource(
    Review,
    '/review/<int:id>',
    endpoint='review'
)
