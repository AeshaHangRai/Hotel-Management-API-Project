from django.db import models

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    hotel = models.ForeignKey(
        'Hotel.Hotel',
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPE_CHOICES
    )
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('hotel', 'room_number')
        ordering = ['room_number']

    def __str__(self):
        return f"Room {self.room_number}"