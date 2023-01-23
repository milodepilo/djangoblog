from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"