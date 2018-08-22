from pyramid.view import view_config
from biggest_loser.services import season_user_service
from biggest_loser.viewmodels.home.home_index_viewmodel import HomeIndexViewModel


@view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
def home_index(request):
    vm = HomeIndexViewModel(request)

    return vm.to_dict()


@view_config(route_name='about', renderer="biggest_loser:templates/home/about.pt")
def home_about(request):
    vm = HomeIndexViewModel(request)
    return vm.to_dict()
