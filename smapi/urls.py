from django.contrib import admin
from django.urls import path
from smapi.views import CreatePostView, CommentView, ProfileView, CreatePostDetails, currentUserPost, LikePostView

urlpatterns = [
    path('createpost/', CreatePostView.as_view(), name='register'),
    path('createpost/<int:pk>/',CreatePostDetails.as_view(), name="createPostDetails"),
    path('comment/<int:pk>/',CommentView.as_view(), name="commentview"),
    path('profile/',ProfileView.as_view(), name="profileview"),   
    path('currpost/',currentUserPost.as_view(), name="curr"),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post')
]