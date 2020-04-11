# Generated by Django 3.0.5 on 2020-04-11 05:40

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('listing', '0007_listing_photofeatured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo1',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos1', to=settings.FILER_IMAGE_MODEL, verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo2',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos2', to=settings.FILER_IMAGE_MODEL, verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo3',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos3', to=settings.FILER_IMAGE_MODEL, verbose_name='Image 3'),
        ),
    ]
