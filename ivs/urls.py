from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
)
