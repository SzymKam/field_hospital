from rest_framework import serializers

from patients.models import AuthorizedPerson


class AuthorizedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedPerson
        fields = "__all__"
