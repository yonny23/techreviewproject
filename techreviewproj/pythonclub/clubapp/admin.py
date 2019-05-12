from django.contrib import admin
from .models import MeetingType, Greet, MeetingMinute, Resource, Event

# Register your models here.
admin.site.register(MeetingType)
admin.site.register(Greet)
admin.site.register(MeetingMinute)
admin.site.register(Resource)
admin.site.register(Event)