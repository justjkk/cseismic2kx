from django.db import models
from datetime import datetime

class NewsItem(models.Model):  
    message = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now().date())
    link = models.URLField(blank=True)
    tags = models.CharField(max_length=50,blank=True)
    def __unicode__(self):  
        return '%s'%self.message
    class Meta:
      ordering = ['-date']
