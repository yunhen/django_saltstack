# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SaltCommand.is_github_hook'
        db.add_column(u'main_saltcommand', 'is_github_hook',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SaltCommand.github_secret'
        db.add_column(u'main_saltcommand', 'github_secret',
                      self.gf('uuidfield.fields.UUIDField')(default='19e608db-04f5-450c-bacf-0286c0dda821', unique=True, max_length=32, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SaltCommand.is_github_hook'
        db.delete_column(u'main_saltcommand', 'is_github_hook')

        # Deleting field 'SaltCommand.github_secret'
        db.delete_column(u'main_saltcommand', 'github_secret')


    models = {
        u'main.saltarg': {
            'Meta': {'ordering': "['order']", 'object_name': 'SaltArg'},
            'command': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.SaltCommand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'main.saltcommand': {
            'Meta': {'ordering': "['order']", 'object_name': 'SaltCommand'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'github_secret': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'hipchat_notification_msg': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_github_hook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'salt_function': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'salt_target': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['main']
