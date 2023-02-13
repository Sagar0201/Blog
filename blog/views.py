from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Blog,Category
from django.contrib.auth.models import User

# Create your views here.

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("this is login page")
    
    
class HomePage(View):
    def get(self, request):
        blogs = Blog.objects.all().order_by('created_at')[:5]
        
        return render(request, "blogs/home.html",{"Blogs":blogs})
    
class AllBlogs(View):
    
    def get(self, request):
        cat= request.GET.get('category')
        category= Category.objects.all()
        if cat != '0' and cat is not None:
            blogs = Blog.objects.filter(category=cat)
        else:
            blogs = Blog.objects.all()
            
        context= {
            "Blogs":blogs,
            "Category":category,
            "Category_name":"All"
        }
        if cat != '0' and cat is not None:
            context["Category_name"]= Category.objects.filter(id=cat)[0]
        
        return render(request, "blogs/allBlogs.html",context)
    
    
class Blogs(View):
    def get(self, request,id):
        blog = Blog.objects.get(id=id)
        
        return render(request, "blogs/blog.html",{"Blog":blog})
        