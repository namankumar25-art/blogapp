from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from posts.models import Post
from django.forms import ModelForm
from .models import Profile

class UserRegisterForm(UserCreationForm):

	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username', 'email', 'password1', 'password2']


class PostCreateForm(ModelForm):
	class Meta:
		model=Post
		fields=['title', 'content', 'published', 'state']

class UserUpdateForm(ModelForm):

	email=forms.EmailField

	class Meta:
		model=User
		fields=['username', 'email']

class ProfileUpdateForm(ModelForm):
	
	class Meta:
		model=Profile
		fields=['image']
