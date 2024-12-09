from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth import get_user_model
from apps.tracker.models import Device


class AddressAutoCompleteInput(TextInput):
    template_name = 'tracker/input.html'

class AddressAutoCompleteField(forms.CharField):
    widget = AddressAutoCompleteInput


class DeviceForm(forms.ModelForm):
    address = AddressAutoCompleteField()
    author = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False)

    class Meta:
        model = Device
        fields = '__all__'
