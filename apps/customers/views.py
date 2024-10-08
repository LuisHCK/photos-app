from .models import Customer
from .forms import CustomerForm
from django.views.generic import ListView, FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'


class CustomerCreateView(LoginRequiredMixin, FormView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create.html'
    success_url = reverse_lazy('customers:list_customers')


class CustomerEditView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_create.html'
    success_url = reverse_lazy('customers:list_customers')
