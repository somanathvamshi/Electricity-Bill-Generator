from django.urls import path
from . import views
from .views import ElcListView,ElcCreateView,ElcDetailView,ElcUpdateView,ElcDeleteView,GeneratePDF
urlpatterns = [
    path('',ElcListView.as_view() ,name='elc-home'),
    
    path('bill/create/',ElcCreateView.as_view(),name = 'elc-create'),
    path('bill/<int:pk>',ElcDetailView.as_view(),name = 'elc-detail'),
    path('bill/<int:pk>/pdf',GeneratePDF.as_view(),name = 'elc-pdf'),
    path('bill/<int:pk>/update',ElcUpdateView.as_view(),name = 'elc-update'),
    path('bill/<int:pk>/delete',ElcDeleteView.as_view(),name = 'elc-delete'),
]