import os
import sys
import json

from flask import Flask, request, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


if len(sys.argv) < 2:
    raise ValueError("No .json filename provided --> 'python app.py <filename>.json'")


file = sys.argv[1]


if not os.path.exists(file):
    raise FileNotFoundError("File '{}' not found!".format(file))


with open(file, 'r') as f:
    data = json.load(f)


class Item(Resource):
    def _get_index_by_id(self, category, id_):
        try:
            idx = next(i for i,j in enumerate(data[category]) if j['id'] == id_)
        except StopIteration:
            abort(404)
        return idx

    def get(self, category, id_):
        idx = self._get_index_by_id(category, id_)
        return data[category][idx]

    def put(self, category, id_):
        idx = self._get_index_by_id(category, id_)
        put_data = request.form.to_dict()
        put_data.pop('id')
        data[category][idx].update(put_data)
        return data[category][idx]

    def delete(self, category, id_):
        idx = self._get_index_by_id(category, id_)
        del data[category][idx]
        return {'status': 'Delete Successful!'}


class Category(Resource):
    def _next_id(self, category):
        try:
            return max(item['id'] for item in data[category]) + 1
        except TypeError:
            return 0

    def get(self, category):
        return data[category]

    def post(self, category):
        id_ = self._next_id(category)
        post_data = request.form.to_dict()
        post_data.update(id=id_)
        data[category].append(post_data)
        return post_data


class Categories(Resource):
    def get(self):
        return data


api.add_resource(Categories, '/')


api.add_resource(Category, '/<string:category>')


api.add_resource(Item, '/<string:category>/<int:id_>')


if __name__ == '__main__':
    app.run(debug=True)
