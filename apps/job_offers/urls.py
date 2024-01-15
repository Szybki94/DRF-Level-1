from django.urls import path
from apps.job_offers.views import JobOfferListApiView


urlpatterns = [
   path('job-offers/', JobOfferListApiView.as_view(), name='job-offers')
]
