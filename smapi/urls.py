from django.contrib import admin
from django.urls import path
from smapi.views import CreatePostView

urlpatterns = [
    path('createpost/', CreatePostView.as_view(), name='register'),
]