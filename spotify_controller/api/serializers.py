from rest_framework import serializers
from .models import Room


# A serializer is a way to convert data into a format that can be easily stored or transferred.
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "id",
            "code",
            "host",
            "guest_can_pause",
            "votes_to_skip",
            "created_at",
        )
