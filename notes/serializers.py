from rest_framework import serializers
from .models import Note
from django.utils.text import slugify
import pytz


'''Custom serializer for date and time fields'''


class DateTimeFieldWithTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = value.astimezone(pytz.timezone("UTC"))
        return {
            "date": value.date().strftime("%d/%m/%Y"),
            "time": value.time().isoformat("minutes"),
        }


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    createdAt = DateTimeFieldWithTZ(source="created_at")
    lastModified = DateTimeFieldWithTZ(source="last_modified")

    class Meta:
        model = Note
        fields = ("id", "user", "title", "description", "createdAt", "lastModified", "slug")

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)
