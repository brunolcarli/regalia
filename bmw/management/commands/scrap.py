"""
Comando para publicação de instalações par ao broker MQTT.
"""
import logging
from threading import Thread
from django.core.management.base import BaseCommand
from bmw.scrapper import crawler


LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('--name', type=int)
        ...

    def handle(self, *args, **options):
        # process = Thread(target=crawler)
        # process.start()
        crawler()
        # LOGGER.info('Started process %s', str(process))
