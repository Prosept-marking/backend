import os

from fastapi_users.authentication import (AuthenticationBackend,
                                          CookieTransport, JWTStrategy)

cookie_transport = CookieTransport(cookie_name='cookie', cookie_max_age=3600)

SECRET = os.environ.get('SECRET_JWT')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
