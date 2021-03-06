from django.db import models

from home.models import YoutubeVideo

class Event(models.Model):
    caption = models.CharField(max_length=30)
    classic_name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    rules = models.TextField()
    additional_info = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    venue = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    youtube_video = models.ForeignKey(YoutubeVideo, null=True, blank=True)
    class Meta:
        ordering = ['start_time', 'end_time']
    
    def __unicode__(self):
        return self.caption + ' ( ' + self.classic_name + ' )'

    def list_coordinators(self):
        return self.coordinators.filter(academic_year=4)
