from app.models import TrainingDirectionGroup, TrainingDirection
from django.core.exceptions import ObjectDoesNotExist

from lxml.html import fromstring
from lxml import *
import requests


class Parser:
    def parse(self):
        pass


class FgosTrainingDirectionParser(Parser):
    base_url = 'http://www.edu.ru/'

    direction_count = 0
    group_count = 0

    def __parse_direction(self, direction):
        request = requests.get(direction.url)

        dom = fromstring(request.text)
        table = dom.xpath('//table')[3]
        for row in table:
            for cell in row:
                if cell.get('class') == 'tdcont':
                    p_counter = 0
                    h1_counter = 0
                    for item in cell:
                        if item.tag == 'h1':
                            h1_counter += 1
                            if h1_counter == 3:
                                t = item.text.split('(')[1].replace(')', '')
                                if t.startswith('маг'):
                                    return None
                        if item.tag == 'p':
                            p_counter += 1
                            if item.text_content() != '':
                                direction.description = item.text_content()
                                break

        direction.code = direction.url.split('fgos.')[1].split('/st.')[0]
        self.direction_count += 1

        return direction

    def __parse_group(self, relative_url, group):
        request = requests.get(self.base_url + relative_url)

        dom = fromstring(request.text)
        table = dom.xpath('//table')[4]

        direction_array = []
        for row in table:
            for cell in row:
                if cell.get('width') != '15':
                    for item in cell:
                        if item.tag == 'a':
                            try:
                                direction = TrainingDirection.objects.get(
                                    name=item.text
                                )
                            except ObjectDoesNotExist:
                                direction = TrainingDirection(
                                    name=item.text
                                )
                                direction.url = self.base_url + item.get('href')
                                direction.group = group
                                direction = self.__parse_direction(direction)
                            if direction:
                                direction.save()
                                direction_array.append(direction)

        return direction_array

    def parse(self):
        request = requests.get(self.base_url + '/abitur/act.6/index.php')

        dom = fromstring(request.text)
        table = dom.xpath('//table')[4]

        group_array = []
        direction_array = []
        for row in table:
            for cell in row:
                for link in cell:
                    try:
                        group = TrainingDirectionGroup.objects.get(
                            name=link.text
                        )
                    except ObjectDoesNotExist:
                        group = TrainingDirectionGroup(
                            name=link.text
                        )
                        self.group_count += 1
                    group.save()
                    direction_array += self.__parse_group(link.get('href'), group)
                    group_array.append(group)

        result = [
            'New Training Direction Groups: ' + str(self.group_count),
            'New Training Directions: ' + str(self.direction_count),
        ]

        return result
