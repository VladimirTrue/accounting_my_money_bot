import datetime
import decimal
import uuid
from collections import namedtuple
from decimal import Decimal
from typing import List

from sqlalchemy import Table, Column, MetaData, Numeric, DateTime, String, Integer, \
    ForeignKey, Date, func, select, inspect
from sqlalchemy.orm import registry, relationship, Mapped, mapped_column, \
    DeclarativeBase








#
# period_epenses = Table(
#     'period_expenses', mapper_registry.metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('category', String),
#     Column('value', Numeric(precision=38, scale=4), default=0),
#     Column('budged_period_id', Integer, ForeignKey('budget_periods.id'))
# )
#
# total_daily_expenses = Table(
#     'tota_daily_expenses', mapper_registry.metadata,
#     Column('day', Date, default=func.current_date(), unique=True),
#     Column('value', Numeric(precision=38, scale=4), default=0),
#     Column('budged_period_id', Integer, ForeignKey('budget_periods.id')),
# )
#
# daily_expenses = Table(
#     'dayly_expenses', mapper_registry.metadata,
#     Column('day', ForeignKey('total_daily_expenses.day'), default=func.current_date()),
#     Column('category', String),
#     Column('value', Numeric(precision=38, scale=4))
# )


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    budget_periods: Mapped[List["BudgetPeriod"]] = relationship(back_populates="user", )
    # users = Table(
    #     'users', mapper_registry.metadata,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String),
    # )

    def __repr__(self):
        return f"id: {self.id!r}, name: {self.name!r}, periods: {self.budget_periods!r}"


class BudgetPeriod(Base):

    __tablename__ = 'budget_periods'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    start_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates='budget_periods')
    income: Mapped["PeriodIncome"] = relationship(back_populates='budget_period', )
    expense: Mapped["PeriodExpense"] = relationship(back_populates='budget_period', )

    def __repr__(self):
        return (f"id: {self.id!r}, name: {self.name!r}, start_date: {self.start_date!r}, "
                f"end_date: {self.end_date!r}, user_id: {self.user_id!r}")


class PeriodIncome(Base):

    __tablename__ = 'period_incomes'

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String)
    value: Mapped[Decimal] = mapped_column(Numeric(precision=38, scale=4), default=0)
    budget_period_id: Mapped["BudgetPeriod"] = mapped_column(ForeignKey("budget_periods.id"))

    budget_period: Mapped["BudgetPeriod"] = relationship(back_populates='income')

    def __repr__(self):
        return (f"id: {self.id!r}, category: {self.category!r}, value: {self.value!r}, "
                f"budget_period_id: {self.budget_period_id!r}")


class PeriodExpense(Base):

    __tablename__ = 'period_expenses'

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String)
    value: Mapped[Decimal] = mapped_column(Numeric(precision=38, scale=4), default=0)
    budget_period_id: Mapped["BudgetPeriod"] = mapped_column(ForeignKey("budget_periods.id"))

    budget_period: Mapped["BudgetPeriod"] = relationship(back_populates='expense')

    def __repr__(self):
        return (f"id: {self.id!r}, category: {self.category!r}, value: {self.value!r}, "
                f"budget_period_id: {self.budget_period_id!r}")


class TotalDaylyExpense:
    pass


class DailyExpense:
    pass


# def start_mappers():
#     mapper_registry.map_imperatively(
#         User, users,
#         properties={'budget_periods': relationship(
#             BudgetPeriod,
#             uselist=True)
#         }
#     )
#     #
#     mapper_registry.map_imperatively(
#         BudgetPeriod, budget_periods,
#     )

    # mapper_registry.map_imperatively(PeriodIncome, period_incomes)
    # mapper_registry.map_imperatively(PeriodExpense, period_epenses)


# if __name__ == "__main__":
#     start_mappers()
#     from sqlalchemy.orm import Session
#     from sqlalchemy import create_engine
#
#     engine = create_engine("sqlite://", echo=True)
#     metadata.create_all(engine)
#     with Session(engine) as session:
#         UserType = namedtuple('User', ['id', 'name'])
#         buf = UserType(id='1', name='first')._asdict()
#         orm_dict = {}
#         print(inspect(User))
#         for col in list(inspect(User).columns):
#             col_name = col.__dict__['key']
#             orm_dict[col_name] = buf.get(col_name)
#
#         print(orm_dict)
#         session.add(User(**orm_dict))
#         session.commit()
#         s = select(User)
#         print('-' * 15)
#         for u in session.scalars(s):
#             # col in  (inspect(u).columns):
#             print('@@@ - ', type(u))
#             print('@@@ - ', list(inspect(u)))
#
#         # session.add(User(**orm_dict))
#         # session.commit()


if __name__ == "__main__":

    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    engine = create_engine("sqlite://", echo=True)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        first = User(id=1, name='first_user')
        # second = User(id=2, name='second_user')

        session.add_all([first])
        session.commit()

        stm1 = select(User)

        stm2 = select(BudgetPeriod)

        print('______')
        for u in session.scalars(stm1):
            print('----')
            print(u)

        for b in session.scalars(stm2):
            print(b)


