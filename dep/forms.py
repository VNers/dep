from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']

    author = forms.CharField(max_length=100, label='Your Name')
    content = forms.CharField(widget=forms.Textarea, label='Your Comment')