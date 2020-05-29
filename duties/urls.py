from django.urls import path

from .views import (DutyListView, DutyUpdateView, DutyDetailView, DutyDeleteView, DutyClaimView, DutyCreateView,)

urlpatterns = [
    path('new/', DutyCreateView.as_view(), name='duty_new'),

    path('<int:pk>/edit/', DutyUpdateView.as_view(),name='duty_edit'),
    
    path('<int:pk>/', DutyDetailView.as_view(), name='duty_detail'),
    
    path('<int:pk>/delete/', DutyDeleteView.as_view(),name='duty_delete'),
    
    path('<int:pk/claim/', DutyClaimView.as_view(), name='duty_claim'),
    
    path('', DutyListView.as_view(), name='duty_list'),
    
    ]
