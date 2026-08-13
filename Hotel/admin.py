from django.contrib import admin

from .models import Hotel


# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hotel._meta.fields]

