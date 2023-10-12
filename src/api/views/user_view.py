from django.contrib.auth.models import User
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers.user_serializer import CreateUserSerializer

from ..serializers.user_serializer import (
    ChangePasswordUserSerializer,
    UpdateUserSerializer,
)


class UserViewSet(RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UpdateUserView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()


class ChangePasswordUserView(UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordUserSerializer
