from django.views.generic import (TemplateView,
                                  CreateView,
                                  ListView,
                                  UpdateView,
                                  DetailView,
                                  DeleteView)
from django.http import HttpResponse

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import Group, Event
from .forms import GroupCreateForm
from .mixins import GroupMixin, EventSubmissionMixin


class FrontPage(ListView):
    template_name = 'communitycalendar/index.html'


class SiteEdit(StaffuserRequiredMixin, UpdateView):
    template_name = 'communitycalendar/edit_site.html'


class GroupCreate(LoginRequiredMixin, CreateView):
    form_class = GroupCreateForm
    template_name = 'communitycalendar/group_create.html'


class GroupDetail(GroupMixin, TemplateView):
    template_name = 'communitycalendar/group_detail.html'


class GroupUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'communitycalendar/update_group.html'


class GroupList(ListView):
    model = Group


class GroupDelete(LoginRequiredMixin, DeleteView):
    template_name = 'comminitycalendar/delete_group.html'


class EventCreateForGroup(EventSubmissionMixin,
                          GroupMixin, LoginRequiredMixin, TemplateView):
    template_name = 'communitycalendar/create_event_for_group.html'

    def post(self, request, **kwargs):
        forms = self.forms()
        event_details_form = forms['event_form']
        event_instance_formset = forms['event_instance_formset']
        if event_details_form.is_valid() and event_instance_formset.is_valid():
          pass
        return self.get(request)


class EventCreate(LoginRequiredMixin, CreateView):
    template_name = 'communitycalendar/create_event.html'


class EventDetail(DetailView):
    template_name = 'communitycalendar/event_detail.html'


class EventEdit(LoginRequiredMixin, UpdateView):
    template_name = 'communitycalendar/update_event.html'


class EventDelete(LoginRequiredMixin, DeleteView):
    template_name = 'communitycalendar/delete_event.html'


class ApplyToOrganize(CreateView):
    template_name = 'communitycalendar/apply_to_organize.html'


class InviteToOrganize(LoginRequiredMixin, CreateView):
    template_name = 'communitycalendar/invite_to_organize.html'


class ApplyToMod(CreateView):
    template_name = 'communitycalendar/apply_to_mod.html'


class InviteToMod(LoginRequiredMixin, CreateView):
    template_name = 'communitycalendar/invite_to_organize.html'


class ModerationQueue(ListView):
    template_name = 'communitycalendar/moderate.html'


class AcceptInvitation(UpdateView):
    template_name = 'communitycalendar/accept_invitation.html'


class ReportAProblem(CreateView):
    template_name = 'communitycalendar/report_trouble.html'
