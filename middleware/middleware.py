from flask import Flask
from werkzeug import Response
from werkzeug.middleware.proxy_fix import ProxyFix

from middleware.errors import *
from middleware.keycloak import KeycloakConnect


class KeycloakMiddleware(ProxyFix):
    """
    Middleware to handle Keycloak authentication and authorization.
    """

    def __init__(self, app: Flask):
        super().__init__(app.wsgi_app)
        self.keycloak = KeycloakConnect(
            server_url=app.config['KEYCLOAK_SERVER_URL'],
            realm_name=app.config['OIDC_RP_REALM_ID'],
            client_id=app.config['OIDC_RP_CLIENT_ID'],
            client_secret_key=app.config['OIDC_RP_CLIENT_SECRET']
        )

    def __call__(self, environ, start_response):
        try:
            if not self._is_token_valid(environ):
                raise InvalidTokenError()
            if not self._is_token_authorized(environ):
                raise UnauthorizedError()
        except KeycloakMiddlewareError as e:
            return Response(e.message, status=e.error_code)(environ, start_response)
        return self.app(environ, start_response)

    def _get_request_token(self, environ) -> str:
        """
        Get the bearer token from the request. Raise an error if it doesn't exist.
        :param environ: Object with request information.
        :return: token as string.
        """
        try:
            if not environ.get('HTTP_AUTHORIZATION'):
                raise MissingTokenError()
            if not environ.get('HTTP_AUTHORIZATION').startswith('Bearer '):
                raise InvalidTokenError()
            return environ.get('HTTP_AUTHORIZATION').split(' ')[1]  # Bearer token
        except Exception:
            raise InvalidTokenError()

    def _get_request_scope(self, environ):
        """
        Get the scope from the request header.
        :param environ: Object with request information.
        :return: scope as string.
        """
        scope = environ.get('HTTP_AUTHORIZATION_SCOPE')

        if scope:
            return scope
        # return 'read' if the request is a GET request
        if not scope and environ.get('REQUEST_METHOD') == 'GET':
            return 'read'
        # return 'write' if the request is a POST|PUT|PATCH request
        if not scope and environ.get('REQUEST_METHOD') in ['POST', 'PUT', 'PATCH']:
            return 'write'
        # return 'destroy' if the request is a DELETE request
        if not scope and environ.get('REQUEST_METHOD') == 'DELETE':
            return 'destroy'
        raise MissingScopeError()

    def _is_token_valid(self, environ):
        """
        Check if the token is valid.
        """
        return self.keycloak.is_token_active(self._get_request_token(environ))

    def _get_proxy_target(self, environ):
        """
        Get the target URL from the request.
        Note: This method will raise an error if the 'to' parameter is not present in the request.
        """

        forward_url: str = environ.get('werkzeug.request').args.get('to')
        if forward_url is None:
            raise MalformedRequestError()

        # remove the http*://*/ prefix
        if forward_url.startswith('http'):
            forward_url = forward_url.split('://')[1]
            if forward_url.find('/') != -1:
                forward_url = forward_url[forward_url.find('/'):]
            else:
                forward_url = '/'
        return forward_url

    def _is_token_authorized(self, environ):
        """
        Check if the token is authorized.
        """
        uri = self._get_proxy_target(environ)
        token = self._get_request_token(environ)
        scope = self._get_request_scope(environ)
        return self.keycloak.has_context_access(token, uri, scope)
