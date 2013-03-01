from django.conf.urls import patterns, url

from communitycalendar.views import FrontPage


urlpatterns = patterns('communitycalendar.views',
    url(r'^$', FrontPage.as_view()
        ),
)
