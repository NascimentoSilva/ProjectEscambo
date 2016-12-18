from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'escambo/home.html', {'posts' : posts})

def detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'escambo/detalhes.html', {'post' : post})

def novo(request):
    form = PostForm()
    return render(request, 'escambo/novo.html', {'form' : form})

def sobre(request):
    return render(request, 'escambo/sobre.html', {})

def editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalhes', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'escambo/novo.html', {'form': form})

def index(request):
    return render(request, 'escambo/index.html', {})
