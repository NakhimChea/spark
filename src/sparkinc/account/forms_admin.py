from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . import models

class UserAdminCreationForm(forms.ModelForm):

	mpassword	= forms.CharField(label='Password', widget=forms.PasswordInput)
	repeat_pw	= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:

		model	= models.User
		fields	= ('phone_number', )

	def clean_repeatpw(self):

		mpassword	= self.cleaned_data.get('mpassword')
		repeat_pw	= self.cleaned_data.get('repeat_pw')

		if mpassword and repeat_pw and mpassword != repeat_pw:
			raise form.ValidationError("Password does not match.")

		return repeat_pw

	def save(self, commit=True):
		# Save the password in hashed format

		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['mpassword'])
		
		if commit:
			user.save()

		return user

class UserAdminChangeForm(forms.ModelForm):

	password = ReadOnlyPasswordHashField()

	class Meta:

		model	= models.User
		fields	= ('phone_number', 'password', 'active', 'admin')

	def clean_password(self):

		return self.initial['password']