from django.shortcuts import render, redirect, get_object_or_404

from common.models import Like
from photos.forms import PhotoForm
from PythonWebWorkshop1.utils import get_profile
from photos.models import Photo


# Create your views here.
def add(request):

    form = PhotoForm(request.POST, request.FILES)
    profile = get_profile()
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = PhotoForm()

    return render(request, template_name='photos/photo-add-page.html', context={'form': form, 'profile': profile})

def details(request, pk):
    return render(request, template_name='photos/photo-details-page.html')

def edit(request, pk):
    form = PhotoForm(request.POST, request.FILES)
    profile = get_profile()
    if form.is_valid():
        photo = form.save()
        return redirect('photo-details', pk=photo.id)
    else:
        form = PhotoForm()
    return render(request, template_name='common/home-page.html', context={'form': form, 'profile': profile})


