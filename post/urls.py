from django.urls import path
from .views import CollectContentsApiView, SocialMediaPostsApiView

urlpatterns = [
    path("load-data", CollectContentsApiView.as_view()),
    path("", SocialMediaPostsApiView.as_view()),
]
