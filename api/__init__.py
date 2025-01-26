import os

from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_restx import Api

from api.proxy import Proxy
from middleware.middleware import KeycloakMiddleware

load_dotenv()

app = Flask(__name__)

with app.app_context():
    app.config['KEYCLOAK_SERVER_URL'] = os.getenv('KEYCLOAK_SERVER_URL')
    app.config['OIDC_OP_AUTHORIZATION_ENDPOINT'] = os.getenv('OIDC_OP_AUTHORIZATION_ENDPOINT')
    app.config['OIDC_OP_TOKEN_ENDPOINT'] = os.getenv('OIDC_OP_TOKEN_ENDPOINT')
    app.config['OIDC_OP_USER_ENDPOINT'] = os.getenv('OIDC_OP_USER_ENDPOINT')
    app.config['OIDC_OP_JWKS_ENDPOINT'] = os.getenv('OIDC_OP_JWKS_ENDPOINT')
    app.config['OIDC_OP_LOGOUT_ENDPOINT'] = os.getenv('OIDC_OP_LOGOUT_ENDPOINT')
    app.config['OIDC_OP_ENDSESSION_ENDPOINT'] = os.getenv('OIDC_OP_ENDSESSION_ENDPOINT')
    app.config['OIDC_OP_LOGOUT_URL_METHOD'] = os.getenv('OIDC_OP_LOGOUT_URL_METHOD')
    app.config['OIDC_RP_CLIENT_ID'] = os.getenv('OIDC_RP_CLIENT_ID')
    app.config['OIDC_RP_REALM_ID'] = os.getenv('OIDC_RP_REALM_ID')
    app.config['OIDC_RP_CLIENT_SECRET'] = os.getenv('OIDC_RP_CLIENT_SECRET')
    app.config['OIDC_RP_SIGN_ALGO'] = os.getenv('OIDC_RP_SIGN_ALGO')

    app.wsgi_app = KeycloakMiddleware(app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)
app.add_url_rule('/proxy', view_func=Proxy.as_view('proxy'))
