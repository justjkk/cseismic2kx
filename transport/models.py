from django.contrib.gis.db import models

class Stop(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    objects = models.GeoManager()
    
    class Meta:
        ordering = ['name',]
    def __unicode__(self):
        return self.name
        
    def get_timings(self):
        msg = ""
        for timings in self.stop_timings.all():
            msg += "'" + str(timings.college_bus.name) + "' arrives at " + timings.time.strftime("%I:%M %p") + "<br>"
        return msg

class CollegeBus(models.Model):
    name = models.CharField(max_length=20)
    route_name = models.CharField(max_length=50)
    stops = models.ManyToManyField(Stop, through='StopTimings')

    def __unicode__(self):
        return self.route_name + ' | ' + self.name

class StopTimings(models.Model):
    sequence = models.IntegerField()
    stop = models.ForeignKey(Stop, related_name='stop_timings')
    college_bus = models.ForeignKey(CollegeBus, related_name='stop_timings')
    time = models.TimeField()
    
    def __unicode__(self):
        return str(self.college_bus) + ' | ' + str(self.stop)
