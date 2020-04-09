from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from mptt.models import MPTTModel, TreeForeignKey
from parler.models import TranslatableModel, TranslatedFields
from smart_selects.db_fields import ChainedForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField

from cities_light.abstract_models import AbstractCountry, AbstractRegion, AbstractCity
from cities_light.receivers import connect_default_signals
from cities_light.models import *

from .elastic_search_connection import ListingIndex


# Create your models here.
class Country(AbstractCountry):
    def get_absolute_url(self):
        return reverse('country_list', kwargs={'country_slug': self.slug})


connect_default_signals(Country)


class Region(AbstractRegion):
    def get_absolute_url(self):
        return reverse('region_list', kwargs={'country_slug': self.country.slug, 'region_slug': self.slug})


connect_default_signals(Region)


class City(AbstractCity):
    def get_absolute_url(self):
        return reverse('city_list', kwargs={'country_slug': self.country.slug, 'region_slug': self.region.slug, 'city_slug': self.slug})


connect_default_signals(City)


class Category(MPTTModel):
    title = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return u'%s: %s' % (self.parent.title, self.title)
        return u'%s' % (self.title)

#    def get_absolute_url(self):
#        return ('listing.views.category_list', (), {'slug': self.slug})

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'category_slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('slug', 'parent',)


def listing_upload_path(instance, filename):
    return '{0}/{1}'.format('photos', filename)


class Listing(models.Model):
    title = models.CharField("Listing Title", max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text='Automatically built from the title.')
    description = models.TextField("Listing Description")
    age = models.IntegerField()
    phone = PhoneNumberField()
    photo = models.ImageField(upload_to=listing_upload_path, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(City, related_name='locations', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, **kwargs)

#    def indexing(self):
#        obj = ListingIndex(
#            meta={
#                'id': self.id
#            },
#            title=self.title,
#            category=self.category,
#            location=self.location
#        )
#        obj.save()
#        return obj.to_dict(include_meta=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Listing'
