from flask import jsonify, Blueprint, abort
from flask_restful import Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for
from app.models import models, db


course_fields = {
    'title': fields.String,
    'url': fields.String,
    'review': fields.List(fields.String)
}


# def add_reviews(course):
#     course.reviews = [url_for('resources.reviews.review', id=review.id)
#                       for review in course.review_set]
#     return course


class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No Course Title provided',
            location=['json', 'form']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No Coursee Url Provided',
            location=['json', 'form'],
            type=inputs.url
        )
        super().__init__()

    def get(self):
        courses = [marshal(course, course_fields)
                   for course in models.Course.objects()]
        return {'courses': courses}

    def post(self):
        args = self.reqparse.parse_args()
        course = models.Course(**args).save()
        return {'id': str((course.id))}, 200


class Course(Resource):
    @marshal_with(course_fields)
    def get(self, id):
        try:
            course = models.Course.objects().get(id=id)
        except models.Course.DoseNotExist:
            abort(404, message="Course {} Dose Not exist".format(id))
        else:
            return marshal(course, course_fields)

    def put(self, id):
        return jsonify({'title': 'python basics'})

    def delete(self, id):
        return jsonify({'title': 'python basics'})


courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='course'
)
api.add_resource(
    Course,
    '/api/v1/course/<float:id>',
    endpoint='courses'
)
