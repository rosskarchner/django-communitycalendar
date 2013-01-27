# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'IcalSource.next_fetch'
        db.alter_column(u'compoundcalendar_icalsource', 'next_fetch', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'IcalSource.last_fetch'
        db.alter_column(u'compoundcalendar_icalsource', 'last_fetch', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'IcalSource.next_fetch'
        raise RuntimeError("Cannot reverse this migration. 'IcalSource.next_fetch' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'IcalSource.last_fetch'
        raise RuntimeError("Cannot reverse this migration. 'IcalSource.last_fetch' and its values cannot be restored.")

    models = {
        u'compoundcalendar.icalsource': {
            'Meta': {'object_name': 'IcalSource'},
            'ical_href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_fetch': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next_fetch': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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