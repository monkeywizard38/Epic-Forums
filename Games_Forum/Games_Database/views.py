from django.shortcuts import render, redirect
from .models import * 
from .forms import * 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'home.html')
#There are different sections for each Video Game Console, so we want these categories, that each correspond to a html page.
def category_forums(request, category_name):
    #This filters out the videos, by backwards order.
    forums = forum.objects.filter(category=category_name).order_by('-id') 
    #map of each category to each html.
    template_map = {
        'ps4': 'ps4.html',
        'ps5': 'ps5.html',
        'xbox one': 'xbox_one.html',
        'xbox series x': 'xbox_series_x.html',
        'nintendo switch': 'nintendo_switch.html',
        'nintendo switch 2': 'nintendo_switch_2.html',
        'pc': 'pc.html',
        'retro': 'retro.html',
    }

    # Get the appropriate template or a fallback
    template_name = template_map.get(category_name.lower(), 'default_category.html')

    return render(request, template_name, {
        'forums': forums,
        'category': category_name
    })
#to add a post or a reply, we will need to be logged into an account.
#This is the View for creating a forum, where we get the category by default(what page you were on) and then can post a Forum Post.
@login_required
def addForum(request):
    form = CreateForum()
    category = request.POST.get("category") or request.GET.get("category")

    if request.method == 'POST':
        form = CreateForum(request.POST)
        if form.is_valid():
            
            forum_instance = form.save(commit=False) 
            forum_instance.user = request.user
            forum_instance.category = category
            forum_instance.save()
            
            
            return redirect('/')
    context = {'form': form, 'category': category}  # pass category to template if needed
    return render(request, 'addForum.html', context)
 
#This view allows a user to reply to a post, in which hidden input gets the forum_id
@login_required
def addReply(request):
    if request.method == 'POST':
        form = CreateReply(request.POST)
        forum_id = request.POST.get('forum_id')  

        if form.is_valid() and forum_id:
            discussion = form.save(commit=False)
            discussion.user = request.user
            discussion.forum_id = forum_id  # link the reply to the correct forum post
            discussion.save()
            return redirect('/')  # or redirect to forum detail page
    else:
        form = CreateReply()

    context = {
        'form': form,
        'forum_id': request.GET.get('forum_id'),  # pass forum_id so the form can keep it
    }
    return render(request, 'addReply.html', context)

#This is for creating an account, in which we use the default django user creation form.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #After creating an account, we want users to log into their accounts.  
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

#This is for uploading and creating a video post, just like the the addForum view.
#Also need to be logged in to upload a video.
@login_required
def addVideo(request):
    form = CreateVideo()
    category = request.POST.get("category") or request.GET.get("category")

    if request.method == 'POST':
        form = CreateVideo(request.POST, request.FILES)
        if form.is_valid():
            video_instance = form.save(commit=False)
            video_instance.user = request.user
            video_instance.category = category
            video_instance.save()
            return redirect('/')
    
    context = {'form': form, 'category': category}
    return render(request, 'addVideo.html', context)

#This is similar to the categories for posts above but for the video posts part of the website.
def category_videos(request, category_name):
    #This filters out the videos, by backwards order.
    videos = video.objects.filter(category=category_name).order_by('-id')
    #these are each category of videos, and the htmls that map to each category.
    template_map = {
        
        'retrovideos': 'retrovideos.html',
        'pcvideos': 'pcvideos.html',
        'ps4videos': 'ps4videos.html',
        'ps5videos': 'ps5videos.html',
        'nsvideos': 'nsvideos.html',
        'ns2videos': 'ns2videos.html',
        'xonevideos': 'xonevideos.html',
        'xseriesvideos': 'xseriesvideos.html',
    }

    # Get the appropriate template or a fallback
    template_name = template_map.get(category_name.lower(), 'default_category.html')

    return render(request, template_name, {
        'videos': videos,
        'category': category_name
    })


#Requires a login.
#This is the view to add a reply to a video post.
@login_required
def addVideoReply(request):
    if request.method == 'POST':
        form = CreateVideoReply(request.POST)
        video_id = request.POST.get('video_id')

        if form.is_valid() and video_id:
            discussion = form.save(commit=False)
            discussion.user = request.user
            discussion.video_id = video_id
            discussion.save()
            return redirect('/')
    else:
        form = CreateReply()

    context = {
        'form': form,
        'video_id': request.GET.get('video_id'),  # pass forum_id so the form can keep it
    }
    return render(request, 'addVideoReply.html', context)
