from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'width': 900, 'height': 400}),
        }