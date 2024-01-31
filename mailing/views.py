from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from mailing.models import Client, Mailing


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing_all'] = Mailing.objects.all().count()
        context_data['count_mailing_active'] = Mailing.objects.filter(is_active=True).count()
        context_data['count_unique_clients'] = Client.objects.distinct().count()
        # context_data['blog'] = Blog.objects.all().order_by('?')[:3]
        return context_data


class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.set_mailing_status'):
            return queryset

        return queryset.filter(user=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('email', 'full_name', 'comment')
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(UserPassesTestMixin, UpdateView):
    model = Client
    fields = ('email', 'full_name', 'comment')
    success_url = reverse_lazy('mailing:client_list')

    def test_func(self):
        client = self.get_object()
        user = self.request.user
        return user.is_authenticated and (client.user == user or user.has_perm('mailing.change_client'))


class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')

    def test_func(self):
        client = self.get_object()
        user = self.request.user
        return user.is_authenticated and (client.user == user or user.has_perm('mailing.delete_client'))