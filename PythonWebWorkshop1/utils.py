from accounts.models import User
from photos.models import Photo


def get_profile():
    return User.objects.first()

def get_photos():
    return Photo.objects.all()