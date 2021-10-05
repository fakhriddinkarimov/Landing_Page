from django import forms
from .models import Blog, Comments


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description', 'image']

class BlogForm(forms.Form):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'