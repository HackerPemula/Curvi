from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile
from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
session = SessionStore()

REQUIRED_URLS = []
if hasattr(settings, 'LOGIN_REQUIRED_URLS'):
    REQUIRED_URLS += [compile(expr) for expr in settings.LOGIN_REQUIRED_URLS]

class AuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info.lstrip('/')
        if not any(m.match(path) for m in REQUIRED_URLS):
            return
        # assert hasattr(request, 'user'), "The Login Required middleware requires authentication middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes 'django.core.context_processors.auth'."

        if 'ActiveUser' not in request.session:
            return HttpResponseRedirect(settings.LOGIN_URL)
                