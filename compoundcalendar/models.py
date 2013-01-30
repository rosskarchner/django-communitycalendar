from django.db import models
from django.contrib.sites.models import Site


class SiteSettings(models.Model):
    site = models.ForeignKey(Site)
    default_timezone = models.CharField(max_length=255)
    default_destination = models.ForeignKey('Calendar')
    #TODO: find a package that provides a real timezone field


class IcalSource(models.Model):
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=255)
    source_link = models.URLField()
    ical_href = models.URLField()
    last_fetch = models.DateTimeField(blank=True, null=True)
    next_fetch = models.DateTimeField(blank=True, null=True)
    destination = models.ForeignKey("Calendar", null=True)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.site)


class Calendar(models.Model):
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    staff_only = models.BooleanField()
    default_timezone = models.CharField(max_length=255)
    #TODO: find a package that provides a real timezone field

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = (("site", "slug"),)
