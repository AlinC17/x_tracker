import requests
from django.conf import settings
from dataclasses import dataclass
from abc import ABC, abstractmethod
from dadata import Dadata


@dataclass
class Autocompleter(ABC):
    input_address: str

    @property
    @abstractmethod
    def data(self):
        raise NotImplementedError()


class APIAutocompleter(Autocompleter):
    API_URL = 'http://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'
    HEADERS = {
        'Authorization': f"Token {settings.DADATA_API_KEY}",
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    @property
    def data(self):
        response = requests.post(self.API_URL, json={"query": self.input_address}, headers=self.HEADERS)
        if not response.ok:
            return []
        return response.json()['suggestions']


class LibAutocompleter(Autocompleter):

    @property
    def data(self):
        return Dadata(settings.DADATA_API_KEY).suggest('address', self.input_address)


def get_autocompleter(input_text):
    if settings.USE_LIB:
        return LibAutocompleter(input_text)
    return APIAutocompleter(input_text)
