# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'YoutubeVideo.title'
        db.add_column('home_youtubevideo', 'title', self.gf('django.db.models.fields.CharField')(default='Cseismic 2k10', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'YoutubeVideo.title'
        db.delete_column('home_youtubevideo', 'title')


    models = {
        'home.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2010, 8, 14)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'home.youtubevideo': {
            'Meta': {'object_name': 'YoutubeVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['home']
