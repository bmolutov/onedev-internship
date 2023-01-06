from rest_framework import viewsets, status
from rest_framework.response import Response

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.GenericViewSet):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def get_queryset(self):
        if self.action == 'list':
            if self.request.user.is_authenticated:
                return Order.objects.all() # noqa
            return Order.objects.filter( # noqa
                client=None
            )

    def get_serializer_class(self):
        return OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
