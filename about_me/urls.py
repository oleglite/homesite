#coding: utf-8
from django.conf.urls import patterns, url

from about_me.views import about_me, contacts

urlpatterns = patterns('',
       url(r'^about_me$', about_me, name='about_me'),
       url(r'^contacts$', contacts, name='contacts'),
)