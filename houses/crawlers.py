import requests
from time import sleep
from price_parser import Price
from django.conf import settings
from bs4 import BeautifulSoup
from houses.models import HouseOffer
from bmw.utils import get_random_user_agent


class OlxHouseCrawler:
    """
    Crawler that scrapes data of Houses for sale from OLX website.
    """
    URL = settings.HOUSES_URLS['olx']

    @staticmethod
    def get_offers():
        response = requests.get(OlxHouseCrawler.URL, headers={'User-Agent': get_random_user_agent()})
        html_parser = BeautifulSoup(response.content, "html.parser")

        return html_parser.find_all(class_='sc-1fcmfeb-2 fvbmlV')

    @staticmethod
    def get_offer_urls(offers):
        # TODO: This method is already defined as function in bmw.scrappers
        # It is a good practice to move the function to a generic module so
        # it can be shared to be used for multiple internal applications, since
        # its a functiont hat apply for (I guess) all kind of url retrieval from
        # the scraped html from OLX search list.
        urls = []
        for offer in offers:
            html_parser = BeautifulSoup(str(offer), "html.parser")
            try:
                urls.append(html_parser.find("a").attrs['href'])
            except AttributeError:
                continue

        return urls

    @staticmethod
    def get_offer_content(url):
        response = requests.get(url, headers={'User-Agent': get_random_user_agent()})
        html_parser = BeautifulSoup(response.content, "html.parser")

        price = html_parser.find(class_='sc-1wimjbb-1 bQzdqU sc-ifAKCX cmFKIN')
        description = html_parser.find(class_='sc-1sj3nln-1 eOSweo sc-ifAKCX cmFKIN')
        data = html_parser.find_all(class_='duvuxf-0 h3us20-0 jyICCp')
        details = [i.text.lower() for i in data]

        try:
            extracted = {
                'url': url,
                'price': Price.fromstring(price.text.split('$')[1]).amount_float,
                'description': description.text
            }
        except (AttributeError, IndexError):
            print('Failed getting house price on : ', url)
            return {}
        try:
            for detail in details:
                if 'categoria' in detail:
                    extracted['categoria'] = detail.split('categoria')[1].upper()
                elif 'tipo' in detail:
                    extracted['tipo'] = detail.split('tipo')[1]
                elif 'condomínio' in detail:
                    value = detail.split('condomínio')[1]
                    extracted['condomínio'] = Price.fromstring(value).amount_float
                elif 'iptu' in detail:
                    value = detail.split('iptu')[1]
                    extracted['iptu'] = Price.fromstring(value).amount_float
                elif 'área útil' in detail:
                    extracted['área útil'] = detail.split('área útil')[1]
                elif 'quartos' in detail:
                    extracted['quartos'] = int(detail.split('quartos')[1])
                elif 'banheiros' in detail:
                    extracted['banheiros'] = int(detail.split('banheiros')[1])
                elif 'vagas na garagem' in detail:
                    extracted['vagas na garagem'] = int(detail.split('vagas na garagem')[1])
                elif 'cep' in detail:
                    extracted['cep'] = detail.split('cep')[1]
                elif 'município' in detail:
                    extracted['município'] = detail.split('município')[1]
                elif 'bairro' in detail:
                    extracted['bairro'] = detail.split('bairro')[1]
                elif 'logradouro' in detail:
                    extracted['logradouro'] = detail.split('logradouro')[1]
        except:
            print('Failed to extract data from url ', url)
        
        return extracted

    @staticmethod
    def extract_data(urls):
        return [OlxHouseCrawler.get_offer_content(url) for url in urls]

    @staticmethod
    def store_data(data):
        for content in data:
            try:
                offer, _ = HouseOffer.objects.get_or_create(
                    url=content.get('url'),
                    price=content.get('price'),
                    description=content.get('description'),
                    category=content.get('categoria'),
                    type=content.get('tipo'),
                    condominium=content.get('condomínio'),
                    property_tax=content.get('iptu'),
                    useful_area=content.get('área útil'),
                    bedrooms=content.get('quartos'),
                    bathrooms=content.get('banheiros'),
                    parking_spaces=content.get('vagas na garagem'),
                    postal_code=content.get('cep'),
                    county=content.get('município'),
                    district=content.get('bairro'),
                    address=content.get('logradouro')
                )
                offer.save()
            except Exception as e:
                print(f'Failed saving offer content: {content} with error: {str(e)}')
                continue

        return HouseOffer.objects.all().count()

    @staticmethod
    def crawl():
        while True:
            offers = OlxHouseCrawler.get_offers()
            urls = OlxHouseCrawler.get_offer_urls(offers)
            data = OlxHouseCrawler.extract_data(urls)
            count = OlxHouseCrawler.store_data(data)
            print(f'Collected {len(data)} house offers')
            print(f'Total houses on database: {count}')
            sleep(3600*2)
