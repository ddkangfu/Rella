# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'main_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('svn_source', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('dist_path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('latest_runing_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000, blank=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'main', ['Task'])

        # Adding model 'Project'
        db.create_table(u'main_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000, blank=True)),
            ('svn_path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('public_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('build_file_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('release_note_file_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'main', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'main_task')

        # Deleting model 'Project'
        db.delete_table(u'main_project')


    models = {
        u'main.project': {
            'Meta': {'object_name': 'Project'},
            'build_file_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public_time': ('django.db.models.fields.DateTimeField', [], {}),
            'release_note_file_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'svn_path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.task': {
            'Meta': {'object_name': 'Task'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'blank': 'True'}),
            'dist_path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latest_runing_time': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'svn_source': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']