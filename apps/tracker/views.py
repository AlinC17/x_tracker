from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.tracker.models import DeviceModel, Device
from apps.tracker.serializers import DeviceModelSerializer, DeviceSerializer, DeviceDetailSerializer
from apps.tracker.services.address import get_autocompleter


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all().order_by('id')
    serializer_class = DeviceModelSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update']:
            return DeviceDetailSerializer
        return super().get_serializer_class()


@api_view(['GET'])
def suggestions(request):
    address_input = request.query_params.get('input')
    if not address_input:
        return Response([])
    autocompleter = get_autocompleter(address_input)
    return Response(autocompleter.data)
