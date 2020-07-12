from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . import models

class RegisterForm(forms.ModelForm):

	mpassword	= forms.CharField(label='Password', widget=forms.PasswordInput)
	repeat_pw	= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

	class Meta:

		model	= models.User
		fields	= ('phone_number', )

	def save(self, commit=True):
		# Save the password in hashed format

		user = super().save(commit=False)
		user.set_password(self.clean_repeatpw)

		if commit:
			user.save()

		return user

	@property
	def clean_phonenumber(self):

		phone_number	= self.cleaned_data.get('phone_number')

		return phone_number

	@property
	def clean_repeatpw(self):

		mpassword	= self.cleaned_data.get('mpassword')
		repeat_pw	= self.cleaned_data.get('repeat_pw')

		if mpassword and repeat_pw and mpassword != repeat_pw:
			raise forms.ValidationError("Passwords do not match.")

		return repeat_pw

class LoginForm(forms.ModelForm):

	password	= forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:

		model	= models.User
		fields	= ('phone_number', )
