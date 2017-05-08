from .models import  Song
from django.shortcuts import render

def index(request):
    all_songs = Song.objects.all();
    return render(request, 'music/index.html',{'all_songs': all_songs})



