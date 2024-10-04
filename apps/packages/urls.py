from django.urls import path
from .views import PackageListView, PackageCreateView, PackageEditView

urlpatterns = [
    path('', PackageListView.as_view(), name='list_packages'),
    path('create/', PackageCreateView.as_view(), name='create_package'),
    path('<int:pk>/edit/', PackageEditView.as_view(), name='edit_package'),
]
