from django.db import models

class Event(models.Model):
    caption = models.CharField(max_length=30)
    classic_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    rules = models.TextField()

    def __unicode__(self):
        return self.caption + ' ( ' + self.classic_name + ' )'

    def list_coordinators(self):
        return self.coordinators.order_by('-academic_year')
