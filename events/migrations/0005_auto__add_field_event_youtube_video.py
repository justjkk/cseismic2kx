# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Event.youtube_video'
        db.add_column('events_event', 'youtube_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.YoutubeVideo'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Event.youtube_video'
        db.delete_column('events_event', 'youtube_video_id')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'additional_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'classic_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'rules': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'youtube_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.YoutubeVideo']", 'null': 'True', 'blank': 'True'})
        },
        'home.youtubevideo': {
            'Meta': {'object_name': 'YoutubeVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['events']
