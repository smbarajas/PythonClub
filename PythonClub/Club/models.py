from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
 # fields for title, date, time,location, agenda    
    MeetingTitle=models.CharField(max_length=255)
    MeetingDate=models.DateField()
    MeetingTime=models.CharField(max_length=255)
    MeetingLocation=models.CharField(max_length=255)
    MeetingAgenda=models.CharField(max_length=255)
    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
# fields for meeting id, attendance, minutes
    MeetingID=models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.MeetingID

    class Meta:
        db_table='minutes'
        
class Resource(models.Model):
# fields for resource name, type, URL, date entered, user ID, description    
    ResourceName=models.CharField(max_length=255)
    ResourceType=models.ForeignKey(ResourceType, on_delete=models.DO_NOTHING)
    Resourceurl=models.URLField(null=True, blank=True)
    ResourceDate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ResourceDescription=models.TextField()

     def __str__(self):
        return self.ResourceName

    class Meta:
        db_table='resource'

class Event(models.Model):
# fields for event title, location, date, time, description, user   
    EventTitle=models.CharField(max_length=255)
    EventLocation=models.CharField(max_length=255)
    EventDate=models.DateField()
    EventTime=models.CharacterField()
    
     def __str__(self):
        return self.EventTitle

    class Meta:
        db_table='events'        
