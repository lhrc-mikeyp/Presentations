"""Hello World using WebOb, Paste + WSGI """

from webob import Response
from webob.dec import wsgify

from paste import httpserver
from paste.deploy import loadapp

INI_PATH = '/home/mikeyp/Documents/Projects/OpenStack/presentations/api_examples/wsgi_webob.ini'

@wsgify
def application(request):

    return Response('Hello, World of WebOb !')


def app_factory(global_config, **local_config):
    return application

wsgi_app = loadapp('config:' + INI_PATH)

httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)
