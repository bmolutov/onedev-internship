from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser

from orders.models import Order


class OrderSerializer(serializers.Serializer): # noqa
    id = serializers.IntegerField(
        read_only=True
    )
    title = serializers.CharField()
    description = serializers.CharField(
        required=False
    )
    client_id = serializers.IntegerField(
        source='client.id',
        required=False,
    )
    status = serializers.ChoiceField(
        choices=Order.STATUSES
    )

    def create(self, validated_data):
        instance = Order.objects.create(**validated_data) # noqa
        user = self.context['request'].user
        if not isinstance(user, AnonymousUser):
            instance.client = user
            instance.save()
        return instance
