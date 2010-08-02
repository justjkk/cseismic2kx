# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Coordinator.fullname'
        db.add_column('host_coordinator', 'fullname', self.gf('django.db.models.fields.CharField')(default='Noname', max_length=50), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Coordinator.fullname'
        db.delete_column('host_coordinator', 'fullname')


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
        },
        'host.coordinator': {
            'Meta': {'object_name': 'Coordinator'},
            'academic_year': ('django.db.models.fields.IntegerField', [], {}),
            'contact_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'coordinators'", 'null': 'True', 'to': "orm['events.Event']"}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['host']
