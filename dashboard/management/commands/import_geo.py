import json
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from dashboard.models import Municipality
from dashboard.models import Locality



class Command(BaseCommand):
    """
        заполняем связанные таблицы геоданных
    """
    def __clear_tables(self):
        Locality.objects.all().delete()
        Municipality.objects.all().delete()
        

    def handle(self, *args, **options):
        answer = input('При импорте геоданных информация таблица с информацией об объектах будет очищена. Продолжить (yes/no) : ')
        if answer == 'yes':
            self.__clear_tables()
            filename = 'geo.json'
            json_data = open(filename, encoding='utf-8').read()
            data = json.loads(json_data)
            for muninicipality_name in data.keys():
                print(muninicipality_name)
                m = Municipality(name=muninicipality_name)
                m.save()
                for locality_name in data[muninicipality_name]:
                    l = Locality(name=locality_name, municipality=m)
                    l.save()
                    print('locality={}'.format(locality_name))
        else:
            print('Операция отменена')
            return
