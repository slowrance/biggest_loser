import os
import datetime
import random
from typing import List

import biggest_loser
from biggest_loser import DbSession
from biggest_loser.data.season_users import SeasonUser
from biggest_loser.data.seasons import Season
from biggest_loser.data.users import User
from biggest_loser.data.weights import Weight


def main():
    init_db()
    seasons = get_seasons()
    insert_users(seasons)


def init_db():
    top_folder = os.path.dirname(biggest_loser.__file__)
    rel_file = os.path.join('db', 'biggest_loser.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    DbSession.global_init(db_file)


def get_seasons() -> List[Season]:
    seasons = []
    s1 = Season()
    s1.name = 'Season 1'
    s1.start_date = datetime.datetime(2018, 8, 1)
    s1.end_date = datetime.datetime(2018, 8, 31)
    s1.buy_in = 10.50
    seasons.append(s1)

    s2 = Season()
    s2.name = 'Season 1'
    s2.start_date = datetime.datetime(2018, 9, 1)
    s2.end_date = datetime.datetime(2018, 9, 30)
    s2.buy_in = 20.00
    seasons.append(s2)

    return seasons


def insert_users(seasons: List[Season]):
    u1 = User()
    u1.code_name = "Moosin' Around"
    u1.fname = 'Steve'
    u1.lname = 'Lowrance'
    u1.email = 'steve.lowrance@gmail.com'
    for s in seasons:
        su = SeasonUser()
        su.season = s
        su.user = u1
        u1.seasons.append(su)
    rand_weights = get_weights()
    for w in rand_weights:
        u1.weights.append(w)
    u2 = User()
    u2.code_name = "Cryin' Calories"
    u2.fname = 'Tara'
    u2.lname = 'Moore'
    u2.email = 'mooretd@gmail.com'
    for s in seasons:
        su = SeasonUser()
        su.season = s
        su.user = u2
        u2.seasons.append(su)
    rand_weights = get_weights()
    for w in rand_weights:
        u2.weights.append(w)

    session = DbSession.factory()
    session.add(u1)
    session.add(u2)
    session.commit()


def get_weights() -> List[Weight]:
    weights = []
    w1 = Weight()
    w1.date = rand_date(datetime.datetime(2018, 8, 1), datetime.datetime(2018, 9, 30))
    w1.weight = random.uniform(150, 300)
    w2 = Weight()
    w2.date = rand_date(datetime.datetime(2018, 8, 1), datetime.datetime(2018, 9, 30))
    w2.weight = random.uniform(150, 300)
    w3 = Weight()
    w3.date = rand_date(datetime.datetime(2018, 8, 1), datetime.datetime(2018, 9, 30))
    w3.weight = random.uniform(150, 300)
    w4 = Weight()
    w4.date = rand_date(datetime.datetime(2018, 8, 1), datetime.datetime(2018, 9, 30))
    w4.weight = random.uniform(150, 300)
    weights.append(w1)
    weights.append(w2)
    weights.append(w3)
    weights.append(w4)
    return weights


def rand_date(start: datetime, end: datetime) -> datetime:
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


if __name__ == '__main__':
    main()
