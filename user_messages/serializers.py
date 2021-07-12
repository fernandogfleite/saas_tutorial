from django.db.models import fields
from .models import UserMessage
from core.serializers import CompanySafeSerializerMixin
from rest_framework import serializers

class UserMessageSerializer(CompanySafeSerializerMixin,serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMessage
        fields = ['id', 'url', 'from_user', 'to_user', 'text', 'date']
        read_only_fields = ['from_user',]
