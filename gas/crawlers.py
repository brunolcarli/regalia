"""
Module for insertion of more scrappers to extend or enhance the API.
"""
from datetime import datetime
from time import sleep
import requests
from django.conf import settings
from bs4 import BeautifulSoup
from gas.models import GasPrice
from gas.enums import CityRegions


class GasCrawler:
    """
    Crawler for collection gas prices from gas stations.
    The scrapping structure may change if the target website URL is changed.
    """
    @staticmethod
    def get_price(endpoint):
        response = requests.get(f'{settings.GASPASS_TARGET_URL}{endpoint}')
        soup = BeautifulSoup(response.content, 'html.parser')
        spans = soup.find_all('span')
        labels = [tag.text for tag in spans if len(tag.text) > 3]
        labels = labels[1:]

        # split labels
        split_range = 7
        gasoline_data = labels[:split_range]
        ethanol_data = labels[split_range:split_range*2]
        # diesel_data = labels[split_range*2:split_range*3]

        data = {
            'gasoline_mean_price': float(gasoline_data[2].split('R$')[1].strip()),
            'gasoline_lowest_price': float(gasoline_data[4].split('R$')[1].strip()),
            'gasoline_highest_price': float(gasoline_data[6].split('R$')[1].strip()),
            'ethanol_mean_price': float(ethanol_data[2].split('R$')[1].strip()),
            'ethanol_lowest_price': float(ethanol_data[4].split('R$')[1].strip()),
            'ethanol_highest_price': float(ethanol_data[6].split('R$')[1].strip()),            
        }

        return data

    @staticmethod
    def store_data(data, region):
        gas_record, created = GasPrice.objects.get_or_create(
            region=region,
            datetime_reference=datetime.now().date()
        )

        if created:
            gas_record.gas_price = data.get('gasoline_mean_price')
            gas_record.gas_lower_price = data.get('gasoline_lowest_price')
            gas_record.gas_higher_price = data.get('gasoline_highest_price')
            gas_record.ethanol_price = data.get('ethanol_mean_price')
            gas_record.ethanol_lower_price = data.get('ethanol_lowest_price')
            gas_record.ethanol_higher_price = data.get('ethanol_highest_price')
            gas_record.save()

        return GasPrice.objects.all().count()

    @staticmethod
    def crawl():
        while True:
            # scrap data for Pinhais City region
            data = GasCrawler.get_price(CityRegions.PINHAIS.value)
            GasCrawler.store_data(data, CityRegions.PINHAIS.name.title())

            # scrape data for CWB region
            data = GasCrawler.get_price(CityRegions.CURITIBA.value)
            GasCrawler.store_data(data, CityRegions.CURITIBA.name.title())

            sleep(25200)
