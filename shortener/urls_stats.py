from django.conf.urls import patterns, include, url
from shortener import views

urlpatterns = patterns('',
    url(r'^(?P<lid>[a-zA-Z0-9]+)$', views.stats),
)
