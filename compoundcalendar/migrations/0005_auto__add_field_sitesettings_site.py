# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SiteSettings.site'
        db.add_column(u'compoundcalendar_sitesettings', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['sites.Site']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SiteSettings.site'
        db.delete_column(u'compoundcalendar_sitesettings', 'site_id')


    models = {
        u'compoundcalendar.calendar': {
            'Meta': {'unique_together': "(('site', 'slug'),)", 'object_name': 'Calendar'},
            'default_timezone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'staff_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'compoundcalendar.icalsource': {
            'Meta': {'object_name': 'IcalSource'},
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compoundcalendar.Calendar']", 'null': 'True'}),
            'ical_href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_fetch': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'next_fetch': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'source_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'compoundcalendar.sitesettings': {
            'Meta': {'object_name': 'SiteSettings'},
            'default_timezone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['compoundcalendar']