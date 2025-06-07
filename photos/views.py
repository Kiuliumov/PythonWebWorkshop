from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request, template_name='photos/photo-add-page.html')

def details(request, pk):
    return render(request, template_name='photos/photo-details-page.html')

def edit(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')

