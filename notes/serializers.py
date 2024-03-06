from rest_framework import serializers
from .models import Note
from django.utils.text import slugify

class NoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
    read_only=True,
    )
    class Meta:
        model = Note
        fields = "__all__"
        def create(self, validated_data):
            validated_data['slug'] = slugify(validated_data['title'])
            return super().create(validated_data)
        
