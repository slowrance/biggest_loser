import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from biggest_loser.data.modelbase import SqlAlchemyBase


class Weight(SqlAlchemyBase):
    __tablename__ = 'weights'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    weight = sa.Column(sa.Float)
    date = sa.Column(sa.DateTime, default=datetime.datetime.now)

    user_id = sa.Column(sa.String, sa.ForeignKey('users.code_name'))
    user = orm.relation('User', back_populates='weights')
