from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('tag/<str:tag>/', views.TagPostListView.as_view(), name='tag_posts'),
    path('my_posts/', views.UserPostListView.as_view(), name='user_posts'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment'),
]