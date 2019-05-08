from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MeetingType(models.Model):
    meetingtypename=models.CharField(max_length=255)
    meetingdescription=models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.meetingtypename 

    class Meta(): 
        db_table='meetingtype'
        verbose_name_plural='meetingtypes'

    class MeetingMeet(models.Model):
        meetingmeettitle=models.CharField(max_length=255)
        meetingmeetdate =models.DateField()
        meetingmeettime=models.TimeField()
        meetingmeetlocation=models.TextField()
        meetingmeetagenda=models.TextField()

        class Meta:
            db_table='meeting'
            verbose_name_plural='meetings' 
    
    class MeetingMinute(models.Model):
        meetingid=models.ForeignKey
        meetingattendance=models.ManyToManyField(User)
        meetingminutes=models.TextField()

        def __str__(self):
            return self.meetingid
        
        class Meta:
            db_table='meetingminute'


    class Resource(models.Model):
        resourcename=models.CharField(max_length=255) 
        resourcetype=models.TextField()
        resourceurl=models.URLField(null=True, blank=True)
        resourcedate=models.DateField()
        resourceuserid=models.ForeignKey
        resourcedescription=models.TextField()

        def __str__(self):
            return self.resourceuserid
        
        class Meta:
            db_table='resource'
    

    class Event(models.Model):
        eventtitle=models.CharField(max_length=255) 
        eventlocation=models.TextField()
        eventtime=models.TimeField()
        eventdate=models.DateField()
        eventuserid=models.ForeignKey
        eventdescription=models.TextField()

        def __str__(self):
            return self.eventuserid
        
        class Meta:
            db_table='event'



