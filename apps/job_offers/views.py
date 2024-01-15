from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.job_offers.models import JobOffer
from apps.job_offers.serializers import JobOfferSerializers


class JobOfferListApiView(APIView):

    def get(self, request):
        query = JobOffer.objects.all()
        serializer = JobOfferSerializers(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
