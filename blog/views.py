from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    Posts = Post.objects.all()
    return render(request,'blog/blog.html',{'Posts': Posts})


def caregory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html',{'category':category})