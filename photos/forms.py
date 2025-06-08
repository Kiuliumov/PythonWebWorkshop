from django import forms

from common.models import Like
from photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'tagged_pets': forms.SelectMultiple(attrs={'id': 'id_tagged_pets'}),
        }
        labels = {
            'photo': 'Photo file',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag Pets',
        }
