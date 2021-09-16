from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from core.forms import ImportCNADForm
from core.models import Store, ImportCNAD


class RedirecAuthenticationView(TemplateView):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('core:login')
        return redirect('core:store_list_view')


class LoginView(TemplateView):
    template_name = 'core/pages/login.html'


class StoreListView(ListView):
    model = Store
    template_name = 'core/pages/store/list.html'


class ImportFileCreateView(View):
    success_url = reverse_lazy('core:store_list_view')

    def post(self, request, *args, **kwargs):
        print('POST')
        return HttpResponseRedirect(self.success_url)
