from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *


#@receiver(post_save, sender=Listing)
#def index_listing(sender, instance, **kwargs):
#    instance.indexing()
