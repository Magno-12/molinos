from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid email or password')
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
        }
    

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    change_password = serializers.BooleanField(read_only=True)
    data = serializers.DictField(child=serializers.CharField())
    user = serializers.SerializerMethodField()

    class Meta:
        fields = ['refresh', 'access', 'change_password', 'data', 'user']

    def get_user(self, obj):
        user = User.objects.get(username=obj['username'])
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': 'admin'  # This should be replaced by actual role data
        }


class LogoutResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(read_only=True)
