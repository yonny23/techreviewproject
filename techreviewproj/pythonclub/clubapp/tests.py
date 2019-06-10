from django.test import TestCase
from .models import MeetingType, Greet, MeetingMinute, Resource, Event

class EventTypeTest(TestCase):
    def test_string(self):
       type=Event(eventtitle="Lebron James Retirement Party")
       self.assertEqual(str(type), type.eventtitle)

    def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')
    
    def test_string(self):
       type=MeetingType(meetingtypename="Big Meeting")
       self.assertEqual(str(type), type.meetingtypename)

    def test_table(self):
       self.assertEqual(str(MeetingType._meta.db_table), 'meeting type')
    
    def test_string(self):
       type=Greet(greettitle="Greet object (None)")
       self.assertEqual(str(type), type.greettitle)

    def test_table(self):
       self.assertEqual(str(Greet._meta.db_table), 'greet')
    
    def test_string(self):
       type=Resource(resourcename="Python Help")
       self.assertEqual(str(type), type.resourcename)

    def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')
    
    def test_string(self):
       type=MeetingMinute(meetingminutes="20 minutes blabbering about something")
       self.assertEqual(str(type), type.meetingminutes)

    def test_table(self):
       self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')
   
    def test_table(self):
       self.assertEqual(str)
   
    def test_string(self):
       type=Event(eventtitle="The Goat")
       self.assertEqual(str(type), type.eventtitle)
   
    def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')
   


    


