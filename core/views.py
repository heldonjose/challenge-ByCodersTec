import codecs
from django.contrib.auth import  login as django_login

from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from extra_views import SearchableListMixin
from core.models import Company, ImportCNAB


class RedirecAuthenticationView(TemplateView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('core:login')
        return redirect('core:store_list_view')


class LoginView(TemplateView):
    template_name = 'core/pages/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            return redirect('core:store_list_view')


class StoreListView(LoginRequiredMixin, SearchableListMixin, ListView):
    model = Company
    template_name = 'core/pages/store/list.html'
    search_fields = ['name', 'owner__name', ]

    def get_context_data(self, **kwargs):
        context = super(StoreListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q') if self.request.GET.get('q') else ''
        return context


class ImportFileCreateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('core:store_list_view')

    def get(self, request, *args, **kwargs):
        return redirect('core:store_list_view')

    def post(self, request, *args, **kwargs):
        ImportCNAB.objects.create(file=request.FILES.get('importFile'))
        return HttpResponseRedirect(self.success_url)
