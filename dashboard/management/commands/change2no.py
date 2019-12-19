from dashboard.models import ObjectInfo
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps


class Command(BaseCommand):

    def handle(self, *args, **options):
        objects = ObjectInfo.objects.all()
        YES = 'Да'
        NO = 'Нет'
        IN_WORK = 'На подготовке'
        information_CHOICES = (
            (YES, 'Да'),
            (NO, 'Нет'), 
            (IN_WORK, 'На подготовке')
        )
        like_BOOLEAN = (
            (YES, 'Да'),
            (NO,  'Нет'),
        )
        
        objects.update(
            OKN_in_ensemble='Нет',
            information_sign='Нет',
            information_sign_conformity='Нет',
            affiliation_U='Нет',
            esp_valuable_object='Нет',
            has_security_obligation='Нет',
            has_passport_OKN='Нет',
            has_docs_boundaries='Нет',
            has_docs_of_aprroval='Нет',
            has_rights='Нет',
        )
        counter = 0
        for ob in objects:
            counter+=1
            print("{}. {} {}" .format(counter, ob.nativeName, ob.OKN_in_ensemble))
            ob.save()
                
