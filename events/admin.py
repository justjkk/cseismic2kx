from models import Event
from django.contrib import admin  
from participantsprofile.models import Participant

class ParticipantInline(admin.TabularInline):
    model = Participant.events.through

class EventAdmin(admin.ModelAdmin):
    inlines = [
                ParticipantInline,
              ]
admin.site.register(Event, EventAdmin)

