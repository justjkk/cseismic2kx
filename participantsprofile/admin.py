from django.contrib import admin
from participantsprofile.models import UserProfile, Participant, College, Team

class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email_id',
        'college',
    )
    ordering = ('college',)

admin.site.register(UserProfile)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(College)
admin.site.register(Team)
