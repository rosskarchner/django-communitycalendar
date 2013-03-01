from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class SiteSettings(models.Model):
    site = models.ForeignKey(Site)
    default_timezone = models.CharField(max_length=255)
    guidelines = models.TextField(blank=True)


class Group(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    ical_url = models.URLField(null=True, blank=True)
    organizers = models.ManyToManyField(User, related_name="groups_organizing")
    followers = models.ManyToManyField(User, related_name="groups_following")


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
    source_type = models.ForeignKey(ContentType, null=True)
    source_id = models.CharField(max_length=500, null=True)
    source = generic.GenericForeignKey('source_type', 'source_id')
    all_day = models.BooleanField(default=False)
