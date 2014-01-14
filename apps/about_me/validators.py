from django.core.exceptions import ValidationError


def validate_level(value):
    """ IntegerField validator for numbers from 0 to 100 """
    if not (0 <= value <= 100):
        raise ValidationError(u'%s is not a level value (level is number from 0 to 100)' % value)