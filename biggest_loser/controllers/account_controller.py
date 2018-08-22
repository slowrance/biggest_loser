from pyramid.view import view_config
from pyramid.request import Request
import pyramid.httpexceptions as x

# @view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
# def home_index(request):
#     return {'project': 'biggest_loser'}

# ################### INDEX ###############################
from biggest_loser.infrastructure import cookie_auth
from biggest_loser.services import user_service
from biggest_loser.viewmodels.account.account_home_viewmodel import AccountHomeViewModel
from biggest_loser.viewmodels.account.login_viewmodel import LoginViewModel
from biggest_loser.viewmodels.account.register_viewmodel import RegisterViewModel


@view_config(route_name='account_home',
             renderer='biggest_loser:templates/account/index.pt',
             request_method='GET')
@view_config(route_name='account_home/',
             renderer='biggest_loser:templates/account/index.pt',
             request_method='GET')
def index(request: Request):
    vm = AccountHomeViewModel(request)
    if not vm.user:
        return x.HTTPFound('/account/login')
    return vm.to_dict()

# ################### LOGIN ###############################

@view_config(route_name='login',
             renderer='biggest_loser:templates/account/login.pt',
             request_method='GET')
def login_get(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()

@view_config(route_name='login',
             renderer='biggest_loser:templates/account/login.pt',
             request_method='POST')
def login_post(request: Request):
    vm = LoginViewModel(request)
    vm.validate()
    if vm.error:
        return vm.to_dict()

    if not vm.user:
        return vm.to_dict()

    cookie_auth.set_auth(request, vm.user.id)

    return x.HTTPFound('/account')



# ################### REGISTER ###############################

@view_config(route_name='register',
             renderer='biggest_loser:templates/account/register.pt',
             request_method='GET')
def register_get(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@view_config(route_name='register',
             renderer='biggest_loser:templates/account/register.pt',
             request_method='POST')
def register_post(request: Request):
    vm = RegisterViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.fname, vm.lname, vm.code_name, vm.email, vm.password)

    cookie_auth.set_auth(request, user.id)

    return x.HTTPFound('/account')

# ################### LOGOUT ###############################

@view_config(route_name='logout')
def logout(request: Request):
    cookie_auth.logout(request)
    return x.HTTPFound('/')
