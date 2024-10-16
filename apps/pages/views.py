from django.views.generic import TemplateView
from .models import Page
from apps.packages.models import Package


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = None
        packages = Package.objects.filter(display_on_homepage=True)

        try:
            page = Page.objects.get(slug='homepage')
        except Page.DoesNotExist:
            print('Homepage data not found')

        context['page'] = page
        context['packages'] = packages
        
        return context
