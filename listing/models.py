from django.db import models
from django.urls import reverse
from django.utils.text import slugify
#from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey
from parler.models import TranslatableModel, TranslatedFields
from smart_selects.db_fields import ChainedForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from cities_light.abstract_models import AbstractCountry, AbstractRegion, AbstractCity
from cities_light.receivers import connect_default_signals
from cities_light.models import *

from .elastic_search_connection import ListingIndex


# Create your models here.
class Country(AbstractCountry):
    def get_absolute_url(self):
        return reverse('country_list', kwargs={'slug': self.slug})


connect_default_signals(Country)


class Region(AbstractRegion):
    def get_absolute_url(self):
        return reverse('region_list', kwargs={'region_slug': self.slug})


connect_default_signals(Region)


class City(AbstractCity):
    def get_absolute_url(self):
        return reverse('city_list', kwargs={'city_slug': self.slug})


connect_default_signals(City)


class Category(MPTTModel):
    title = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.DO_NOTHING)

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
#    location = instance.city.name
#    slug_location = slugify(location)
#    category = instance.category.title
#    slug_category = slugify(category)
    title = instance.category.title
    slug = slugify(title)
    return "photos/%s-%s" % (slug, filename)
#    return '{0}/{1}'.format('photos', filename)
#    return 'user_{0}/{1}'.format(instance.user.id, filename)
#    return '{0}/{1}/{2}/{3}'.format('photos', slug_location, slug_category, filename)



#class Images(models.Model):
#    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to=listing_upload_path, null=True, blank=True)
#    image = FilerImageField(on_delete=models.CASCADE)

#    def __str__(self):
#        return str(self.image)

#    class Meta:
#        verbose_name = 'Images'
#        verbose_name_plural = "Images"



class Listing(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField("Listing Title", max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text='Automatically built from the title.')
    description = models.TextField("Listing Description")
    age = models.IntegerField()
    phone = PhoneNumberField()
    photofeatured = FilerImageField(verbose_name='Featured Image', related_name='photosfeatured', null=True, blank=True, on_delete=models.CASCADE)
    photo1 = FilerImageField(verbose_name='Image 1', related_name='photos1', null=True, blank=True, on_delete=models.CASCADE)
    photo2 = FilerImageField(verbose_name='Image 2', related_name='photos2', null=True, blank=True, on_delete=models.CASCADE)
    photo3 = FilerImageField(verbose_name='Image 3', related_name='photos3', null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    street = models.TextField(blank=True)
#    postal_code = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
#        self.slug = slugify(self.title)
        self.title_slug = slugify(self.title)
#        self.title_slug += slugify(self.location.title)
        super(Listing, self).save(*args, **kwargs)

    def get_image(self):
        return self.photo.url

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'city_slug': self.location.slug})

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

