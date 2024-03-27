
from django.contrib import admin
from django.urls import path
from django.conf import settings
from salonsamochodowyapp.views import home
from django.views.static import serve
from django.urls import re_path

def trigger_error(request):
    division_by_zero = 1 / 0

def trigger_error2(request):
    request["Error"]

def trigger_error3(request):
    result = int('error')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    re_path(r'^media_car/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    path('sentry-debug/', trigger_error3),
]