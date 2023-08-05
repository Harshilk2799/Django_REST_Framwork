from rest_framework import serializers
from .models import Singer, Song


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "singer", "duration"]

class SingerSerializers(serializers.ModelSerializer):
    song = SongSerializers(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ["id", "name", "gender", "song"]