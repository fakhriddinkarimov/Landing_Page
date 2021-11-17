from django import forms
from .models import Product
from geo.models import Region, District
class ProductForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    city = forms.ModelChoiceField(queryset=District.objects.all())
    class Meta:
        model = Product
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ProductForm, self).__init__(*args, **kwargs)
