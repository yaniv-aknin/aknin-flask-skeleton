from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy()
db.init_app(app)

all_models = {name: obj for name, obj in globals().items()
              if isinstance(obj, type) and issubclass(obj, db.Model)}
