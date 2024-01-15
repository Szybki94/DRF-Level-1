from rest_framework import status
from rest_framework.generics import get_object_or_404
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


class JobOfferDetailApiView(APIView):
    def get_object(self, pk):
        query = get_object_or_404(JobOffer, pk=pk)
        return query

    def get(self, request, pk):
        serializer = JobOfferSerializers(self.get_object(pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        job_offer = self.get_object(pk=pk)
        serializer = JobOfferSerializers(job_offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
