from django.views.generic import TemplateView
from django.core.signing import Signer
from .models import Session


class SessionDetailView(TemplateView):
    template_name = "public-session.html"

    def get_template_names(self):
        slug = self.kwargs.get('slug')
        unavailable_statuses = ('expired', 'deleted')
        is_staff = self.request.user.is_staff
        session_unavailable = Session.objects.get(access_slug=slug).status in unavailable_statuses

        if session_unavailable and not is_staff:
            return ["session-unavailable.html"]
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        session = Session.objects.get(access_slug=slug)
        photos = session.photo_set.all()
        return super().get_context_data(session=session, photos=photos, **kwargs)
