from os import environ
from re import match

from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from .settings import TEMPLATE_NAME, REDIRECT_URL, PROTECT_STATUS_VARIABLE


class ControlMiddleware(MiddlewareMixin):
    def process_request(self, request):
        url = match(r'^/django_dev_protector/$', request.path)
        if url and request.method == 'POST':
            import json
            data = json.loads(request.body.decode('utf-8'))
            if data['key'] == settings.SECRET_KEY:
                from .setup import save_status
                environ[PROTECT_STATUS_VARIABLE] = str(data['status'])
                save_status(str(data['status']))
                return redirect('/')

        if environ.get(PROTECT_STATUS_VARIABLE) == 'True':
            from django.shortcuts import render
            return render(request, TEMPLATE_NAME, {
                'redirect_url': REDIRECT_URL
            })
