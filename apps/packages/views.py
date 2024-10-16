from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Package, Tier
from .forms import PackageForm, TierForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tiers'] = Tier.objects.filter(package=self.object)
        return context

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


class TiersListView(LoginRequiredMixin, ListView):
    model = Tier
    template_name = 'tiers_list.html'
    context_object_name = 'tiers'

    def get_queryset(self):
        return Tier.objects.filter(package=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['package'] = Package.objects.get(id=self.kwargs['pk'])
        return context

    def is_ajax(self):
        return self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get_template_names(self):
        if self.is_ajax():
            return ['partials/_tier_list.html']
        return ['tiers_list.html']


class TierCreateView(LoginRequiredMixin, FormView):
    model: Tier
    form_class = TierForm
    template_name = 'tier_form.html'

    def form_valid(self, form):
        features = form.instance.features

        if features:
            features = features[0].split('\r\n')

        form.instance.features = features
        form.instance.package = Package.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_tiers', kwargs={'pk': self.kwargs['pk']})


class TierUpdateView(LoginRequiredMixin, UpdateView):
    model = Tier
    form_class = TierForm
    template_name = 'tier_form.html'

    def get_object(self):
        tier = Tier.objects.filter(
            id=self.kwargs['pk'], package=self.kwargs['package_pk'])
        return super().get_object(tier)

    def form_valid(self, form):
        features = form.instance.features
        if features:
            features = features[0].split('\r\n')
            print(features[0])

        form.instance.features = features
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_tiers', kwargs={'pk': self.kwargs['package_pk']})


class TierDeleteView(LoginRequiredMixin, DeleteView):
    model = Tier
    template_name = 'tier_confirm_delete.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_object(self):
        tier = Tier.objects.filter(
            id=self.kwargs['pk'], package=self.kwargs['package_pk'])
        return super().get_object(tier)

    def get_success_url(self):
        print('hola')
        return reverse_lazy('edit_package', kwargs={'pk': self.kwargs['package_pk']})
