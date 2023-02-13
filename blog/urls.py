from django.urls import path
from .views import LoginView,HomePage,AllBlogs,Blogs


from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path("",LoginView.as_view(),name="login"),
    path("home/",HomePage.as_view(),name="home"),
    path("all-blogs/",AllBlogs.as_view(),name="allBlogs"),
    path("all-blogs/<int:id>",Blogs.as_view(),name="blog"),
    
    
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]