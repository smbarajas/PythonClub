from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
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
    MeetingID=models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.MeetingID

    class Meta:
        db_table='minutes'
        
class Resource(models.Model):
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
    EventTitle=models.CharField(max_length=255)
    EventLocation=models.CharField(max_length=255)
    EventDate=models.DateField()
    EventTime=models.CharacterField()
    
     def __str__(self):
        return self.EventTitle

    class Meta:
        db_table='events'        