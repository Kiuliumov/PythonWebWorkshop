from django.urls import path, include

from pets import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('<str:username>/pet/<slug:pet_slug>/', include(
    [
        path('', views.details, name='details-pet'),
        path('edit/', views.edit, name='edit-pet'),
        path('delete/', views.delete, name='delete-pet')
    ]
    ))]

