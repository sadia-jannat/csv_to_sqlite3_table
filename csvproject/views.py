from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from csvproject import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .models import *

def Details(request):
    alldetails=Book.objects.all()
    return render(request, 'index.html', {'alldetails':alldetails})
