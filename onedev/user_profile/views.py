from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from django.core.exceptions import ObjectDoesNotExist

from custom_auth.models import CustomUser
from user_profile.serializers import ProfileSerializer


class ProfileViewSet(viewsets.GenericViewSet): # noqa
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return ProfileSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        try:
            instance = CustomUser.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def edit(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        try:
            instance = CustomUser.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if instance.id != self.request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
