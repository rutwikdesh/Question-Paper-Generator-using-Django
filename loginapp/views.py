from django.http import HttpResponse
from django.shortcuts import render
#from .models import Question
import random


def index(request):
    return HttpResponse('Hi')