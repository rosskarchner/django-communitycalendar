from django.db import models
from django.contrib.sites.models import Site
# from django.contrib.auth.models import User


class IcalSource(models.Model):
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=255)
    source_link = models.URLField()
    ical_href = models.URLField()
    last_fetch = models.DateTimeField(blank=True, null=True)
    next_fetch = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name
