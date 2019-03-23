from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    session_factory = SignedCookieSessionFactory('Gh4n4Secret',timeout=None)
    config = Configurator(settings=settings,session_factory=session_factory)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('homeInError', '/')
    config.add_route('show_first','/first.pt')
    config.add_route('show_second','/two.pt')
    config.add_route('show_wrong_second','/second.pt')
    config.add_route('show_third','/teesra.pt')
    config.add_route('show_final','/final.pt')
    config.add_route('show_completed','/completed.pt')
    config.add_route('show_game','/game.pt')
    config.add_route('show_hoodie','/hoodie.pt')
    config.add_static_view(name='static', path='puzzle:static')
    config.scan('.views')
    return config.make_wsgi_app()

