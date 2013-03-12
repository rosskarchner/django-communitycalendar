from django.conf.urls import patterns, url

from communitycalendar.views import *


urlpatterns = patterns('communitycalendar.views',
    url(r'^$', FrontPage.as_view(),
        name='communitycalendar-front'),

    url(r'^settings/$', SiteEdit.as_view(),
        name='site-settings'),

    url(r'^groups/create/$', GroupCreate.as_view(),
        name='group-create'),
    url(r'^groups/(?P<group_slug>[-_\w]+)/$', GroupDetail.as_view(),
        name='group-detail'),
    url('^groups/(?P<group_slug>[-_\w]+)/edit/$', GroupUpdate.as_view(),
        name='group-update'),
    url('^groups/(?P<group_slug>[-_\w]+)/delete/', GroupDelete.as_view(),
        name='group-delete'),
    url('^groups/$', GroupList.as_view(),
        name='group-list'),
    url('^groups/(?P<group_slug>[-_\w]+)/apply-to-organize/',
        ApplyToOrganize.as_view(),
        name='apply-to-organize'),
    url('^groups/(?P<group_slug>[-_\w]+)/invite-to-organize/',
        InviteToOrganize.as_view(),
        name='invite_to_organize'),
    url('^groups/(?P<group_slug>[-_\w]+)/add-an-event/$',
        EventCreateForGroup.as_view(),
        name='event-add-for-group'),

)
