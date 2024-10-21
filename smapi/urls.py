from django.contrib import admin
from django.urls import path
from smapi.views import CreatePostView, CommentView

urlpatterns = [
    path('createpost/', CreatePostView.as_view(), name='register'),
    path('comment/<int:pk>/',CommentView.as_view(), name="commentview")
]