from django import forms
from .models import MeetingType, Greet, MeetingMinute, Resource, Event

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'

class GreetForm(forms.ModelForm):
    class Meta:
        model=Greet
        fields='__all__'




