from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse 

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(state='published')

class Post(models.Model):

	state_options=(
		('draft', 'Draft'),
		('published', 'Published'),
		)
	title=models.CharField(max_length=100)
	content=models.TextField()
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	published=models.DateTimeField(default=timezone.now)
	updated=models.DateTimeField(auto_now=True)
	state=models.CharField(max_length=100, choices=state_options, default='draft')

	# publish_manager=PublishedManager()

	class Meta:
		ordering=('-published',)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('post-detail',kwargs={'pk':self.pk})
