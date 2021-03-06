from django.db import models

# Create your models here.

class TennisEvent(models.Model):
    match_time=models.DateTimeField(editable=True)
    event_status=models.CharField(max_length=100,default="Scheduled")
    event_type=models.CharField(max_length=100)
    event_name=models.CharField(max_length=100)
    match_id=models.CharField(max_length=100,unique=True)
    participant1=models.CharField(max_length=100)
    participant2=models.CharField(max_length=100)
    event_score=models.CharField(max_length=100,blank=True)

