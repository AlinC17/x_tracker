from django.contrib import admin
from apps.tracker.models import Device, DeviceModel
from apps.tracker.forms import DeviceForm


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ['model_name']
    search_fields = ['model_name']


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    name = 'Device'
    list_display = ['device_name', 'ip_address', 'model_name_display']
    search_fields = ['device_name', 'ip_address']
    autocomplete_fields = ['device_model', 'author']
    form = DeviceForm

    @staticmethod
    @admin.display(description='Model name')
    def model_name_display(obj: Device):
        return obj.device_model.model_name

    def save_model(self, request, obj, form, change):
        obj.author = request.user if not hasattr(obj, 'author') or not obj.author else obj.author
        return super().save_model(request, obj, form, change)
