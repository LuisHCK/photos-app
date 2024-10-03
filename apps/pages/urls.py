from django.urls import path
from .views import HomepageView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*0)(HomepageView.as_view()), name='homepage'),
]
