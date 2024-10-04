from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Package
from .forms import PackageForm


class PackageListView(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'package_list.html'
    context_object_name = 'packages'

    def get_queryset(self):
        return Package.objects.all()


class PackageCreateView(LoginRequiredMixin, FormView):
    model = Package
    form_class = PackageForm
    template_name = 'package_form.html'
    success_url = reverse_lazy('list_packages')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)

    def _create_tier(self, tier):
        """Create a tier and add it to the package."""
        package = self.object
        package.tiers.add(tier)
        package.save()


class PackageEditView(LoginRequiredMixin, UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'package_form.html'
    success_url = reverse_lazy('list_packages')

    def _update_tier(self, tier):
        """Update a tier and add it to the package."""
        package = self.object
        # Update the tier
        tier = package.tiers.get(id=tier.id)

        if tier:
            tier.name = tier.name
            tier.description = tier.description
            tier.features = tier.features
            tier.save()
