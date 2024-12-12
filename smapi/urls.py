from django.contrib import admin
from django.urls import path
from smapi.views import (CreatePostView, CommentView, ProfileView, CreatePostDetails, 
                         currentUserPost, LikePostView, CommentViewDetails)

urlpatterns = [
    # get/create the post
    path('post/', CreatePostView.as_view()),
    # update/delete the post
    path('post/<int:pk>/',CreatePostDetails.as_view()),
    # add comment to a specified post
    path('comment/<int:pk>/',CommentView.as_view()),
    # get profile view
    path('profile/',ProfileView.as_view()), 
    # get logged in user post  
    path('userPost/',currentUserPost.as_view()),
    # like the specified post
    path('post/<int:post_id>/like/', LikePostView.as_view()),
    # delete the comment on a specified post
    path('post/<int:post_pk>/comment/<int:comment_pk>/',CommentViewDetails.as_view())
]