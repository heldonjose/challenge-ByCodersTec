from django.conf.urls.static import static
from django.urls import path

from projeto import settings
from . import views

app_name = 'core'

urlpatterns = [
              ] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)