from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class SiteSettings(models.Model):
    site = models.ForeignKey(Site)
    default_timezone = models.CharField(max_length=255)
    everyone_can_endorse = models.BooleanField(default=False)
    source_endorsement_threshhold = models.IntegerField(default=1)
    event_endorsement_threshhold = models.IntegerField(default=1)
    guidelines = models.TextField(blank=True)


class IcalSource(models.Model):
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=255)
    source_link = models.URLField()
    ical_href = models.URLField()
    last_fetch = models.DateTimeField(blank=True, null=True)
    next_fetch = models.DateTimeField(blank=True, null=True)
    overide_timezone = models.CharField(max_length=255, blank=True, null=True)
    submitted_by = models.ForeignKey(User, null=True)
    fully_endorsed_at = models.DateTimeField(null=True)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.site)


class Event(models.Model):
    site = models.ForeignKey(Site)
    summary = models.TextField()
    description = models.TextField(blank=True)
    geo = models.CharField(max_length=255, blank=True)
    location = models.TextField(blank=True)
    dtstart = models.DateTimeField()
    dtend = models.DateTimeField(null=True)
    status = models.CharField(max_length=255)
    rrule = models.TextField(blank=True)
    ical_last_seen = models.DateTimeField(null=True)
    source_type = models.ForeignKey(ContentType)
    source_id = models.CharField(max_length=500)
    source = generic.GenericForeignKey('source_type', 'source_id')
    all_day = models.BooleanField(default=False)
    fully_endorsed_at = models.DateTimeField(null=True)


class SourceEndorsements(models.Model):
    ical = models.ForeignKey(IcalSource)
    endorsers = models.ManyToManyField(User, related_name="endorsed_sources")


class EventEndorsements(models.Model):
    event = models.ForeignKey(Event)
    endorsers = models.ManyToManyField(User, related_name="endorsed_events")
