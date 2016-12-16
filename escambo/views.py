from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'escambo/home.html', {'posts' : posts})

def detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'escambo/detalhes.html', {'post' : post})

def novo(request):

    return render(request, 'escambo/novo.html', {})

def sobre(request):
    return render(request, 'escambo/sobre.html', {})
