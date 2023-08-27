from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = UserSerializer
    queryset = User.objects.all()
