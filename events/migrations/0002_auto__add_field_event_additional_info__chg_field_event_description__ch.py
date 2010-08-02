# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Event.additional_info'
        db.add_column('events_event', 'additional_info', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Changing field 'Event.description'
        db.alter_column('events_event', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True))

        # Changing field 'Event.venue'
        db.alter_column('events_event', 'venue', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True))


    def backwards(self, orm):
        
        # Deleting field 'Event.additional_info'
        db.delete_column('events_event', 'additional_info')

        # Changing field 'Event.description'
        db.alter_column('events_event', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Event.venue'
        db.alter_column('events_event', 'venue', self.gf('django.db.models.fields.CharField')(max_length=50))


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'additional_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'classic_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rules': ('django.db.models.fields.TextField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']
