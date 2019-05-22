from django.shortcuts import render
from .models import MeetingType, Greet, MeetingMinute, Resource, Event

# Create your views here.

def index(request):
    return render(request, 'clubapp\index.html')

def gettypes(request):
    type_list=Resource.objects.all()
    return render(request, 'clubapp/types.html' ,{'type_list' : type_list})

def getevents(request):
    event_list=Event.objects.all()
    return render(request, 'clubapp/events.html', {'event_list': event_list})

def eventdetails(request, eventdetails):
    events=get_object_or_404(Event.id)

    context={
        'event' : events,
    }
    return render(request, 'clubapp/eventdetails.html', context=context)
    

