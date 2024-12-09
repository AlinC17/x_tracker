from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False)

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise exceptions.ValidationError({"detail": "Invalid credentials"})
        self.instance = user
        return data

    @property
    def data(self):
        _ = super().data
        token, __ = Token.objects.get_or_create(user=self.instance)
        return {
            "token": token.key
        }
