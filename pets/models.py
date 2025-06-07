from django.db import models
from django.utils.text import slugify


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    personal_pet_photo = models.URLField(max_length=200, null=False, blank=False)
    date_of_birth = models.DateField()
    slug = models.SlugField(unique=True, null=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
            return super().save(*args, **kwargs)

        super().save(*args, **kwargs)

