from rest_framework import serializers
from django.contrib.auth.models import Group

from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model	= models.User
		fields	= ['url', 'ID', 'get_full_name', 'phone_number'] #, 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model	= Group
		fields	= ['url', 'id', 'name']
