from django.contrib import admin
from participantsprofile.models import UserProfile, Participant, College, Team

class ParticipantInline(admin.TabularInline):
    model = Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email_id',
        'college',
    )
    ordering = ('college',)

class CollegeAdmin(admin.ModelAdmin):
    inlines = [
                ParticipantInline,
              ]
admin.site.register(UserProfile)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Team)