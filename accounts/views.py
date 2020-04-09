from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.dispatch import receiver

from allauth.account.signals import user_signed_up, user_logged_in

from accounts.models import *


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def account(request):
    context = {
        'navbar': 'account',
    }
    return render(request, 'account.html', context)
