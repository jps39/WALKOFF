import os

from jinja2 import Environment, FileSystemLoader
from core.config import paths
import connexion
#from .encoder import JSONEncoder

def create_app():
    connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/')
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

    # Template Loader
    env = Environment(loader=FileSystemLoader("apps"))

    app.config["SECURITY_LOGIN_USER_TEMPLATE"] = "login_user.html"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    connexion_app.add_api('api.yaml')
    return app

app = create_app()


