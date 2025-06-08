from django.shortcuts import render, redirect
from PythonWebWorkshop1.utils import get_profile
from accounts.forms import RegisterForm
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    first_user = get_profile()

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, template_name='accounts/register-page.html', context={'form': form, 'profile':first_user})

def login(request):
    return render(request, template_name='accounts/login-page.html')

def details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')

def edit(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')

def delete(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')