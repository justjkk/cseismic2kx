from django.db import models
from django.contrib.auth.models import User

from events.models import Event

ACADEMIC_YEAR_CHOICES = (
    (2, 'II yr CSE'),
    (3, 'III yr CSE'),
    (4, 'IV yr CSE'),
)

class Coordinator(models.Model):
    fullname = models.CharField(max_length=50)
    academic_year = models.IntegerField(choices=ACADEMIC_YEAR_CHOICES)
    event = models.ForeignKey(Event, blank=True, null=True, related_name = 'coordinators')
    contact_phone = models.BigIntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return (str)(self.fullname) + ' ( ' + self.event.caption + ' )'
        
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name
        
    def contact_email(self):
        return self.user.email
