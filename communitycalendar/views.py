from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DetailView,
                                  DeleteView)

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .models import Group
from .forms import GroupCreateForm


class FrontPage(ListView):
    template_name = 'communitycalendar/index.html'


class SiteEdit(StaffuserRequiredMixin, UpdateView):
    template_name = 'communitycalendar/edit_site.html'


class GroupCreate(LoginRequiredMixin, CreateView):
    form_class = GroupCreateForm
    template_name = 'communitycalendar/group_create.html'


class GroupDetail(DetailView):
    template_name = 'communitycalendar/group.html'
    model = Group


class GroupUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'communitycalendar/update_group.html'


class GroupList(ListView):
    model = Group


class GroupDelete(LoginRequiredMixin, DeleteView):
    template_name = 'comminitycalendar/delete_group.html'


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
