from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50,  null=False, blank=False)
    parent = models.ForeignKey('self', related_name='father', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.parent and self.parent.name == self.name:
            raise ValidationError('Xato....')
        else:
            if not self.slug:
                self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def str(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='media/product/image/')


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    decription = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductImage(models.Model):
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)