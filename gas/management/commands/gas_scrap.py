import logging
from django.core.management.base import BaseCommand
from gas.crawlers import GasCrawler


LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        # parser.add_argument('--name', type=int)
        ...

    def handle(self, *args, **options):
        LOGGER.info('Staring Gas crawler')
        GasCrawler.crawl()
