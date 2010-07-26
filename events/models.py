from django.db import models

class Event(models.Model):
    caption = models.CharField(max_length=30)
    classic_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    rules = models.TextField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['start_time', 'end_time']
    
    def __unicode__(self):
        return self.caption + ' ( ' + self.classic_name + ' )'

    def list_coordinators(self):
        return self.coordinators.order_by('-academic_year')
