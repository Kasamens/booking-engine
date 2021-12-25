from django.urls import path
from .views import ListingApiView

urlpatterns = [
    path('api/v1/units/', ListingApiView.as_view(), name='listings'),
]