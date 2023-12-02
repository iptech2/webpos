from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_dashboard, name='invoice_dashboard'),
    path('employees/', views.customer_invoice, name='customer_invoice')
]
