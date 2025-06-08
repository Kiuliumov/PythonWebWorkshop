from django.urls import path, include

from photos import views

urlpatterns = [
    path('add/', views.add, name='photo-add'),
    path('<int:pk>/', views.details, name='photo-details'),
    path('<int:pk>/edit/', views.edit, name='photo-edit'),
]