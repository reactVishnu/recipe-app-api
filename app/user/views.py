from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer, AuthTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES
