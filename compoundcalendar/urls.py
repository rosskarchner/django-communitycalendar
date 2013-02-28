from django.conf.urls import patterns, include, url

from compoundcalendar.views import FrontPage


urlpatterns = patterns('compoundcalendar.views',
    url(r'^$', FrontPage.as_view()
        ),
)
