from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
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


class PostUpdateView(UpdateView):
    template_name: str="posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]


class PostDeleteView(DeleteView):
    template_name: str="posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")