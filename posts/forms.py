from django import forms  
from django.contrib.auth.models import User 

class PostForm(forms.Form):  
    title = forms.CharField(max_length=200)  
    content = forms.TextField()  
    author = forms.ForeignKey(User, on_delete=forms.CASCADE)  