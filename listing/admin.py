from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.options import ModelAdmin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import *

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'description', 'age', 'phone', 'location']
    prepopulated_fields = {'slug': ('title',), }
    ModelAdmin.ordering = ('id',)

    class Meta:
        model = Listing


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['id', 'title', 'parent', 'slug', 'city', 'region', 'country']
    prepopulated_fields = {'slug': ('title',), }
    ModelAdmin.ordering = ('id',)

    class Meta:
        model = Category


admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
