from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
class User(models.Model):

    class Gender(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
        DO_NOT_SHOW = 'Do not show'
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2), MaxLengthValidator(50)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2), MaxLengthValidator(50)])
    profile_picture = models.URLField()
    gender = models.CharField(max_length=50, choices=Gender.choices)




