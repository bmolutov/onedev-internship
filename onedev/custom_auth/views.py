from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from custom_auth.models import CustomUser
from custom_auth.serializers import RegisterSerializer


class RegisterViewSet(viewsets.GenericViewSet):
    def get_queryset(self):
        return CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'register':
            return RegisterSerializer

    def get_permission_class(self):
        if self.action == 'register':
            return permissions.AllowAny

    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
