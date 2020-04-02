from django.shortcuts import render,get_object_or_404
from .models import blog
# Create your views here.
def blogs_list(request):
    blogs=blog.objects.all()
    context={
    'blogs':blogs
    }
    return render(request,'blogs/blogs.html',context)
def blog_details_view(request,id):
    blogs=get_object_or_404(blog,pk=id)
    context={
    'blog':blogs
    }
    return render(request,'blogs/blog_details.html',context)
