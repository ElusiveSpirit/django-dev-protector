django-dev-protector
====================
The app for freelance developers, that blocks site if needed.

It can be used in situations when a client don't want to pay your work. The app blocks all requests to the site and shows a message of this situation.

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
PROTECT_REDIRECT_URL = 'http://your_client_opponent_site.com/'
```
By default server is unblocked

Usage
-----
You save your django SECRET_KEY from settings
```
SECRET_KEY = '...
```
After you are able to block or unblock site with POST requests
```
{
  "key": <SECRET_KEY>,
  "status": true
}
POST to http://<your_domain>/django_dev_protector/
```
An example
```
curl \
  -H "Content-Type: application/json" \
  -X POST -d '{"key": "<SECRET_KEY>", "status": true}' \
  http://<your_domain>/django_dev_protector/
```
