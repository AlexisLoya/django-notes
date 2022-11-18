from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id', 'title', 'description',
                  'owner', 'created_at', 'updated_at')
        read_only_fields = ('owner', 'created_at', 'id')
