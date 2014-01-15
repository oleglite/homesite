#coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from apps.about_me.views import about_me, contacts

urlpatterns = patterns('',
       url(r'^$', RedirectView.as_view(url='about_me', permanent=False), name='index'),
       url(r'^about_me$', about_me, name='about_me'),
       url(r'^contacts$', contacts, name='contacts'),
)