from rest_framework.views import APIView, Response, status
from rest_framework import viewsets

from users_app import serializers, models


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Create and update user profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()