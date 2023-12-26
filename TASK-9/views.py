# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import BlogForm, CommentForm

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'blog': blog, 'comments': comments, 'comment_form': comment_form})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form': form})
