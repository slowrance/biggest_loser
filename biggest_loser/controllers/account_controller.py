from pyramid.view import view_config
from pyramid.request import Request

# @view_config(route_name='home', renderer="biggest_loser:templates/home/index.pt")
# def home_index(request):
#     return {'project': 'biggest_loser'}

# ################### INDEX ###############################

@view_config(route_name='account_home',
             renderer='biggest_loser:templates/account/index.pt',
             request_method='GET')
def index(request: Request):
    return {}

# ################### LOGIN ###############################

@view_config(route_name='login',
             renderer='biggest_loser:templates/account/login.pt',
             request_method='GET')
def login_get(request: Request):
    return {}

@view_config(route_name='login',
             renderer='biggest_loser:templates/account/login.pt',
             request_method='POST')
def login_post(request: Request):
    return {}

# ################### REGISTER ###############################

@view_config(route_name='register',
             renderer='biggest_loser:templates/account/register.pt',
             request_method='GET')
def register_get(request: Request):
    return {}

@view_config(route_name='register',
             renderer='biggest_loser:templates/account/register.pt',
             request_method='POST')
def register_post(request: Request):
    return {}

# ################### LOGOUT ###############################

@view_config(route_name='logout')
def logout(request: Request):
    return {}
