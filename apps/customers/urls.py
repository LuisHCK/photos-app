from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='list_customers'),
    path('create/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('<int:pk>/edit/', views.CustomerEditView.as_view(), name='edit_customer'),
]
