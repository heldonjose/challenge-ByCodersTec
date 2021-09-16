from django.conf.urls.static import static
from django.urls import path

from projeto import settings
from . import views

app_name = 'core'

urlpatterns = [
                  path('', views.RedirecAuthenticationView.as_view(), name='redirect_authentication'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('logout/', views.LogoutRedirectViews.as_view(), name='logout'),
                  path('store/list/', views.StoreListView.as_view(), name='store_list_view'),
                  path('store/import/create/', views.ImportFileCreateView.as_view(), name='store_import_create_view'),
              ] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
