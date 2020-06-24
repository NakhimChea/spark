from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
from . import forms_admin

class UserAdmin(BaseUserAdmin):

	form = forms_admin.UserAdminChangeForm
	add_form = forms_admin.UserAdminCreationForm

	# The fields to be used in displaying the User Model
	# These override the base UserAdmin

	list_display	= ('ID', 'phone_number', 'admin')
	list_filter		= ('admin', )
	fieldsets		= (
		('Account',			{'fields': ('phone_number', 'password')}),
		#('Personal Info',	{'fields': ()}),
		('Permissions',		{'fields': ('active', 'staff', 'admin', )}),
	)

	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin 
	# overrides get_fieldsets to use this attribute when creating new user.
	
	add_fieldsets		= (
		('Account',	{'classes'	: ('wide', ), 
					'fields'	: ('phone_number', 'mpassword', 'repeat_pw')}
		),
	)
	search_fields		= ('ID', 'phone_number', )
	ordering			= ('ID', 'phone_number', )
	filter_horizontal	= ()

# Register to admin page
admin.site.register(models.User, UserAdmin)

# Remove from admin page
#admin.site.unregister(Group)