from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^api/', include('api.urls')),
    url('auth/', include('djoser.urls')),
    url('auth/', include('djoser.urls.authtoken')),
    url('auth/', include('djoser.urls.jwt')),
]
