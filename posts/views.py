from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from users.forms import PostCreateForm
from django.contrib import messages
from django.core.paginator import Paginator

@login_required(login_url='login')
def home(request):
	return render(request, 'posts/home.html')

@login_required(login_url='login')
def about(request):

	return render(request, 'posts/about.html')

@login_required(login_url='login')
def post_list(request):
	posts = Post.objects.all().order_by('-published')

	paginator=Paginator(posts, 3)
	page_number=request.GET.get('page')
	page_obj=paginator.get_page(page_number)

	return render(request, 'posts/post_list.html', {'page_obj':page_obj})

@login_required(login_url='login')
def my_list(request):
	posts = Post.objects.filter(author=request.user).order_by('-published')

	paginator=Paginator(posts, 3)
	page_number=request.GET.get('page')
	page_obj=paginator.get_page(page_number)

	return render(request, 'posts/my_list.html', {'page_obj':page_obj})

@login_required(login_url='login')
def user_posts(request, author):
	posts = Post.objects.filter(author=author).order_by('-published')

	paginator=Paginator(posts, 3)
	page_number=request.GET.get('page')
	page_obj=paginator.get_page(page_number)

	return render(request, 'posts/user_posts.html', {'page_obj':page_obj})


@login_required
def post_detail(request, id):
	post=Post.objects.get(id=id)

	return render(request, 'posts/post_detail.html', {'post':post})

@login_required
def create(request):
	if request.method=='POST':
		form=PostCreateForm(request.POST)
		form.instance.author=request.user
		if form.is_valid():			
			form.save()
			title=form.cleaned_data.get('title')
			
			messages.success(request, f"{title} created successfully")
			return redirect('post-detail', id=form.instance.id)

	else:
		form=PostCreateForm()

	return render(request, "posts/post_create.html", {'form':form, 'author':request.user})

@login_required
def update(request, id):
	
	post=Post.objects.get(pk=id)
	if request.user==post.author:
		
		if request.method=='POST':
			form=PostCreateForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
				return redirect('post-detail', id=id)

		else:
			form=PostCreateForm(instance=post)

		return render(request, 'posts/post_create.html',{'form':form, 'post':post})

@login_required
def delete(request, id):

	post=Post.objects.get(id=id)
	if request.user==post.author:
		
		if request.method=='POST':

			post.delete()
			return redirect('post-list')

		return render(request, 'posts/post_delete.html', {'post':post})