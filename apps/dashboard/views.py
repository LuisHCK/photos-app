from django.shortcuts import redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.photo_sessions.models import Session, Photo
from apps.photo_sessions.forms import SessionForm
from apps.customers.models import Customer
from apps.photo_sessions.tasks import delete_photos


class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        sessions = Session.objects.all().order_by('-id')
        total_customers = Customer.objects.count()
        total_photos = Photo.objects.count()
        return super().get_context_data(sessions=sessions, total_customers=total_customers, total_photos=total_photos, **kwargs)


class SessionPageView(LoginRequiredMixin, TemplateView):
    template_name = "session.html"

    def get_context_data(self, **kwargs):
        session = Session.objects.get(pk=self.kwargs.get('session_id'))
        form = SessionForm(instance=session)
        return super().get_context_data(session=session, form=form, **kwargs)

    def post(self, request, *args, **kwargs):
        session = Session.objects.get(id=self.kwargs.get('session_id'))
        session_form = SessionForm(request.POST, instance=session)
        if session_form.is_valid():
            photos = self.request.FILES.getlist('photos')
            for photo in photos:
                Photo.objects.create(session=session, image=photo)
            session_form.save()
        return self.render_to_response(self.get_context_data())


class SessionPhotoDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photo = Session.objects.get(id=self.kwargs.get(
            'session_id')).photo_set.get(id=self.kwargs.get('photo_id'))
        photo.delete()
        return redirect('session_edit', session_id=self.kwargs.get('session_id'))


class SessionCreateView(LoginRequiredMixin, FormView):
    template_name = "session.html"
    form_class = SessionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        context['is_create'] = True
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        session = form.save()
        photos = self.request.FILES.getlist('photos')

        for photo in photos:
            Photo.objects.create(session=session, image=photo)

        # Schedule the deletion of the photos
        self._schedule_delete_photos(
            session.id, expiration_date=session.expires_at())

        return redirect('session_edit', session.id)

    def _schedule_delete_photos(self, session_id, expiration_date):
        id = str(session_id)
        delete_photos.apply_async(args=[id], eta=expiration_date)


class SettingsPageView(LoginRequiredMixin, TemplateView):
    template_name = "settings.html"
