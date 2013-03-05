from django import forms

from .models import Group, Event, EventInstance


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'slug', 'description', 'link']


class EventInstanceForm(forms.ModelForm):
    class Meta:
        model = EventInstance
        fields = ['dtstart', 'end_time']


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['summary', 'description']
