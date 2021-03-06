# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'College'
        db.create_table('participantsprofile_college', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('participantsprofile', ['College'])

        # Adding model 'Participant'
        db.create_table('participantsprofile_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['participantsprofile.UserProfile'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participants', to=orm['participantsprofile.College'])),
            ('roll_no', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('participantsprofile', ['Participant'])

        # Adding model 'UserProfile'
        db.create_table('participantsprofile_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('participantsprofile', ['UserProfile'])

        # Adding model 'Team'
        db.create_table('participantsprofile_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('no_of_persons', self.gf('django.db.models.fields.IntegerField')()),
            ('for_event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams_registered', to=orm['events.Event'])),
        ))
        db.send_create_signal('participantsprofile', ['Team'])

        # Adding M2M table for field participants on 'Team'
        db.create_table('participantsprofile_team_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['participantsprofile.team'], null=False)),
            ('participant', models.ForeignKey(orm['participantsprofile.participant'], null=False))
        ))
        db.create_unique('participantsprofile_team_participants', ['team_id', 'participant_id'])


    def backwards(self, orm):
        
        # Deleting model 'College'
        db.delete_table('participantsprofile_college')

        # Deleting model 'Participant'
        db.delete_table('participantsprofile_participant')

        # Deleting model 'UserProfile'
        db.delete_table('participantsprofile_userprofile')

        # Deleting model 'Team'
        db.delete_table('participantsprofile_team')

        # Removing M2M table for field participants on 'Team'
        db.delete_table('participantsprofile_team_participants')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'participantsprofile.college': {
            'Meta': {'object_name': 'College'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'participantsprofile.participant': {
            'Meta': {'object_name': 'Participant'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participants'", 'to': "orm['participantsprofile.College']"}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'roll_no': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['participantsprofile.UserProfile']", 'unique': 'True'})
        },
        'participantsprofile.team': {
            'Meta': {'object_name': 'Team'},
            'for_event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams_registered'", 'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_of_persons': ('django.db.models.fields.IntegerField', [], {}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['participantsprofile.Participant']", 'symmetrical': 'False'})
        },
        'participantsprofile.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['participantsprofile']
