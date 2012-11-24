from flask import request
from flask.ext.restful import Api, Resource

from app import app

class ModelEntity(Resource):
    def get(self, id):
        return self.model.query.get_or_404(id)
class ModelCollection(Resource):
    def get(self):
        page = int(request.args.get('page', 1))
        return self.model.query.order_by(self.model.id).paginate(page, 50).items

api = Api(app)
