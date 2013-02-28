from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^compoundcalendar/',
        include('compoundcalendar.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
