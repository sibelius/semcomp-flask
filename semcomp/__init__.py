import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.restful import Api

db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config['MONGODB_DB'] = os.environ.get('DB_NAME', 'semcomp')
    app.config['MONGODB_HOST'] = os.environ.get('DB_HOST', 'localhost')
    app.config['MONGODB_PORT'] = int(os.environ.get('DB_PORT', 27017))
    app.config['MONGODB_USERNAME'] = os.environ.get('DB_USER', '')
    app.config['MONGODB_PASSWORD'] = os.environ.get('DB_PASS', '')

    db.init_app(app)

    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    from .main import main as main_blueprint
    from .api import api as api_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)

    api_rest = Api(app, prefix='/api')

    # adicionar rotas
    from .api import routes
    routes.route_all_resources(api_rest)

    return app
