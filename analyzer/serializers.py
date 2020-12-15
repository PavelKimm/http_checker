from rest_framework import serializers

from analyzer.models import Website, WebsiteAvailability


class WebsiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('id', 'url')


class WebsiteAvailabilityDetailSerializer(serializers.ModelSerializer):
    website = WebsiteDetailSerializer()

    class Meta:
        model = WebsiteAvailability
        fields = ('id', 'website', 'response_status_code', 'reason', 'ip_address', 'server', 'checked_at')
