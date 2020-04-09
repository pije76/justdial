from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.account, name='account'),
]
