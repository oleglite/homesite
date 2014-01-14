# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'about_me_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'about_me', ['Location'])

        # Adding model 'PersonalInfo'
        db.create_table(u'about_me_personalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.Location'])),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('photo_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'about_me', ['PersonalInfo'])

        # Adding model 'School'
        db.create_table(u'about_me_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.Location'])),
            ('school_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'about_me', ['School'])

        # Adding model 'Education'
        db.create_table(u'about_me_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.School'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.PersonalInfo'])),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('speciality', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('completion_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'about_me', ['Education'])

        # Adding model 'Skill'
        db.create_table(u'about_me_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'about_me', ['Skill'])

        # Adding model 'Technology'
        db.create_table(u'about_me_technology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('technology_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.Skill'])),
        ))
        db.send_create_signal(u'about_me', ['Technology'])

        # Adding model 'TechnologyCompetence'
        db.create_table(u'about_me_technologycompetence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('technology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.Technology'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about_me.PersonalInfo'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'about_me', ['TechnologyCompetence'])

        # Adding model 'Project'
        db.create_table(u'about_me_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('project_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'about_me', ['Project'])

        # Adding M2M table for field technologies on 'Project'
        m2m_table_name = db.shorten_name(u'about_me_project_technologies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'about_me.project'], null=False)),
            ('technology', models.ForeignKey(orm[u'about_me.technology'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'technology_id'])

        # Adding M2M table for field executor on 'Project'
        m2m_table_name = db.shorten_name(u'about_me_project_executor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'about_me.project'], null=False)),
            ('personalinfo', models.ForeignKey(orm[u'about_me.personalinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'personalinfo_id'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'about_me_location')

        # Deleting model 'PersonalInfo'
        db.delete_table(u'about_me_personalinfo')

        # Deleting model 'School'
        db.delete_table(u'about_me_school')

        # Deleting model 'Education'
        db.delete_table(u'about_me_education')

        # Deleting model 'Skill'
        db.delete_table(u'about_me_skill')

        # Deleting model 'Technology'
        db.delete_table(u'about_me_technology')

        # Deleting model 'TechnologyCompetence'
        db.delete_table(u'about_me_technologycompetence')

        # Deleting model 'Project'
        db.delete_table(u'about_me_project')

        # Removing M2M table for field technologies on 'Project'
        db.delete_table(db.shorten_name(u'about_me_project_technologies'))

        # Removing M2M table for field executor on 'Project'
        db.delete_table(db.shorten_name(u'about_me_project_executor'))


    models = {
        u'about_me.education': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'Education'},
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
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
            'order': ('django.db.models.fields.IntegerField', [], {}),
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
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'about_me.technology': {
            'Meta': {'object_name': 'Technology'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.Skill']"}),
            'technology_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'about_me.technologycompetence': {
            'Meta': {'object_name': 'TechnologyCompetence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.PersonalInfo']"}),
            'technology': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['about_me.Technology']"})
        }
    }

    complete_apps = ['about_me']