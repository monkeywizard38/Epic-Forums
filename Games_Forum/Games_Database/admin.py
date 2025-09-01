from django.contrib import admin
from .models import forum, reply, video, videoreply
 
# Register your models here.
admin.site.register(forum)
admin.site.register(reply)
admin.site.register(video)
admin.site.register(videoreply)