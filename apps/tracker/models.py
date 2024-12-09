from django.db import models
from django.contrib.auth import get_user_model


class DeviceModel(models.Model):
    model_name = models.CharField(max_length=150)
    model_description = models.TextField()

    def __str__(self):
        return self.model_name


class Device(models.Model):
    address = models.CharField(max_length=255)
    device_name = models.CharField(max_length=150)
    ip_address = models.GenericIPAddressField()
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='devices')
    device_model = models.ForeignKey(DeviceModel, on_delete=models.PROTECT, related_name='devices')
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.device_name
