from django.shortcuts import render, redirect, get_object_or_404
from PythonWebWorkshop1.utils import *
from common.forms import CommentForm
from common.models import Like


# Create your views here.
def home(request):

    form = CommentForm(request.POST or None)

    all_photos = get_photos()
    profile = get_profile()


    return render(request, template_name='common/home-page.html', context={'all_photos': all_photos, 'user': profile, 'form': form})


def comment(request, pk):
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        photo = get_object_or_404(Photo, id=pk)
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.save()
        print(photo.comments.all())
        return redirect('home')

def like(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    like_qs = Like.objects.filter(to_photo=photo)

    if like_qs.exists():
        like_qs.delete()
    else:
        Like.objects.create(to_photo=photo)

    return redirect('home')