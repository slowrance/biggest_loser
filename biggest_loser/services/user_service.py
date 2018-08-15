from biggest_loser import DbSession
from biggest_loser.data.users import User
from biggest_loser.data.seasons import Season


def get_users():
    session = DbSession.factory()
