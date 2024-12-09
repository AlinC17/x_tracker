from rest_framework import serializers

from apps.authorization.serializers import UserSerializer
from apps.tracker.models import Device, DeviceModel


class DeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceDetailSerializer(DeviceSerializer):
    device_model = DeviceModelSerializer(read_only=True)
    device_model_id = serializers.PrimaryKeyRelatedField(
        queryset=DeviceModel.objects.all(),
        required=True,
        allow_null=False,
        allow_empty=False,
        write_only=True
    )
    author = UserSerializer(read_only=True)

    def create(self, validated_data):
        request = self.context['request']
        validated_data['author'] = request.user
        return super().create(validated_data)

    class Meta(DeviceSerializer.Meta):
        pass
