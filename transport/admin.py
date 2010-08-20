from django.contrib.gis import admin
from models import Stop, StopTimings, CollegeBus

class StopTimingsInline(admin.TabularInline):
   model = StopTimings

class StopAdmin(admin.OSMGeoAdmin):
   list_display = ('name',
                  )
   inlines = (StopTimingsInline,)

class CollegeBusAdmin(admin.OSMGeoAdmin):
   inlines = (StopTimingsInline,)

admin.site.register(Stop, StopAdmin)
admin.site.register(CollegeBus, CollegeBusAdmin)
