from django.urls import path

from analyzer.views import load_websites_to_check, check_websites, get_website_info_by_url

urlpatterns = [
    path('load-websites/', load_websites_to_check, name='address-detail'),
    path('check-websites/', check_websites, name='check-websites'),
    path('websites/', get_website_info_by_url, name='get-website-info-by-url'),
]
