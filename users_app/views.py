from rest_framework.views import APIView, Response, status
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from rest_framework.settings import api_settings
from users_app import serializers, models,  permissions


class UserViewSet(viewsets.ModelViewSet):
    """ Create and update user profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()

    authentication_classes =  (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnUser,)
    # firter for username or email
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')

#login
class UserLoginApiView(ObtainAuthToken):
    """ create tokens for the users """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """ CRUD profile """
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
    # permission_classes = (
    #     permissions.UpdateOwnProfile,
    #     # IsAuthenticated
    # )


    # def perform_create(self, serializer):
    #     """ set user profile for current login user """
    #     serializer.save(user_id = self.request.user)