import logging
from django.core.management.base import BaseCommand
from bmw.scrapper import crawler

LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('--name', type=int)
        ...

    def handle(self, *args, **options):
        LOGGER.info('Starting BMW scraper crawler')
        crawler()
