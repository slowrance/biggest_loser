from pyramid.view import view_config


def get_test_users():
    return[
        {'codename': "Cryin' Calories", 'percent': .034},
        {'codename': "Water Horse", 'percent': .021},
        {'codename': "Moosin' Around", 'percent': -.012},
    ]

@view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
def home_index(request):
    return {'users': get_test_users()}


@view_config(route_name='about', renderer="biggest_loser:templates/home/about.pt")
def home_about(request):
    return {'project': 'biggest_loser'}
