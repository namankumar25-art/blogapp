from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(func):

	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('post-home')
		else:
			return func(request, *args, **kwargs)

	return wrapper_func