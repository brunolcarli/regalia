"""
Module for insertion of more scrappers to extend or enhance the API.
"""
import requests
from bs4 import BeautifulSoup
from gas.models import GasPrice
from django.conf import settings


class GasCrawler:

    URL=settings.GASPASS_TARGET_URL

    @staticmethod
    def get_price():
        response = requests.get(GasCrawler.URL)
        html_parser = BeautifulSoup(response.content, 'html.parser')
        html = html_parser.find_all(class_='gasolina d-flex flex-column')
        span_parser = BeautifulSoup(str(html), 'html.parser')
        spans = span_parser.find_all(class_='price')
        price = float(spans[0].text.split('R$')[1].strip())

        return price

    @staticmethod
    def store_data(price, gas_station):
        gas_record = GasPrice.objects.create(
            gas_station_name=gas_station,
            gas_price=price
        )
        gas_record.save()

        return GasPrice.objects.all().count()
