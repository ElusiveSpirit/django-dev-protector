django-dev-protector
====================
The app for freelance developers, that blocks site if needed.  

It can be used in situations when a client don't want to pay your work. The app blocks all requests to the site and shows a template.

Installation
------------
settings.py
```
INSTALLED_APPS = [
    ...

    # import django_dev_protector
    'django_dev_protector',
]


MIDDLEWARE = [
    # set middleware class
    'django_dev_protector.middleware.ControlMiddleware',

    ...
]
```

Settings
--------
```
# render a simple template
PROTECT_TEMPLATE_NAME = 'django_dev_protector/index.html'

# if redirect url is set, then default template would be  
# redirects person after 10 sec
PROTECT_REDIRECT_URL = None
```
