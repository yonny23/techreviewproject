from django.urls import reverse
from django.contrib.auth.models import User 
from .models import MeetingType, Greet, MeetingMinute, Resource, Event
from django.shortcuts import get_object_or_404, render


# Create your views here.

def index(request):
    return render(request, 'clubapp\index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'clubapp/types.html' ,{'type_list' : type_list})

def getevents(request):
    event_list=Event.objects.all()
    return render(request, 'clubapp/events.html', {'event_list': event_list})

def eventdetails(request, id):
    vents=get_object_or_404(Event, pk=id)
    context={
        'event' : vents,
    }
    return render(request, 'clubapp/eventdetails.html', context=context)

    

