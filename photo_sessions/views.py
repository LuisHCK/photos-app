from django.views.generic import TemplateView
from django.core.signing import Signer
from .models import Session


class SessionDetailView(TemplateView):
    template_name = "public-session.html"

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        session = Session.objects.get(access_slug=slug)
        photos = session.photo_set.all()
        return super().get_context_data(session=session, photos=photos, **kwargs)
