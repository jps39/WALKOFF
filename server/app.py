import os, logging

from jinja2 import Environment, FileSystemLoader
from core import helpers
from core.config import paths
import connexion
from gevent import monkey
from flask_security.utils import encrypt_password
from flask import Blueprint, g
monkey.patch_all()


app_page = Blueprint('appPage', 'apps', template_folder=os.path.abspath('apps'), static_folder='static')

def create_app():
    connexion_app = connexion.App(__name__, specification_dir='swagger/')
    app = connexion_app.app
    #app.json_encoder = JSONEncoder
    app.jinja_loader = FileSystemLoader(['server/templates'])

    app.config.update(
            # CHANGE SECRET KEY AND SECURITY PASSWORD SALT!!!
            SECRET_KEY = "SHORTSTOPKEYTEST",
            SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath(paths.db_path),
            SECURITY_PASSWORD_HASH = 'pbkdf2_sha512',
            SECURITY_TRACKABLE = False,
            SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production',
            SECURITY_POST_LOGIN_VIEW = '/',
            WTF_CSRF_ENABLED = False,
            STATIC_FOLDER=os.path.abspath('server/static')
        )



    app.config["SECURITY_LOGIN_USER_TEMPLATE"] = "login_user.html"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    connexion_app.add_api('api.yaml')

    app.register_blueprint(app_page, url_prefix='/apps/<app>')
    return app

# Template Loader
env = Environment(loader=FileSystemLoader("apps"))
app = create_app()

# Creates Test Data
@app.before_first_request
def create_user():
    from server.context import running_context
    from . import database

    running_context.db.create_all()

    if not database.User.query.first():
        admin_role = running_context.user_datastore.create_role(name='admin',
                                                                description='administrator',
                                                                pages=database.default_urls)

        u = running_context.user_datastore.create_user(email='admin', password=encrypt_password('admin'))
        running_context.user_datastore.add_role_to_user(u, admin_role)
        running_context.db.session.commit()

    apps = set(helpers.list_apps()) - set([_app.name
                                           for _app in running_context.db.session.query(running_context.App).all()])
    app.logger.debug('Found apps: {0}'.format(apps))
    for app_name in apps:
        running_context.db.session.add(running_context.App(app=app_name, devices=[]))
    running_context.db.session.commit()

    running_context.CaseSubscription.sync_to_subscriptions()

    app.logger.handlers = logging.getLogger('server').handlers


@app_page.url_value_preprocessor
def static_request_handler(endpoint, values):
    g.app = values.pop('app', None)
    app_page.static_folder = os.path.abspath(os.path.join('apps', g.app, 'interface', 'static'))
