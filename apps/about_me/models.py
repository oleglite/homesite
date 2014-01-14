import datetime
import collections
from babel.dates import format_timedelta, format_date

from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import to_locale, get_language
from django.utils.translation import ugettext as _
from apps.about_me import validators


# https://github.com/ckelly/django-resume/blob/master/django_resume/resume/models.py

validate_url = URLValidator()


def formatted_date(date):
    return format_date(date, "LLLL yyyy", locale=get_locale())


def get_locale():
    return to_locale(get_language())


class Location(models.Model):
    city = models.CharField(max_length=255, help_text="e.g. city such as Minsk")
    country = models.CharField(max_length=255, help_text="e.g. country such as Belarus")

    def __unicode__(self):
        return u'%s, %s' % (self.city, self.country)


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
        born = self.birthday
        today = datetime.date.today()
        try:
            birthday = born.replace(year=today.year)
        except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
            birthday = born.replace(year=today.year, day=born.day - 1)
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    def age_formatted(self):
        delta = datetime.timedelta(self.age() * 365)
        return format_timedelta(delta, granularity='year', locale=get_locale())

    def skills(self):
        """ return dict of skills with list of person's technology competences as value """

        # use OrderedDict to save skills ordering
        skills = collections.OrderedDict()

        for skill in Skill.objects.all():
            technologies = Technology.objects.filter(skill=skill)
            competences = self.technologycompetence_set.filter(technology__in=technologies)
            if competences:
                skills[skill] = competences

        return skills

    def email(self):
        try:
            email = self.contact_set.get(name='email')
        except PersonalInfo.MultipleObjectsReturned:
            email = self.contact_set.filter(name='email')[0]
        except ObjectDoesNotExist:
            return ''
        return email

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    person = models.ForeignKey(PersonalInfo)
    order = models.SmallIntegerField(default=9)

    class Meta:
        ordering = ['order']

    def is_link(self):
        try:
            validate_url(self.value)
            return True
        except ValidationError, e:
            return False

    def __unicode__(self):
        return u'%s: %s' % (self.name, self.value)


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
    completion_date = models.DateField(null=True, blank=True)

    summary = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def is_current(self):
        return not self.completion_date or datetime.date.today() < self.completion_date

    def date_range(self):
        start_str = self.formatted_start_date()
        completion_str = _('Today') if self.is_current() else self.formatted_completion_date()
        return '%s - %s' % (start_str, completion_str)

    def formatted_start_date(self):
        return formatted_date(self.start_date)

    def formatted_completion_date(self):
        return formatted_date(self.completion_date)

    def __unicode__(self):
        return u'%s - %s' % (self.person, self.school)


class Skill(models.Model):
    name =  models.CharField(max_length=255)
    order = models.IntegerField(default=9)

    class Meta:
        ordering = ['order']

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
    level = models.IntegerField(validators=[validators.validate_level], help_text='number from 0 to 100')

    class Meta:
        ordering = ['-level']

    def __unicode__(self):
        return u'%s - %s - %i/100' % (self.person, self.technology, self.level)


class Project(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=9)
    client = models.CharField(max_length=255, blank=True)
    project_url = models.URLField('Project URL', blank=True)
    technologies = models.ManyToManyField(Technology)
    executor = models.ManyToManyField(PersonalInfo)

    summary = models.TextField()

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name