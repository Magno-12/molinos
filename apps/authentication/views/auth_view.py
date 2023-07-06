from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import NotAuthenticated

from apps.authentication.serializers.auth_serializer import (
    LoginSerializer, 
    LogoutSerializer, 
    LoginResponseSerializer, 
    LogoutResponseSerializer
  )
from apps.users.models.user import User

class AuthViewSet(GenericViewSet):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        if self.action == 'logout':
            return LogoutSerializer
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """
        Logs in an existing user using their email and password.

        Takes email and password as input.

        If the provided email and password are correct, 
        returns a new refresh and access token for the user. 
        The refresh token can be used to generate new access tokens.

        ---
        # YAML (must be separated by `---`)

        type:
          email:
            required: true
            type: string
          password:
            required: true
            type: string

        responses:
          200:
            description: Successful login
            examples:
              {
                  "refresh": "refresh_token",
                  "access": "access_token",
                  "user": {
                      "id": "user_id",
                      "username": "username",
                      "email": "email",
                      "role": "role"
                  }
              }
          400:
            description: Invalid email or password
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data

        user = User.objects.get(id=user_data['id'])

        refresh = RefreshToken.for_user(user)  # Pass the User object, not the UUID
        
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user_data,
        }
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        """
        Logs out an authenticated user.

        Takes a refresh token as input.

        If the refresh token is valid, invalidates it so it cannot be used 
        again. Any associated access tokens are also invalidated.

        ---
        # YAML (must be separated by `---`)

        type:
          refresh:
            required: true
            type: string

        responses:
          204:
            description: Successful logout
          400:
            description: Invalid refresh token
        """
        if request.user.is_anonymous:
          raise NotAuthenticated("No active session")
    
        # If using token authentication
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # If using JWT authentication
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                refresh_token = serializer.data['refresh_token']
                token = RefreshToken(refresh_token)
                token.blacklist()
            except TokenError:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(status=status.HTTP_200_OK)
