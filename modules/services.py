from sqlalchemy import exc

from modules import unit_of_work
from lib.log import get_logger
from modules.orm import User


LOG = get_logger(__name__)


class UserService:

    def __init__(self):
        self.uow = unit_of_work.SqlAlchemyUnitOfWork()

    def create_user(self, data: dict) -> dict:
        LOG.debug('CREATING USER')

        user = User(**data)
        LOG.debug(f'user:  {user!r},\n')

        with self.uow:
            try:
                self.uow.users.add(user)
                self.uow.commit()
            except exc.IntegrityError:
                raise Exception('USER DOES NOT EXIST')

        LOG.debug(f'user:  {user!r},\n')
        return user.__dict__

    def get_user(self):
        pass

    def get_all_users(self):
        pass

    def update_user(self):
        pass

    def delet_user(self):
        pass

    def authenticate_user(self):
        pass
