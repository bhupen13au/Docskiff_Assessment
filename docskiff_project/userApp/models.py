from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    owner = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
