from rest_framework.views import APIView, Response, status
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users_app import serializers, models,  permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Create and update user profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()

    authentication_classes =  (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    # firter for username or email
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')


class UserLoginApiView(ObtainAuthToken):
    """ create tokens for the users """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES