from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('shortener.urls', namespace='shortener')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stats/', include('shortener.urls_stats', namespace='shortener')),
    url(r'^add/', include('shortener.urls_add', namespace='shortener')),
    url(r'^l/', include('shortener.urls_link', namespace='shortener')),
)
