import abc
from typing import List
from sqlalchemy.exc import OperationalError

from lib.exceptions import DBCannotBeConnectedError
from modules.orm import Base


class AbstractRepository(metaclass=abc.ABC):

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

    def _add(self, obj: Base) -> None:
        pass

    def _get(self, row_id: int) -> Base:
        pass

    def _get_all(self) -> List:
        pass

    def _delete(self, row_id: int) -> None:
        pass

    def _update(self, obj: Base) -> None:
        pass