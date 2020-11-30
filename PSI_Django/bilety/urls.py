# \myclub_root\events\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
]