from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


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
