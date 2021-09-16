import codecs

from django.contrib import messages
from django.contrib.auth import login as django_login, logout

from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, RedirectView
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
        messages.error(request, 'Login ou senha inválida')
        return redirect('core:login')

class LogoutRedirectViews(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('core:redirect_authentication')

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
        messages.success(request, 'Arquivo importando com sucesso!')
        return HttpResponseRedirect(self.success_url)
