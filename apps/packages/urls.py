from django.urls import path
from .views import PackageListView, \
    PackageCreateView, \
    PackageEditView, \
    TierCreateView, \
    TierUpdateView, \
    TiersListView, \
    TierDeleteView

urlpatterns = [
    path('', PackageListView.as_view(), name='list_packages'),
    path('create/', PackageCreateView.as_view(), name='create_package'),
    path('<int:pk>/edit/', PackageEditView.as_view(), name='edit_package'),
    path('<int:pk>/tiers/', TiersListView.as_view(), name='list_tiers'),
    path('<int:pk>/tiers/create/', TierCreateView.as_view(), name='create_tier'),
    path('<int:package_pk>/tiers/<int:pk>/edit/',
         TierUpdateView.as_view(), name='edit_tier'),
    path('<int:package_pk>/tiers/<int:pk>/delete/',
         TierDeleteView.as_view(), name='delete_tier'),
]
