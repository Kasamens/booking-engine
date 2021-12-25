from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):

    price = serializers.CharField(source = 'booking_info.price')

    
    class Meta:
        model = Listing
        fields = ('listing_type', 'title', 'country', 'city', 'price')