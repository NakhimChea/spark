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
		user.set_password(self.cleaned_data['mpassword'])

		if commit:
			user.save()

		return user

	'''
	def clean_phonenumber(self):

		phone_number	= self.cleaned_data.get('phone_number')
		queryset		= model.User.objects.filter(phone_number=phone_number)

		if queryset.exists():
			raise forms.ValidationError("Phone Number inputed existed.")

		return phone_number

	def clean_repeatpw(self):

		mpassword	= self.cleaned_data.get('mpassword')
		repeat_pw	= self.cleaned_data.get('repeat_pw')

		if mpassword and repeat_pw and mpassword != repeat_pw:
			raise form.ValidationError("Passwords do not match.")

		return repeat_pw
	'''