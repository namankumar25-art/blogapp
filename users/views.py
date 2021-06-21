from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from blog.decorators import authenticated_user

@authenticated_user
def register(request):
	
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('login')

	else:
		form=UserRegisterForm()

	return render(request, "users/register.html", {'form':form})

@authenticated_user
def userlogin(request):

	if request.method=='POST':
				
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('post-home')	

	return render(request, 'users/login.html',{})

def userlogout(request):
	logout(request)
	return redirect('login')

def profile(request):

	if request.method=="POST":

		user_update_form=UserUpdateForm(request.POST, instance=request.user)
		profile_update_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_update_form.is_valid() and profile_update_form.is_valid():
			user_update_form.save()
			profile_update_form.save()
			messages.success(request, f'Profile Updated')
			return redirect('profile')

	else:

		user_update_form=UserUpdateForm(instance=request.user)
		profile_update_form=ProfileUpdateForm(instance=request.user.profile)

	context={
		'user_update_form':user_update_form, 
		'profile_update_form':profile_update_form
		}

	return render(request, "users/profile.html", context)