from django.urls import URLPattern, path
from modules.maaji.api.api import ClienteAPIview

urlpatterns = [
    path('cliente/', ClienteAPIview.as_view(), name = 'cliente_api')
]