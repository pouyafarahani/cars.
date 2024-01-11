from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, FactorListView, FactorDetailView

app_name = 'pages'

urlpatterns = [
    path('', HomeView, name='home'),
    path('factor/', FactorListView.as_view(), name='factor'),
    path('factor/<int:pk>/', FactorDetailView.as_view(), name='factor'),
]
