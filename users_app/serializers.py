from rest_framework import serializers

from users_app import models

class UserProfileSerializer(serializers.ModelSerializer):
    """ serialize the user profile object """

    class Meta:
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'is_active', 'is_staff', 'last_login', 'created_at')
        extra_kwargs = {
            'password': {
                'write_only': True, # it only shows the password when we create the user object
                'style': {'input_type': 'password'}, # protect the password when writing to an input
            }
        }

    def create(self, validate_data):
        """ create and return new user """
        user = models.User.objects.create_user(
            email = validate_data['email'],
            username = validate_data['username'],
            password = validate_data['password']
        )

        return user
    
    def update(self, instance, validate_data):
        """ update a user account """
        if 'password' in validate_data:
            password = validate_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validate_data)
