from django.views.generic import TemplateView
from django.contrib.sites.models import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings as django_settings


class SiteMixin(object):
    @property
    def site(self):
        return get_current_site(self.request)

    @property
    def site_settings(self):
        try:
            return self.site.sitesettings_set.get()
        except ObjectDoesNotExist:
            timezone = django_settings.TIME_ZONE
            settings = self.site.sitesettings_set.create(
                default_timezone=timezone)
            settings.save()
            return settings

    def get_context_data(self, **kwargs):
        context = super(SiteMixin,
                        self).get_context_data(**kwargs)
        context["site"] = self.site
        context["site_settings"] = self.site_settings
        return context


class FrontPage(SiteMixin, TemplateView):
    template_name = 'communitycalendar/index.html'
