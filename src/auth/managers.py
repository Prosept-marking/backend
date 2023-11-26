import os

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from database import User, get_user_db

SECRET = os.environ.get('SECRET_MANAGER')


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
            self, user: User,
            request: Request | None = None):
        print(f'User {user.id} has registered.')


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
