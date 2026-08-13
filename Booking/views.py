from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users only see their own bookings
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status='pending')

    @action(detail=True, methods=['post'], url_path='confirm')
    def confirm(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'confirmed'
        booking.save()
        return Response(BookingSerializer(booking).data)

    @action(detail=True, methods=['post'], url_path='cancel')
    def cancel(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'cancelled'
        booking.save()
        return Response(BookingSerializer(booking).data)