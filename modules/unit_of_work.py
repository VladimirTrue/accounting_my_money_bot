from __future__ import annotations

import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modules import repository
from modules.orm import Base

engine = create_engine("sqlite://", echo=True)

class AbstractUnitOfWork(metaclass=abc.ABCMeta):
    users: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    expire_on_commit=False,
    bind=engine
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        Base.metadata.create_all(engine)
        self.session = session_factory()

    def __enter__(self):
        self.users = repository.UserSqlAlchemyRepository(self.session)
        return super(SqlAlchemyUnitOfWork, self).__enter__()

    def __exit__(self, *args):
        super(SqlAlchemyUnitOfWork, self).__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
