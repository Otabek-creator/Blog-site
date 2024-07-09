from django.urls import path

from .views import *

urlpatterns = [
    path('', get_posts, name='post_all'),
    path('detail/<int:pk>/', get_post, name='post_detail'),
    path('filter/<str:tag_name>/', get_posts_by_tag, name='post_filter'),
    path('about/', about, name='about_me'),

]
