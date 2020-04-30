from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list-articles'),
    path('articles/<int:id>/email', views.email, name='email'),
    path('email', views.send_email, name='send-email'),
]






