import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.util import symbol

from biggest_loser.data.modelbase import SqlAlchemyBase


class Season(SqlAlchemyBase):
    __tablename__ = 'seasons'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, index=True)
    start_date = sa.Column(sa.DateTime)
    end_date = sa.Column(sa.DateTime)
    buy_in = sa.Column(sa.Float)

    user = orm.relation('SeasonUser', back_populates='season')
