from django.db import models

from django.contrib.auth.models import (
	AbstractBaseUser, 
	BaseUserManager,
	PermissionsMixin,
	)

from django.core.validators import RegexValidator
#from django_countries.fields import CountryField
	
class UserManager(BaseUserManager):
	def create_user(self, phone_number, password=None):
		# Create and save a User with the given phone number and password

		if not phone_number:
			raise ValueError('User must have a phone number for account.')

		user = self.model(phone_number=phone_number,)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_staffuser(self, phone_number, password):
		# Create and save a staff User with the given phone number and pw

		user = self.create_user(phone_number, password=password, )
		user.staff = True
		user.save(using=self._db)

		return user

	def create_superuser(self, phone_number, password):
		# Create and save an admin User with the given phone number and pw

		user = self.create_user(phone_number, password=password, )
		user.staff = True
		user.admin = True
		user.save(using=self._db)

		return user

class User(AbstractBaseUser, PermissionsMixin):

	phone_regex		= RegexValidator(regex=r'^\+?1?\d{9,13}$',
		message="Phone number must be entered in the format: '+999999999'. \
				Up to 13 digits allowed.")
	ID				= models.AutoField(primary_key=True)
	phone_number	= models.CharField("Phone Number", blank=False,
		validators=[phone_regex], max_length=13, unique=True)
	# Password Field is built in
	active			= models.BooleanField(default=True)
	staff			= models.BooleanField(default=False)
	admin			= models.BooleanField(default=False)

	objects			= UserManager()

	USERNAME_FIELD	= 'phone_number'
	REQUIRED_FIELDS	= []

	def get_full_name(self):

		return str(self.phone_number)

	def get_short_name(self):

		return str(self.phone_number)

	def __str__(self):

		return str(self.phone_number)
	
	@property
	def is_active(self):

		return self.active

	@property
	def is_staff(self):

		return self.staff

	@property
	def is_superuser(self):

		return self.admin
