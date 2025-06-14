from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import ImageValidator


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', validators=[ImageValidator()])
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)], blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

