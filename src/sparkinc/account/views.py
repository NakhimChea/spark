from django.shortcuts import render
from django.contrib.auth.models import Group

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from . import serializers
from . import models

class UserViewSet(viewsets.ModelViewSet):
	# API endpoint that allows authentications to be viewed or edited.
	queryset			= models.User.objects.all().order_by('ID')
	serializer_class	= serializers.UserSerializer
	permission_classes	= [IsAdminUser]

class GroupViewSet(viewsets.ModelViewSet):
	# API endpoint that allows authentication groups to be viewed or edited.
	queryset			= Group.objects.all().order_by('id')
	serializer_class	= serializers.GroupSerializer