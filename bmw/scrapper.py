"""
This module contains the main scrapper for the BMW 320i data from OLX.
"""
from datetime import datetime
import requests
import sys
from time import sleep
from bs4 import BeautifulSoup
from bmw.utils import get_random_user_agent
from bmw.models import BMWOffer
from django.conf import settings


URL=settings.OLX_TARGET_URL


def get_offers(url):
    response = requests.get(url, headers={'User-Agent': get_random_user_agent()})
    html_parser = BeautifulSoup(response.content, "html.parser")

    return html_parser.find_all(class_='sc-1fcmfeb-2 fvbmlV')


def get_offer_urls(offers):
    urls = []
    for offer in offers:
        html_parser = BeautifulSoup(str(offer), "html.parser")
        try:
            urls.append(html_parser.find("a").attrs['href'])
        except AttributeError:
            continue

    return urls


def get_offer_content(url):
    response = requests.get(url, headers={'User-Agent': get_random_user_agent()})
    html_parser = BeautifulSoup(response.content, "html.parser")

    data = html_parser.find_all(class_='sc-hmzhuo eNZSNe sc-jTzLTM iwtnNi')
    price = html_parser.find(class_='sc-1leoitd-0 cIfjkh sc-ifAKCX cmFKIN')
    details = [i.text.lower() for i in data]

    extracted = {
        'url': url,
        'price': float(price.text.split('$')[1])
    }

    for detail in details:
        if 'modelo' in detail:
            extracted['model'] = detail.split('modelo')[1].upper()
        elif 'ano' in detail:
            extracted['year'] = int(detail.split('ano')[1])
        elif 'quilometragem' in detail:
            extracted['km'] = int(detail.split('quilometragem')[1])
        elif 'motor' in detail:
            extracted['power'] = detail.split('motor')[1]
        elif 'cor' in detail:
            extracted['color'] = detail.split('cor')[1]
    
    return extracted


def extract_data(urls):
    return [get_offer_content(url) for url in urls]


def retrieve_data():
    raise Exception('NOT IMPLEMENTED :(')


def store_data(data):
    # previous = retrieve_data()
    for content in data:
        try:
            offer, _ = BMWOffer.objects.get_or_create(
                url=content.get('url'),
                price=content.get('price'),
                car_model=content.get('model'),
                car_year=content.get('year'),
                km=content.get('km'),
                color=content.get('color'),
                seller_name=content.get('seller_name'),
                power=content.get('power')
            )
            offer.save()
        except Exception as e:
            offer = None
            continue

    return BMWOffer.objects.all().count()


def crawler():
    while True:
        sys.stdout.write(f'Crawling {URL} | {str(datetime.now())}\n')
        offers = get_offers(URL)
        urls = get_offer_urls(offers)
        data = extract_data(urls)
        count = store_data(data)
        sys.stdout.write(f'Total objects count {count} | {str(datetime.now())}\n')
        sleep(3600*2)
