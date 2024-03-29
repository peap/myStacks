from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stackManager.views.home', name='home'),
    url(r'^collections/$', 'stackManager.views.collections', name='collections'),
    url(r'^collections/create/$', 'stackManager.views.create_collection', name='create_collection'),
    url(r'^items/$', 'stackManager.views.items', name='items'),
    url(r'^wishlist/$', 'stackManager.views.wishlist', name='wishlist'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
