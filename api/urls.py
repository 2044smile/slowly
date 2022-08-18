from django.urls import path

from api.views import crawling_university, crawling_country

urlpatterns = [
    path('cwl_country/', crawling_country),
    path('cwl_university/', crawling_university),
]
