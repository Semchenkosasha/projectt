from django.urls import path

from .views import get_base_page

urlpatterns = [
    path ('', get_base_page)
]