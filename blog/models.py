from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models
from ad.models import Category

class Blog(models.Model):
    name = models.CharField(max_length=255)
    description =tinymce_models.HTMLField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='static/img/blog/')
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete =models.CASCADE
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Blog, self).save(*args, **kwargs)


    # def __str__(self):
    #     return self.name

class Comments(models.Model):
    name = models.CharField(max_length=255)
    message = tinymce_models.HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)



