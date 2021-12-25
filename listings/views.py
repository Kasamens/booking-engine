from django.shortcuts import render
from rest_framework import generics
from .models import Listing,BlockedListing,BookingInfo
from .serializers import ListingSerializer

class ListingApiView(generics.ListAPIView):

    serializer_class = ListingSerializer
    
    def get_queryset(self, **kwargs):

        listings = Listing.objects.all()
        #listings = Listing.objects.filter(price__lt=100)

        # max_price = kwargs['max_price']
        # check_in = self.kwargs['check_in']
        # check_out = self.kwargs['check_out']

        # listings = Listing.objects.filter(
        #     price__lt = max_price
        # )

        return listings