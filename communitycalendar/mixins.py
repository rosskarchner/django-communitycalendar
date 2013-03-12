import logging

from django.shortcuts import get_object_or_404
from django.forms.formsets import formset_factory

from .models import Group
from .forms import EventForm, EventInstanceForm, BaseEventInstanceFormSet


class GroupMixin(object):
    @property
    def group(self):
        group_lookup = {'pk': self.kwargs.get('group_slug')}
        return get_object_or_404(Group, **group_lookup)

    def get_context_data(self, **kwargs):
        context = super(GroupMixin, self).get_context_data(**kwargs)
        context['group'] = self.group
        return context


class EventSubmissionMixin(object):
    def forms(self):
        if hasattr(self, '_forms'):
            return self._forms

        forms = {}

        EventInstanceFormset = formset_factory(
            EventInstanceForm,
            formset=BaseEventInstanceFormSet,
            extra=1)

        if self.request.method == 'POST':
            forms['event_form'] = EventForm(self.request.POST, prefix='details')
            forms['event_instance_formset'] = EventInstanceFormset(self.request.POST)

        else:
            forms['event_form'] = EventForm(prefix='details')
            forms['event_instance_formset'] = EventInstanceFormset()

        self._forms = forms
        return forms

    def get_context_data(self, **kwargs):
        context = super(EventSubmissionMixin, self).get_context_data(**kwargs)
        if hasattr(self, '__forms'):
            context.update(self.__form)
        else:
            context.update(self.forms())

        context.update(self.forms())
        return context
