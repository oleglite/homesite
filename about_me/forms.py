from django import forms
from django.forms import ModelForm

from models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

    def clean(self):
        cleaned_data = super(EducationForm, self).clean()
        start_date = cleaned_data.get('start_date')
        completion_date = cleaned_data.get('completion_date')

        if completion_date and start_date > completion_date:
            raise forms.ValidationError('Start date must be earlier than completion date.', code='invalid')

        return cleaned_data

