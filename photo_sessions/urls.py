from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.SessionDetailView.as_view(), name="public_session_details"),
]
