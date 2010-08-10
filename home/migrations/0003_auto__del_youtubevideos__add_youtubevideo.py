# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'YoutubeVideos'
        db.delete_table('home_youtubevideos')

        # Adding model 'YoutubeVideo'
        db.create_table('home_youtubevideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('home', ['YoutubeVideo'])


    def backwards(self, orm):
        
        # Adding model 'YoutubeVideos'
        db.create_table('home_youtubevideos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('home', ['YoutubeVideos'])

        # Deleting model 'YoutubeVideo'
        db.delete_table('home_youtubevideo')


    models = {
        'home.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2010, 8, 10)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'home.youtubevideo': {
            'Meta': {'object_name': 'YoutubeVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['home']
