# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SaltCommand.hipchat_notification_msg'
        db.add_column(u'main_saltcommand', 'hipchat_notification_msg',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SaltCommand.hipchat_notification_msg'
        db.delete_column(u'main_saltcommand', 'hipchat_notification_msg')


    models = {
        u'main.saltarg': {
            'Meta': {'ordering': "['order']", 'object_name': 'SaltArg'},
            'command': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.SaltCommand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'main.saltcommand': {
            'Meta': {'object_name': 'SaltCommand'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hipchat_notification_msg': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'salt_function': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'salt_target': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['main']