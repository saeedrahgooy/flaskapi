from app import create_app
# from flask_mongoengine import MongoEngine
from flask import jsonify, request
from app.models.models import Course

app = create_app()


@app.route('/', methods=['POST'])
def test():
    Course(
        title=request.json['title'],
        url=request.json['url'],
    ).save()
    return jsonify({"result": "ok"}), 201


if __name__ == '__main__':
    app.run()
