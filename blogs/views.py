from django.shortcuts import render, redirect
from .models import Blog
from . forms import BlogForm, PostsForm

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

def blogs(request):
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    posts = blog.posts_set.order_by('date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def create_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else: 
        form = BlogForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    
    return render(request, 'blogs/create_blog.html', {'form': form})

def create_posts(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    
    if request.method != 'POST':
        form = PostsForm()
    else:
        form = PostsForm(data=request.POST)
        if form.is_valid():
            create_post = form.save(commit=False)
            create_post.blog = blog
            create_post.save()
            return redirect('blogs:blog', blog_id = blog_id)
    return render(request, 'blogs/create_posts.html', {'blog': blog, 'form': form, 'create_post': create_post})