from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Character,Affiliations,Occupations
def index(request):
    return HttpResponse("Hello, world. You're at the one piece index.")

def detail(request, character_id):
    return HttpResponse(Character.objects.filter(id=character_id))

def characterView(request):
    character1=Character.objects.filter(id=1)
    url="https://static.wikia.nocookie.net/onepiece/images/b/b8/Koby_Anime_Post_Timeskip_Infobox.png/revision/latest?cb=20230227233927"
    return render(request,'myapp.html',{"character":character1,"source":url})