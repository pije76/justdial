# Generated by Django 3.0.5 on 2020-04-10 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='location',
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='listing.City'),
            preserve_default=False,
        ),
    ]
