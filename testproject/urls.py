
from django.contrib import admin
from django.urls import path
from django.conf import settings
from salonsamochodowyapp.views import home
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    re_path(r'^media_car/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

