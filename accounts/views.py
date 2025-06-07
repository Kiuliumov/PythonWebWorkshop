from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, template_name='accounts/register-page.html')

def login(request):
    return render(request, template_name='accounts/login-page.html')

def details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')

def edit(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')

def delete(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')