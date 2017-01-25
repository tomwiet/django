from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'w3-input'}),
            'text' : forms.Textarea(attrs={'cols' : '100%','class' : 'w3-input'}),

        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author' : forms.TextInput(attrs={'class': 'w3-input'}),
            'text' : forms.Textarea(attrs={'cols' : '100%','class' : 'w3-input'}),

        }
