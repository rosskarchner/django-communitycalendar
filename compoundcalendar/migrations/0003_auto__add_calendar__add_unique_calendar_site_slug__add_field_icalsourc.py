# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calendar'
        db.create_table(u'compoundcalendar_calendar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('staff_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'compoundcalendar', ['Calendar'])

        # Adding unique constraint on 'Calendar', fields ['site', 'slug']
        db.create_unique(u'compoundcalendar_calendar', ['site_id', 'slug'])

        # Adding field 'IcalSource.destination'
        db.add_column(u'compoundcalendar_icalsource', 'destination',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compoundcalendar.Calendar'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Calendar', fields ['site', 'slug']
        db.delete_unique(u'compoundcalendar_calendar', ['site_id', 'slug'])

        # Deleting model 'Calendar'
        db.delete_table(u'compoundcalendar_calendar')

        # Deleting field 'IcalSource.destination'
        db.delete_column(u'compoundcalendar_icalsource', 'destination_id')


    models = {
        u'compoundcalendar.calendar': {
            'Meta': {'unique_together': "(('site', 'slug'),)", 'object_name': 'Calendar'},
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
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['compoundcalendar']