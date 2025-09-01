from django.forms import ModelForm
from django import forms
from .models import *
 
#This Form creates a Post on the Website.
#We don't want the user or the category on the form because that's given.
class CreateForum(ModelForm):
    class Meta:
        model= forum
        exclude = ['category']  # so it's not required in the form
        exclude = ['user']
        fields = "__all__"
        widgets = {'description': forms.Textarea(attrs={'rows': 6, 'cols':50}), 'topic':forms.Textarea(attrs={'rows':2,'cols':50})}
 
#This Form creates a Reply to a Post on the Website.
#We don't want the user to be on the form because that's given.
class CreateReply(ModelForm):
    class Meta:
        model= reply
        exclude = ['user']
        fields = "__all__"
        widgets = { 'discuss':forms.Textarea(attrs={'rows':2,'cols':50})}

#This Form creates a Video to post on the Website.
#We don't want the user or the category on the form because that's given.
class CreateVideo(ModelForm):
    class Meta:
        model = video
        exclude = ['category', 'user']  # so it's not required in the form
        widgets = { 'title':forms.Textarea(attrs={'rows':2,'cols':50})}

#This Form creates a Reply to a Video Post on the Website.
#We don't want the user to be on the form because that's given.
class CreateVideoReply(ModelForm):
    class Meta:
        model= videoreply
        exclude = ['user']
        fields = "__all__"
        widgets = { 'discuss':forms.Textarea(attrs={'rows':2,'cols':50})}