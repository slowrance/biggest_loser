import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from biggest_loser.data.weights import Weight

from biggest_loser.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    code_name = sa.Column(sa.String, primary_key=True)
    fname = sa.Column(sa.String)
    lname = sa.Column(sa.String)
    email = sa.Column(sa.String, index=True)
    hashed_password = sa.Column(sa.String, index=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    profile_img_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    weights = orm.relation('Weight', order_by=Weight.date, back_populates='user')
    seasons = orm.relation('SeasonUser', back_populates='user')
