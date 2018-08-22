from typing import List

from sqlalchemy.orm import joinedload

from biggest_loser import DbSession
from biggest_loser.data.season_users import SeasonUser
from biggest_loser.data.seasons import Season
from biggest_loser.data.users import User


def user_count():
    session = DbSession.factory()

    return session.query(SeasonUser).filter(SeasonUser.season_id == 2).count()


def cash_count():
    session = DbSession.factory()
    return session.query(SeasonUser).filter(SeasonUser.season_id == 2, SeasonUser.for_cash == 1).count()


def prize_pool():
    session = DbSession.factory()
    query_result = session.query(Season.buy_in).filter(Season.id == 2).first()
    result = query_result[0] * cash_count()
    return f'{result:.2f}'


def get_current_season_id():
    session = DbSession.factory()
    return session.query(SeasonUser.season_id).order_by(SeasonUser.season_id.desc()).first()[0]


def get_users(season: Season = get_current_season_id()) -> List[User]:
    session = DbSession.factory()
    users = []
    result = session.query(SeasonUser).options(
        joinedload(SeasonUser.user)
            .joinedload(User.weights)
    ).filter(SeasonUser.season_id == season).all()
    for season_user in result:
        users.append(season_user.user)
    return users
