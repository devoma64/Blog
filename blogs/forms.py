from django import forms
from . models import Blog, Posts

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text': ''}
        
class PostsForm():
    class Meta:
        model = Posts
        fields = ['text']
        labels = {'text': ''}