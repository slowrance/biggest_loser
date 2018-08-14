from biggest_loser import DbSession
from biggest_loser.data.season_users import SeasonUser
from biggest_loser.data.seasons import Season


def user_count():
    session = DbSession.factory()

    return session.query(SeasonUser).filter(SeasonUser.season_id == 2).count()


def cash_count():
    session = DbSession.factory()
    return session.query(SeasonUser).filter(SeasonUser.season_id == 2, SeasonUser.for_cash == 1).count()


def prize_pool():
    session = DbSession.factory()
    query_result = session.query(Season.buy_in).filter(Season.id == 2).first()
    result = query_result[0] * 4
    return f'{result:.2f}'
