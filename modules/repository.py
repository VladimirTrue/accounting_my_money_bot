import abc
from typing import List
from sqlalchemy.exc import OperationalError

from lib.exceptions import DBCannotBeConnectedError
from modules.orm import Base, User


class AbstractRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        ...

    def add(self, obj: Base) -> None:
        self._add(obj)

    def get(self, row_id: int) -> Base:
        return self._get(row_id)

    def get_all(self) -> List:
        return self._get_all()

    def delete(self, row_id: int) -> None:
        return self._delete(row_id)

    def update(self, obj: Base) -> None:
        return self._update(obj)

    @abc.abstractmethod
    def _check_connection(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _add(self, obj: Base) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, row_id: int) -> Base:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_all(self) -> List:
        raise NotImplementedError

    @abc.abstractmethod
    def _delete(self, row_id: int) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _update(self, obj: Base) -> None:
        raise NotImplementedError


class UserSqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        super(UserSqlAlchemyRepository, self).__init__()
        self.session = session
        self._check_connection()

    def _check_connection(self):
        try:
            self.session.connection()
        except OperationalError:
            raise DBCannotBeConnectedError(
                message="Can't connect to Database"
            )

    def _add(self, user: User) -> None:
        self.session.add(user)

    def _get(self, user_id: int) -> User:
        return self.session.query(User).filter_by(id=user_id).one()

    def _get_all(self) -> List:
        return self.session.query(User)

    def _delete(self, user_id: int) -> User:
        return self.session.query(User).filter_by(id=user_id).delete()

    def _update(self, obj: Base) -> None:
        pass
