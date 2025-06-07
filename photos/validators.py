from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageValidator:
    def __init__(self):
        self.max_size = 5242880

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(f"The maximum file size that can be uploaded is {self.max_size / (1024 * 1024)}MB.")
