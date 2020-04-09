# Generated by Django 3.0.5 on 2020-04-09 06:53

from django.db import migrations, models
import django.db.models.deletion
import listing.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='listing.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Listing Title')),
                ('slug', models.SlugField(blank=True, help_text='Automatically built from the title.', max_length=255, unique=True)),
                ('description', models.TextField(verbose_name='Listing Description')),
                ('age', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Phone Number')),
                ('photo', models.FileField(blank=True, null=True, upload_to=listing.models.listing_upload_path)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.Category')),
            ],
            options={
                'verbose_name': 'Listing',
            },
        ),
    ]
