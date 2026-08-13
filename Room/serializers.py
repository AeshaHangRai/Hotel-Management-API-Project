from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id', 'hotel', 'room_number', 'room_type',
            'price_per_night', 'capacity', 'is_available',
            'image_url', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']