from pyramid.view import view_config
from biggest_loser.services import season_user_service


def get_test_users():
    return[
        {'codename': "Cryin' Calories", 'percent': .034},
        {'codename': "Water Horse", 'percent': .021},
        {'codename': "Moosin' Around", 'percent': -.012},
    ]

@view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
def home_index(request):
    return {'users': get_test_users(),
            'user_count': season_user_service.user_count(),
            'cash_players': season_user_service.cash_count(),
            'prize_pool': season_user_service.prize_pool()}


@view_config(route_name='about', renderer="biggest_loser:templates/home/about.pt")
def home_about(request):
    return {'project': 'biggest_loser'}
