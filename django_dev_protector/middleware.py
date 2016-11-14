from os import environ
from re import match

from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin
from .settings import TEMPLATE_NAME, REDIRECT_URL, PROTECT_STATUS_VARIABLE, PROTECT_HASH_VARIABLE


class ControlMiddleware(MiddlewareMixin):
    def process_request(self, request):
        url = match(r'^/django_dev_protector/(?P<hash>\w+)/(?P<status>(on)|(off))/$', request.path)
        if url and url.group('hash') == environ[PROTECT_HASH_VARIABLE]:
            if url.group('status') == 'on':
                status = 'True'
            else:
                status = 'False'
            from .setup import save_status
            environ[PROTECT_STATUS_VARIABLE] = status
            save_status(status)
            return redirect('/')

        if environ.get(PROTECT_STATUS_VARIABLE) == 'True':
            from django.shortcuts import render
            return render(request, TEMPLATE_NAME, {
                'redirect_url': REDIRECT_URL
            })
