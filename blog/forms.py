from django import forms
from .models import Blog


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description', 'image']

class BlogForm(forms.Form):
    class Meta:
        model = Blog
        fields = '__all__'


