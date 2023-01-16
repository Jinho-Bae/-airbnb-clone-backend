from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "price",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "rooms",
        "price",
        "toilets",
        "pet_friendly",
        "created_at",
        "updated_at",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
