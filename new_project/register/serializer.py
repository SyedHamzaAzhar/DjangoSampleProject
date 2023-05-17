from .model import TODO
from rest_framework import serializers


class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = ['id', 'title', 'subject', 'created_at' ]