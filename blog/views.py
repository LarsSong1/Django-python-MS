from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context={
            'posts': posts
        }
        return render(request, 'home.html', context)
    


class CreateBlogView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        print(form)
        context = {
            'form': form
        }
        return render(request, 'createBlog.html', context)
    

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title = title, content = content)
                p.save()
                
                return redirect('blog:home')
        context = {
            'form': form
        }
        context = {

        }
        return render(request, 'createBlog.html', context)
