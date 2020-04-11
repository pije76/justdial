from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import *
from .forms import *

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'description', 'photofeatured', 'photo1', 'photo2', 'photo2', 'age', 'phone', 'street', 'city']
    prepopulated_fields = {'slug': ('title',), }
    ModelAdmin.ordering = ('id',)
    form = ListingForm

    class Meta:
        model = Listing


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['id', 'title', 'parent', 'slug']
    prepopulated_fields = {'slug': ('title',), }
    ModelAdmin.ordering = ('id',)

    class Meta:
        model = Category


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
