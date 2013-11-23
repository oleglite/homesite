#coding: utf-8
from django.conf.urls import patterns, url

from about_me.views import home

urlpatterns = patterns('',
       url(r'^about$', home, name='list'),
)