# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SaltCommand'
        db.create_table(u'main_saltcommand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('key', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
            ('salt_target', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('salt_function', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'main', ['SaltCommand'])

        # Adding model 'SaltArg'
        db.create_table(u'main_saltarg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('command', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.SaltCommand'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'main', ['SaltArg'])


    def backwards(self, orm):
        # Deleting model 'SaltCommand'
        db.delete_table(u'main_saltcommand')

        # Deleting model 'SaltArg'
        db.delete_table(u'main_saltarg')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'salt_function': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'salt_target': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['main']