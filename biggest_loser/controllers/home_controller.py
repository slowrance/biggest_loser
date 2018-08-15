from pyramid.view import view_config
from biggest_loser.services import season_user_service


@view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
def home_index(request):
    users = season_user_service.get_users()

    for u in users:
        lost_weight = None
        start_weight = u.weights[0].weight
        current_weight = u.weights[-1].weight
        u.percent = ((start_weight - current_weight) / start_weight)
        if u.percent >= 0:
            u.lost_weight = True
        u.percent = f'{u.percent:.2%}'

    return {'users': users,
            'user_count': season_user_service.user_count(),
            'cash_players': season_user_service.cash_count(),
            'prize_pool': season_user_service.prize_pool()}


@view_config(route_name='about', renderer="biggest_loser:templates/home/about.pt")
def home_about(request):
    return {'project': 'biggest_loser'}
