from django.shortcuts import render, get_object_or_404
from .models import Post

def render_post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {
        'posts' : posts
    })

def post_detail(request, post_id): # Es el post_id al cual hacemos referencia en urls.py
    post = get_object_or_404(Post, pk=post_id) # Nos sirve para ver si realmente existe en nuestra base de datos
    return render(request, 'post_detail.html', {
        "post": post
    })
