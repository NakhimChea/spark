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

# ------------------------------ Pages -------------------------------------
from . import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf.urls import url

from django.contrib.auth.decorators import login_required

class Pages:

	@staticmethod
	def register(request):

		form = forms.RegisterForm()
		if request.method == 'POST':

			form = forms.RegisterForm(request.POST)

			if form.is_valid():

				form.save()
				messages.success(request, 
					'Account was created for phone number: ' + form.clean_phonenumber)

				return redirect('login')

		context = {'form': form}

		return render(request, 'account/register.html', context)

	@staticmethod
	def login(request):

		form = forms.LoginForm()
		if request.method == 'POST':

			user	= authenticate(request, 
				phone_number=request.POST.get('phone_number'), 
				password=request.POST.get('password'))

			if user is not None:
				
				login(request, user)

				return redirect('dashboard')

			else:

				messages.info(request, 'Phone Number and Password are not matched.')

		context = {'form': form}

		return render(request, 'account/login.html', context)

	@staticmethod
	def logout(request):

		logout(request)
		messages.success(request, 'You have logged out.')

		return redirect('home')
		
	@staticmethod
	def home(request):

		context = {}

		return render(request, 'account/home.html', context)

	@staticmethod
	@login_required(login_url='login')
	def dashboard(request):

		context = {}

		return render(request, 'account/dashboard.html', context)
