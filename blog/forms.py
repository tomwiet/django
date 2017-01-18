from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'w3-input'}),
            'text' : forms.Textarea(attrs={'cols' : '100%','class' : 'w3-input'}),

        }
