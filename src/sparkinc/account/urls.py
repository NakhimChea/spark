from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)


urlpatterns = [
	url(r'', include(router.urls)),

	url(r'^register/', views.Pages.register),
	url(r'^login/', views.Pages.login, name='login'),
	url(r'^logout/', views.Pages.logout, name='logout'),
	url(r'^home/', views.Pages.home, name='home'),
	url(r'^dashboard/', views.Pages.dashboard, name='dashboard'),

]
