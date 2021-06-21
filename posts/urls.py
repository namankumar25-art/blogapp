from django.urls import path, re_path, include
from . import views

urlpatterns=[

	path('', views.home, name='post-home'),	
	path('about/', views.about, name='post-about'),	
	path('articles/', views.post_list, name='post-list'),
	path('articles/create/', views.create, name='post-create'),
	path('articles/mylist/', views.my_list, name='my-list'),
	path('articles/<int:id>/', views.post_detail, name='post-detail'),			
	path('articles/<int:id>/update/', views.update,name='post-update'),
	path('articles/<int:id>/delete/', views.delete, name='post-delete'),
	path('articles/<str:username>/posts/', views.user_posts, name='user-posts'),		
	
]