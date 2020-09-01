from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'pub', views.PublicationViewSet, basename='pub'),

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls')),
]

# urlpatterns = [
    # path('', include('')),
# ]
