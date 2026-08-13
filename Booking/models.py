from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from Room.models import Room

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.check_in_date >= self.check_out_date:
            raise ValidationError("check_out_date must be after check_in_date")

        overlapping = Booking.objects.filter(
            room=self.room,
            status__in=['pending', 'confirmed'],
            check_in_date__lt=self.check_out_date,
            check_out_date__gt=self.check_in_date,
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("Room is already booked for these dates")

    def save(self, *args, **kwargs):
        nights = (self.check_out_date - self.check_in_date).days
        self.total_price = nights * self.room.price_per_night
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking #{self.id} - {self.room.room_number} ({self.status})"