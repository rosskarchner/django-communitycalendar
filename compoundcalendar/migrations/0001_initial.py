# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IcalSource'
        db.create_table(u'compoundcalendar_icalsource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('ical_href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('last_fetch', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('next_fetch', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'compoundcalendar', ['IcalSource'])


    def backwards(self, orm):
        # Deleting model 'IcalSource'
        db.delete_table(u'compoundcalendar_icalsource')


    models = {
        u'compoundcalendar.icalsource': {
            'Meta': {'object_name': 'IcalSource'},
            'ical_href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_fetch': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next_fetch': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'source_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['compoundcalendar']