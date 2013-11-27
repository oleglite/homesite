# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'about_me_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.PersonalInfo'])),
            ('is_important', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'about_me', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'about_me_contact')


    models = {
        u'about_me.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_important': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.PersonalInfo']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'about_me.education': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Education'},
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.PersonalInfo']"}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.School']"}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'about_me.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'about_me.personalinfo': {
            'Meta': {'object_name': 'PersonalInfo'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.Location']"}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {})
        },
        u'about_me.project': {
            'Meta': {'ordering': "['order']", 'object_name': 'Project'},
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'executor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['about_me.PersonalInfo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '9'}),
            'project_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['about_me.Technology']", 'symmetrical': 'False'})
        },
        u'about_me.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'about_me.skill': {
            'Meta': {'ordering': "['order']", 'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '9'})
        },
        u'about_me.technology': {
            'Meta': {'object_name': 'Technology'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.Skill']"}),
            'technology_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'about_me.technologycompetence': {
            'Meta': {'ordering': "['-level']", 'object_name': 'TechnologyCompetence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.PersonalInfo']"}),
            'technology': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.Technology']"})
        }
    }

    complete_apps = ['about_me']