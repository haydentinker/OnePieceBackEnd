from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Character,Affiliations,Occupations
def index(request):
    return HttpResponse("Hello, world. You're at the one piece index.")

def detail(request, character_id):
    return HttpResponse(Character.objects.filter(id=character_id))