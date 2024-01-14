from rest_framework import serializers
from apps.job_offers.models import JobOffer


class JobOfferSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = JobOffer
        fields = "__all__"
