from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
]
