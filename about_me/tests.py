import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError

from models import Location, Education
from forms import EducationForm
from validators import validate_level


def date(day, month, year):
    return datetime.datetime(year, month, day)


class EducationModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(city='London', country='Britan')

    def test_is_current__completion_date_is_none(self):
        edu = Education(name='Hogwarts',
                        start_date=date(20, 10, 2013))
        self.assertTrue(edu.is_current())

    def test_is_current__completion_date_is_in_past(self):
        edu = Education(name='Hogwarts',
                        start_date=date(20, 10, 2013), completion_date=date(22, 10, 2013))
        self.assertFalse(edu.is_current())

    def test_is_current__completion_date_is_in_future(self):
        edu = Education(name='Hogwarts',
                        start_date=date(20, 10, 2013), completion_date=date(20, 10, 2200))
        self.assertTrue(edu.is_current())


class EducationFormTest(TestCase):
    def setUp(self):
        Location.objects.create(city='London', country='Britan')
        self.location_id = Location.objects.all()[0].id

    def create_form(self, **data):
        data.update({'location': self.location_id})
        return EducationForm(data)

    def test_clean__validate_start_date_less_than_completion_date(self):
        form = self.create_form(name='Hogwarts', start_date=date(20, 10, 2013), completion_date=date(10, 10, 2013))
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['__all__'], [u'Start date must be earlier than completion date.'])

    def test_clean__validate_start_date_greater_than_completion_date(self):
        form = self.create_form(name='Hogwarts', start_date=date(10, 10, 2013), completion_date=date(20, 10, 2013))
        self.assertTrue(form.is_valid())

    def test_clean__validate_start_date_equal_completion_date(self):
        form = self.create_form(name='Hogwarts', start_date=date(10, 10, 2013), completion_date=date(10, 10, 2013))
        self.assertTrue(form.is_valid())

    def test_clean__validate_empty_completion_date(self):
        form = self.create_form(name='Hogwarts', start_date=date(10, 10, 2013))
        self.assertTrue(form.is_valid())


class TestValidateLevel(TestCase):
    def test_validate_level_less(self):
        with self.assertRaises(ValidationError):
            validate_level(-1)

    def test_validate_level_ok(self):
        validate_level(100)
        validate_level(0)

    def test_validate_level_greater(self):
        with self.assertRaises(ValidationError):
            validate_level(101)