import re
from datetime import datetime

from django.utils import timezone
from django.utils.timesince import timesince
from rest_framework import serializers

from msg.models import Message


class MessageSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    created_date = serializers.SerializerMethodField(read_only=True)
    updated_date = serializers.SerializerMethodField(read_only=True)
    time_since_creation = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'

    def get_time_since_creation(self, object):
        return timesince(object.created_date, datetime.now(timezone.utc))

    def get_created_date(self, instance):
        return instance.created_date.strftime("%B %d, %Y")

    def get_updated_date(self, instance):
        return instance.updated_date.strftime("%B %d, %Y")

    def get_slug(self, instance):
        return instance.slug

    def validate_msg_text(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('Message text should be less than 100 symbols.')
        return value

    def validate_email(self, value):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, value):
            raise serializers.ValidationError('Invalid email value')
        return value
