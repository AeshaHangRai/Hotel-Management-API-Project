from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Hotel
from .serializers import HotelSerializer


# ModelViewSet provides all the CRUD functionality

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    # Additional functionality:
    # GET /api/hotels/city/?city=Kathmandu
    @action(detail=False, methods=["get"])
    def city(self, request):

        city_name = request.query_params.get("city")

        if city_name:
            hotels = Hotel.objects.filter(city__iexact=city_name)
        else:
            hotels = Hotel.objects.all()

        serializer = HotelSerializer(hotels, many=True)

        return Response(serializer.data)
