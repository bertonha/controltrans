from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'controltrans.core.views.home', name='home'),
    url(r'^upload/$', 'controltrans.core.views.load_xml', name='upload'),
    # Examples:
    # url(r'^$', 'controltrans.views.home', name='home'),
    # url(r'^controltrans/', include('controltrans.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
