from django.core.management.base import BaseCommand, CommandError

import importlib
from ._parsers import *


class Command(BaseCommand):
    help = 'Загрузить данные из источника в базу данных'
    sources = {
        'fgos': 'FgosTrainingDirectionParser'
    }

    def add_arguments(self, parser):
        parser.add_argument('source', nargs='+', type=str, )

    def handle(self, *args, **options):
        source = options['source'][0]
        try:
            parser_name = self.sources[source]
            parser = globals().get(parser_name)()
            result = parser.parse()
            for message in result:
                self.stdout.write(self.style.SUCCESS(message))
        except KeyError as e:
            self.stdout.write(self.style.ERROR('Unknown source'))
