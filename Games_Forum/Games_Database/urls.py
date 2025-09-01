from django.contrib import admin
from django.urls import path
from Games_Database.views import *
from django.contrib.auth import views as auth_views
 
urlpatterns = [
     # we use this for the login page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    #allows us to log out
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #since we have many categories, this allows us to use the same templates and forms but with different categories
    #this page's purpose is to scroll through posts and videos
    path('forum/<str:category_name>/', category_forums, name='category_forums'),
    #creates a post
    path('addForum/', addForum, name='addForum'),
    #this adds a reply to a post
    path('addReply/', addReply, name='addReply'),
    #registers an account
    path('register/', register, name='register'),
    #similar to the forum, this is the same purpose but for videos
    path('video/<str:category_name>/', category_videos, name='category_videos')

]