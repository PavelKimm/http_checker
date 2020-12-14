from django.urls import path

from analyzer.views import load_websites_to_check, check_websites

urlpatterns = [
    path('load-websites-by-url/', load_websites_to_check, name='address-detail'),
    path('check-websites/', check_websites, name='check-websites'),
]
