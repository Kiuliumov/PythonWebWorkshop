from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('<int:pk>', include(
        [
            path('', views.details, name='details'),
            path('edit/', views.edit, name='edit'),
            path('delete/', views.delete, name='delete'),

        ]
    ))
]