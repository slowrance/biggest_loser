from pyramid.view import view_config


@view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
def home_index(request):
    return {'project': 'biggest_loser'}


@view_config(route_name='about', renderer="biggest_loser:templates/home/about.pt")
def home_about(request):
    return {'project': 'biggest_loser'}
