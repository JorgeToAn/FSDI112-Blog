from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from posts.models import Post


class PostListView(ListView):
    template_name: str = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name: str="posts/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name: str="posts/new.html"
    model = Post
    fields = ['title', 'author', 'subtitle', 'body']