# Generated by Django 3.2.4 on 2021-06-18 09:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userApp', '0002_product_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
