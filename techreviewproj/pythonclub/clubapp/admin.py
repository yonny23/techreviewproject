from django.contrib import admin
from .models import MeetingType, MeetingMeet, MeetingMinute, Resource, Event

# Register your models here.
admin.site.register(MeetingType)
admin.site.register(MeetingMeet)
admin.site.register(MeetingMinute)
admin.site.register(Resource)
admin.site.register(Event)