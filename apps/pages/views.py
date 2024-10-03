from django.views.generic import TemplateView
from .models import Page


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = None

        print('HomepageView')

        try:
            page = Page.objects.get(slug='homepage')
            print('details', page.data['details'])
        except Page.DoesNotExist:
            print('Homepage data not found')

        context['page'] = page
        
        return context
