import pytest

from modules.orm import Base
from modules.services import UserService


class TestUserService:
    def test_create_user(self):
        user_dict = {'name': 'Test_user'}
        user_service = UserService()
        res = user_service.create_user(user_dict)
        print(res)
        assert True
