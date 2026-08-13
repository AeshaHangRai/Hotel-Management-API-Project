from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'room', 'check_in_date', 'check_out_date',
            'status', 'total_price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'total_price', 'created_at', 'updated_at']

    def validate(self, data):
        instance = self.instance
        room = data.get('room', instance.room if instance else None)
        check_in = data.get('check_in_date', instance.check_in_date if instance else None)
        check_out = data.get('check_out_date', instance.check_out_date if instance else None)

        if check_in and check_out and check_in >= check_out:
            raise serializers.ValidationError("check_out_date must be after check_in_date")

        overlapping = Booking.objects.filter(
            room=room,
            status__in=['pending', 'confirmed'],
            check_in_date__lt=check_out,
            check_out_date__gt=check_in,
        )
        if instance:
            overlapping = overlapping.exclude(pk=instance.pk)

        if overlapping.exists():
            raise serializers.ValidationError("Room is already booked for these dates")

        return data