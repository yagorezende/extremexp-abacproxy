class KeycloakMiddlewareError(Exception):
    """
    Base class for all Keycloak middleware errors.
    """
    def __init__(self):
        self.message = "Keycloak middleware error."
        self.error_code = 500


class MissingTokenError(KeycloakMiddlewareError):
    """
    This error is raised when the request does not contain a token.
    """
    def __init__(self):
        super().__init__()
        self.message = "Missing token. Please send a token in the Authorization header."
        self.error_code = 401


class InvalidTokenError(KeycloakMiddlewareError):
    """
    This error is raised when the token is invalid.
    """
    def __init__(self):
        super().__init__()
        self.message = "Invalid token. Please send a valid token in the Authorization header."
        self.error_code = 401


class UnauthorizedError(KeycloakMiddlewareError):
    """
    This error is raised when the user is not authorized to perform the action.
    """
    def __init__(self):
        super().__init__()
        self.message = "Unauthorized. You do not have permission to perform this action."
        self.error_code = 403


class MissingScopeError(KeycloakMiddlewareError):
    """
    This error is raised when the request does not contain a 'scope' parameter.
    """
    def __init__(self):
        super().__init__()
        self.message = "Missing valid scope. Please send a valid scope in the request header."
        self.error_code = 403


class MalformedRequestError(KeycloakMiddlewareError):
    """
    This error is raised when the request does not contain a 'to' parameter.
    """

    def __init__(self):
        super().__init__()
        self.message = "Malformed request. The request must contain a 'to' parameter."
        self.error_code = 400
