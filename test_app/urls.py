from django.http import JsonResponse
from django.conf.urls import url
from django.contrib import admin


def index(request):
    return JsonResponse({'site': 'works!'})


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index)
]
