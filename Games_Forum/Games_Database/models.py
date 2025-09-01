from django.db import models
from django.contrib.auth.models import User
category_choicess = [
  ('ps5','PS5'),
  ('xbox series x','Xbox Series X'),
  ('nintendo switch','Nintendo Switch'),
  ('pc','PC'),
  ('retro','Retro'),
  ('ps4', 'PS5'),
  ('xbox one', 'Xbox One'),
  ('nintendo switch 2','Nintendo Switch 2')
  
]
# Create your models here.

#This is the forum model, which is for a post. In this case, it will have what user created it, the topic/title of the post, the description, and the category of course.
class forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    
    category = models.CharField(max_length=25, default='ps4')
#This is the reply model which is a comment on a Forum Post, in which the user will respond to what the post said.
class reply(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)
#This is the video model which is for a video post, in which a user will upload a video with a title, and it naturally gets the time and category.
class video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='forum_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=25, default='ps4')
#This is the reply model which is a comment on a Forum Post, in which the user will respond to the video.
class videoreply(models.Model):
    video = models.ForeignKey(video,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    discuss = models.CharField(max_length=1000)
    

  