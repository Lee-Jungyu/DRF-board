from django.urls import path
from post.views import PostAPI, PostDetailAPI

urlpatterns = [
    path("", PostAPI.as_view()),
    path("<int:pk>", PostDetailAPI.as_view()),
]
