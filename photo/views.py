from .models import Photo
from django.shortcuts import render

def index(request):
    all_photo = Photo.objects.all();
    return render(request, 'photo/index.html',{'all_photo': all_photo})



# Create your views here.
