from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse


class SiteSettings(models.Model):
    site = models.ForeignKey(Site)
    default_timezone = models.CharField(max_length=255)
    guidelines = models.TextField(blank=True)


class Group(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100, primary_key=True)
    description = models.TextField()
    link = models.URLField(blank=True)
    redirect = models.BooleanField(default=False)
    ical_url = models.URLField(null=True, blank=True)
    organizers = models.ManyToManyField(User,
                                        related_name="groups_organizing",
                                        blank=True,
                                        null=True)
    followers = models.ManyToManyField(User,
                                       related_name="groups_following",
                                       blank=True,
                                       null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group-detail', kwargs={'slug': self.slug})


class Event(models.Model):
    site = models.ForeignKey(Site)
    slug = models.SlugField(max_length=100, primary_key=True)
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
