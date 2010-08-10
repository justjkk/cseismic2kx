from django.db import models
from datetime import datetime

class NewsItem(models.Model):  
    message = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now().date())
    link = models.URLField(blank=True)
    tags = models.CharField(max_length=50,blank=True)
    def __unicode__(self):
        if self.link is None or self.link == '':
            return '%s'%self.message
        else:
            return '<a href="'+self.link+'">'+self.message+'</a>'
    class Meta:
      ordering = ['-date']
      
class YoutubeVideo(models.Model):
    video_id = models.CharField(max_length=255)
    
    def __unicode__(self):
        return 'http://www.youtube.com/v/'+self.video_id
