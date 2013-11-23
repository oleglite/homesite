from django.db import models
import datetime

import validators


# https://github.com/ckelly/django-resume/blob/master/django_resume/resume/models.py


def today():
    return datetime.datetime.now()


class Location(models.Model):
    city = models.CharField(max_length=255, help_text="e.g. city such as Minsk")
    country = models.CharField(max_length=255, help_text="e.g. country such as Belarus")

    def __unicode__(self):
        return '%s, %s' % (self.city, self.country)


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=255, blank=True)

    location = models.ForeignKey(Location)
    birthday = models.DateField()

    photo_url = models.URLField(verbose_name='Photo URL', blank=True)
    summary = models.TextField()

    def age(self):
        age = today() - self.birthday
        return age.year

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class School(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=20, blank=True)
    location = models.ForeignKey(Location)
    school_url = models.URLField(verbose_name='School URL', blank=True)

    def __unicode__(self):
        return self.name


class Education(models.Model):
    school = models.ForeignKey(School)
    person = models.ForeignKey(PersonalInfo)
    department = models.CharField(max_length=255, blank=True)
    speciality = models.CharField(max_length=255, blank=True)

    start_date = models.DateField()
    completion_date = models.DateField(blank=True)

    summary = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def is_current(self):
        return not self.completion_date or today() < self.completion_date

    def __unicode__(self):
        return '%s - %s' % (self.person, self.school)


class Skill(models.Model):
    name =  models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=255, unique=True)
    technology_url = models.URLField('Technology URL', blank=True)
    skill = models.ForeignKey(Skill)

    class Meta:
        verbose_name_plural = 'Technologies'

    def __unicode__(self):
        return self.name


class TechnologyCompetence(models.Model):
    technology = models.ForeignKey(Technology)
    person = models.ForeignKey(PersonalInfo)
    level = models.IntegerField(validators=[validators.validate_level])

    def __unicode__(self):
        return '%s - %s - %i' % (self.person, self.technology, self.level)


class Project(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    client = models.CharField(max_length=255, blank=True)
    project_url = models.URLField('Project URL', blank=True)
    technologies = models.ManyToManyField(Technology)
    executor = models.ManyToManyField(PersonalInfo)

    summary = models.TextField()

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name