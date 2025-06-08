from django.urls import path

from common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comment/<int:pk>', views.comment, name='comment'),
    path('like/<int:pk>', views.like, name='like'),
]