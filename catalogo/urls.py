from django.urls import path
from .views import ProductoListView, home

urlpatterns = [
    path('', home, name='home'),
    path('productos/', ProductoListView.as_view(), name='productos'),
]