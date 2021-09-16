import codecs

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from core.forms import ImportCNABForm
from core.internal_Objects import ImportLine
from core.models import Company, ImportCNAB


class RedirecAuthenticationView(TemplateView):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('core:login')
        return redirect('core:store_list_view')


class LoginView(TemplateView):
    template_name = 'core/pages/login.html'


class StoreListView(ListView):
    model = Company
    template_name = 'core/pages/store/list.html'


from io import TextIOWrapper


class ImportFileCreateView(View):
    success_url = reverse_lazy('core:store_list_view')

    def get(self, request, *args, **kwargs):
        return redirect('core:store_list_view')

    def post(self, request, *args, **kwargs):
        ImportCNAB.objects.create(file=request.FILES.get('importFile'))
        return HttpResponseRedirect(self.success_url)
