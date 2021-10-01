from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(Category, CategoryAdmin)
