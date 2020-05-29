from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Duty

class DutyListView(ListView):
    model = Duty
    template_name = 'duty_list.html'


class DutyUpdateView(UpdateView):
    model = Duty
    fields = ('title', 'body', 'point_value')
    template_name = 'duty_edit.html'


class DutyDetailView(DetailView):
    model = Duty
    template_name = 'duty_detail.html'

class DutyDeleteView(DeleteView):
    model = Duty
    template_name = 'duty_delete.html'
    success_url = reverse_lazy('duty_list')


class DutyClaimView(ListView):
    model = Duty
    template_name = 'duty_claim.html'

class DutyCreateView(CreateView):
    model = Duty
    template_name = 'duty_new.html'
    fields = ('title', 'point_value', 'body', 'author',)
