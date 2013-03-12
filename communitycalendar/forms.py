from django import forms
from django.forms.formsets import BaseFormSet

from .models import Group, Event, EventInstance


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'slug', 'description', 'link']


class EventInstanceForm(forms.ModelForm):

    class Meta:
        model = EventInstance
        fields = []
    date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField(required=False)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['summary', 'description', 'link']
    summary = forms.CharField(label='Event Name')


class BaseEventInstanceFormSet(BaseFormSet):
    def clean(self):
        if len(self.forms) <= self.extra:
            raise forms.ValidationError("You must include at least one date and time!")
