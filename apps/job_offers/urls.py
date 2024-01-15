from django.urls import path
from apps.job_offers.views import JobOfferListApiView, JobOfferDetailApiView


urlpatterns = [
   path('job-offers/', JobOfferListApiView.as_view(), name='job-offers'),
   path('job-offers/<int:pk>', JobOfferDetailApiView.as_view(), name='job-offers-detail')
]
