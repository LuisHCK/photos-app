from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardPageView.as_view(), name="dashboard"),
    path('edit/<int:session_id>/',
         views.SessionPageView.as_view(), name="session_edit"),
    path('edit/<int:session_id>/photos/<int:photo_id>/delete/',
         views.SessionPhotoDeleteView.as_view(), name="session_photo_delete"),
    path('create/', views.SessionCreateView.as_view(), name="session_create"),
    path('settings/', views.SettingsPageView.as_view(), name="settings"),
]
