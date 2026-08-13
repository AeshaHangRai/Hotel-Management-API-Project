from rest_framework import serializers

from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = "__all__"

    # Custom error messages
    extra_kwargs = {
        "name": {
            "error_messages": {
                "required": "Hotel name is required.",
                "blank": "Hotel name cannot be empty.",
            }
        },
        "city": {
            "error_messages": {
                "required": "City is required.",
                "blank": "City cannot be empty.",
            }
        },
        "country": {
            "error_messages": {
                "required": "Country is required.",
                "blank": "Country cannot be empty.",
            }
        },
    }

    # Field-level validation
    def validate_star_rating(self, value):

        if value < 0:
            raise serializers.ValidationError(
                "Star rating cannot be negative."
            )

        if value > 5:
            raise serializers.ValidationError(
                "Star rating cannot be greater than 5."
            )

        return value