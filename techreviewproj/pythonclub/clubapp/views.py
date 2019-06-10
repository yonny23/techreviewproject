from django.urls import reverse
from django.contrib.auth.models import User 
from .models import MeetingType, Greet, MeetingMinute, Resource, Event
from django.shortcuts import get_object_or_404, render
from .forms import ResourceForm, GreetForm
from django.contrib.auth.decorators import login_required

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

def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'clubapp/newresource.html', {'form': form})


def newGreet(request):
    form=GreetForm
    if request.method=='POST':
        form=GreetForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=GreetForm()
    else:
        form=GreetForm()
    return render(request, 'clubapp/newgreet.html', {'form': form})
def loginmessage(request):
    return render(request, 'clubapp/login.html')

def logoutmessage(request):
    return render(request, 'clubapp/logout.html')

@login_required
def newGreets(request):
     form=GreetForm
     if request.method=='POST':
          form=GreetForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=GreetForm()
     else:
          form=GreetForm()
     return render(request, 'clubapp/newgreet.html', {'form': form})




    

