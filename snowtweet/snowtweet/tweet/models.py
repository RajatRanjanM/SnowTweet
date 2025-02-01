from django import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text']

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'