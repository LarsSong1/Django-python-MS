from django.urls import path
from .views import HomeView, CreateBlogView, BlogDetailView


app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create/', CreateBlogView.as_view(), name="create-blog"),
    path('blog/<int:id>/', BlogDetailView.as_view(), name="detail-blog" )
]
