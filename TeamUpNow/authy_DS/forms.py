from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from authy_DS.models import Profile_DS



from OptionField_DS.models import INDUSTRY_AND_PROJECT_TYPES


from skills_TaggingField.models import (
						ProvidedBenefits,
						ProvidedVacationTypes,
						ProvidedInsuranceTypes,
						ProductsAndervices,

						)




def ForbiddenUsers(value):
	forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root',
	'email', 'user', 'join', 'sql', 'static', 'python', 'delete']
	if value.lower() in forbidden_users:
		raise ValidationError('Invalid name for user, this is a reserverd word.')

def InvalidUser(value):
	if '@' in value or '+' in value or '-' in value:
		raise ValidationError('This is an Invalid user, Do not user these chars: @ , - , + ')

def UniqueEmail(value):
	if User.objects.filter(email__iexact=value).exists():
		raise ValidationError('User with this email already exists.')

def UniqueUser(value):
	if User.objects.filter(username__iexact=value).exists():
		raise ValidationError('User with this username already exists.')



class SignupForm_DS(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(), max_length=30, required=True,)
	email = forms.CharField(widget=forms.EmailInput(), max_length=100, required=True,)
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Confirm your password.")

	class Meta:

		model = User
		fields = ('username', 'email', 'password')

	def __init__(self, *args, **kwargs):
		super(SignupForm_DS, self).__init__(*args, **kwargs)
		self.fields['username'].validators.append(ForbiddenUsers)
		self.fields['username'].validators.append(InvalidUser)
		self.fields['username'].validators.append(UniqueUser)
		self.fields['email'].validators.append(UniqueEmail)

	def clean(self):
		super(SignupForm_DS, self).clean()
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')

		if password != confirm_password:
			self._errors['password'] = self.error_class(['Passwords do not match. Try again'])
		return self.cleaned_data





# class LoginForm_DS(forms.ModelForm):
# 	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium', "placeholder":'username'}), max_length=30, required=True,)
# 	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input is-medium', "placeholder":'email'}), max_length=100, required=True,)
# 	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium', "placeholder":'password'}))

# 	class Meta:

# 		model = User
# 		fields = ('username', 'email', 'password')
# 		labels = {
#         'username': 'username',
# 		'email': 'email',
# 		'password': 'password',
# 		}

# 	def __init__(self, *args, **kwargs):
# 		super(LoginForm_DS, self).__init__(*args, **kwargs)
# 		self.fields['username'].validators.append(ForbiddenUsers)
# 		self.fields['username'].validators.append(InvalidUser)
# 		self.fields['username'].validators.append(UniqueUser)
# 		self.fields['email'].validators.append(UniqueEmail)

# 	def clean(self):
# 		super(LoginForm_DS, self).clean()
# 		password = self.cleaned_data.get('password')

# 		if password != confirm_password:
# 			self._errors['password'] = self.error_class(['Passwords do not match. Try again'])
# 		return self.cleaned_data




class LoginForm_DS(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
	


class ChangePasswordForm_DS(forms.ModelForm):
	id = forms.CharField(widget=forms.HiddenInput())
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), label="Old password", required=True)
	new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), label="New password", required=True)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), label="Confirm new password", required=True)

	class Meta:
		model = User
		fields = ('id', 'old_password', 'new_password', 'confirm_password')

	def clean(self):
		super(ChangePasswordForm_DS, self).clean()
		id = self.cleaned_data.get('id')
		old_password = self.cleaned_data.get('old_password')
		new_password = self.cleaned_data.get('new_password')
		confirm_password = self.cleaned_data.get('confirm_password')
		user = User.objects.get(pk=id)
		if not user.check_password(old_password):
			self._errors['old_password'] =self.error_class(['Old password do not match.'])
		if new_password != confirm_password:
			self._errors['new_password'] =self.error_class(['Passwords do not match.'])
		return self.cleaned_data

class EditProfileForm_DS(forms.ModelForm):
	picture = forms.ImageField(required=False)
	first_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=True, initial='first name')
	last_name = forms.CharField(widget=forms.TextInput(), max_length=50, required=True, initial='last name')

	industry_and_projects = forms.ChoiceField(widget=forms.Select, choices=INDUSTRY_AND_PROJECT_TYPES, required=False, initial='industry and projects')
	location = forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='location')
	telephone= forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='telephone')
	kaggle = forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='kaggle')
	github= forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='github')
	linkedInn= forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='linkedInn')
	previous_CTO_linkedInn_link= forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='previous CTO linkedInn')
	previous_HRmanager_linkedInn_link= forms.CharField(widget=forms.TextInput(), max_length=50, required=False, initial='previous HRmanager linkedInn')


	class Meta:
		model = Profile_DS
		exclude = ['user', 'created', 'favorites']
		fields = '__all__'
