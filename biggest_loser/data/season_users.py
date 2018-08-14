import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from biggest_loser.data.modelbase import SqlAlchemyBase


class SeasonUser(SqlAlchemyBase):
    __tablename__ = 'season_users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    user_id = sa.Column(sa.String, sa.ForeignKey('users.code_name'), index=True)
    user = orm.relation('User', back_populates='seasons')

    season_id = sa.Column(sa.Integer, sa.ForeignKey('seasons.id'), index=True)
    season = orm.relation('Season', back_populates='user')

    for_cash = sa.Column(sa.Boolean, index=True, default=False)
