from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from core.models import Store


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
