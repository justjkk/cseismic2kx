from django.db import models
from django.contrib.auth.models import User
from events.models import Event
User_Types = (
   ('P','Participant'),
   ('A','Admin')
)

class College(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Participant(models.Model):
    user = models.ForeignKey('participantsprofile.UserProfile', unique=True)
    
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    phone_no = models.CharField(max_length=12)

    college = models.ForeignKey(College, related_name='participants')
    roll_no = models.CharField(max_length=15)
    events = models.ManyToManyField(Event, null=True, blank=True)
    class Meta:
        ordering = ('college',)
    def __unicode__(self):
        return 'Participant - ' + str(self.name)

class UserProfile(models.Model):
   user = models.ForeignKey(User, unique=True)
   user_type = models.CharField(max_length=1, choices=User_Types)
   def __unicode__(self):
      if self.user_type == 'P':
         participant = Participant.objects.filter(user=self)
         if participant:
            return (participant[0].name)
      return (str)(self.user)

class Team(models.Model):
    no_of_persons = models.IntegerField()
    for_event = models.ForeignKey(Event, related_name='teams_registered')
    participants = models.ManyToManyField(Participant)
