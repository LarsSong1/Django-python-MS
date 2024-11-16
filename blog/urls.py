from django.urls import path
from .views import HomeView, CreateBlogView


app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create/', CreateBlogView.as_view(), name="create-blog"),
]
