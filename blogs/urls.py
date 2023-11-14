from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name="index"),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('create_posts/<int:blog_id>/', views.create_posts, name='create_posts')
]
