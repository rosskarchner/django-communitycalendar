# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'compoundcalendar_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'compoundcalendar', ['Event'])

        # Adding field 'SiteSettings.default_destination'
        db.add_column(u'compoundcalendar_sitesettings', 'default_destination',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['compoundcalendar.Calendar']),
                      keep_default=False)

        # Deleting field 'IcalSource.destination'
        db.delete_column(u'compoundcalendar_icalsource', 'destination_id')

        # Adding M2M table for field destination on 'IcalSource'
        db.create_table(u'compoundcalendar_icalsource_destination', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('icalsource', models.ForeignKey(orm[u'compoundcalendar.icalsource'], null=False)),
            ('calendar', models.ForeignKey(orm[u'compoundcalendar.calendar'], null=False))
        ))
        db.create_unique(u'compoundcalendar_icalsource_destination', ['icalsource_id', 'calendar_id'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'compoundcalendar_event')

        # Deleting field 'SiteSettings.default_destination'
        db.delete_column(u'compoundcalendar_sitesettings', 'default_destination_id')

        # Adding field 'IcalSource.destination'
        db.add_column(u'compoundcalendar_icalsource', 'destination',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compoundcalendar.Calendar'], null=True),
                      keep_default=False)

        # Removing M2M table for field destination on 'IcalSource'
        db.delete_table('compoundcalendar_icalsource_destination')


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
        u'compoundcalendar.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'summary': ('django.db.models.fields.TextField', [], {})
        },
        u'compoundcalendar.icalsource': {
            'Meta': {'object_name': 'IcalSource'},
            'destination': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compoundcalendar.Calendar']", 'symmetrical': 'False'}),
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
            'default_destination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compoundcalendar.Calendar']"}),
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