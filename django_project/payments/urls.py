# payments/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('/charged/', views.charged, name='charged'),
    path('', views.PayMe.as_view(), name='payme'),
]
