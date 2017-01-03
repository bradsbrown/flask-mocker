import argparse
import json
import os
import uuid

from flask import Flask, request, abort
from flask_restful import Resource, Api


parser = argparse.ArgumentParser(description="Parameters for flask-mocker")
parser.add_argument('-p', '--port', help='the port number for the server to run')
parser.add_argument('file', help='the name of your JSON data file')
parser.add_argument('--debug', dest='debug', action='store_true',
                    help='this runs the app in debug mode')
parser.set_defaults(debug=False, port=5000)


args = parser.parse_args()
filename = args.file

app = Flask(__name__)
api = Api(app)


if not os.path.exists(filename):
    raise FileNotFoundError("File '{}' not found!".format(filename))


with open(filename, 'r') as f:
    data = json.load(f)


class Item(Resource):
    def get(self, category, id_):
        if id_ not in data[category]:
            abort(404)
        return data[category][id_]

    def put(self, category, id_):
        if id_ not in data[category]:
            abort(404)
        put_data = request.form.to_dict()
        data[category][id_].update(put_data)
        return data[category][id_]

    def delete(self, category, id_):
        del data[category][id_]
        return {'message': 'Delete Successful!'}


class Category(Resource):
    def get(self, category):
        if category not in data:
            abort(404)
        return data[category]

    def post(self, category):
        id_ = str(uuid.uuid4())
        post_data = request.form.to_dict()
        data[category][id_] = post_data
        return {id_: data[category][id_]}


class Categories(Resource):
    def get(self):
        return data


api.add_resource(Categories, '/')


api.add_resource(Category, '/<string:category>')


api.add_resource(Item, '/<string:category>/<string:id_>')


if __name__ == '__main__':
    app.run(port=args.port, debug=args.debug)
