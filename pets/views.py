from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request, template_name='pets/pet-add-page.html')

def details(request, username):
    return render(request, template_name='pets/pet-details-page.html')

def edit(request, username):
    return render(request, template_name='pets/pet-edit-page.html')
def delete(request, username):
    return render(request, template_name='pets/pet-delete-page.html')
