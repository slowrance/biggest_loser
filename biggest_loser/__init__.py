import os
from pyramid.config import Configurator
from biggest_loser.data.db_session import DbSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    init_includes(config)
    init_db(config)
    init_routing(config)
    return config.make_wsgi_app()


def init_includes(config):
    config.include('pyramid_chameleon')


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # home controller
    config.add_route('home', '/')
    config.add_route('about', '/about')

    # account controller
    config.add_route('account_home', '/account')
    config.add_route('login', '/account/login')
    config.add_route('register', '/account/register')
    config.add_route('logout', '/account/logout')

    config.scan()


def init_db(config):
    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'db',
            'biggest_loser.sqlite'
        ))
    DbSession.global_init(db_file)
