from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

# CHARTJS SHIT

from random import randint

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})