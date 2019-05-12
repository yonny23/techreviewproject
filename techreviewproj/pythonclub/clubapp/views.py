from django.shortcuts import render
from .models import MeetingType, Greet, MeetingMinute, Resource, Event

# Create your views here.

def index(request):
    return render(request, 'clubapp\index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'clubapp/types.html' ,{'type_list' : type_list})