from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auDjango.views.home', name='home'),
    # url(r'^auDjango/', include('auDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^start/$', 'start.views.start'),
    url(r'^record/$', 'record.views.rec'),
    url(r'^new/$', 'newDB.views.new'),
    #url(r'^show/$', 'showDB.view.show'),

)
