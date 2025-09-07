"""
URL configuration for Games_Forum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Games_Database.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



 
urlpatterns = [
    #admin page for the creator.
    path('admin/', admin.site.urls),
    #Home page
    path('', home, name='home'),
    #This is for our pages of posts based on a specific category.
    path('forum/<str:category_name>/', category_forums, name='category_forums'),
    #Create a post.
    path('addForum/', addForum, name='addForum'),
    #Create a reply.
    path('addReply/', addReply, name='addReply'),
    #Login.
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #Logout.
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    #Register and Create an Account.
    path('register/', register, name='register'),
    #This is for our pages of videos based on a specific category.
    path('video/<str:category_name>/', category_videos, name='category_videos'),
    #Creates a Post with a Video.
    path('addVideo/', addVideo, name='addVideo'),
    #Create a reply to a video.
    path('addVideoReply/', addVideoReply, name='addVideoReply'),

    path('editForum/<int:forum_id>/<str:category_name>/', editForum, name='editForum')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
