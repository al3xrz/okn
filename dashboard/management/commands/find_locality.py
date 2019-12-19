import re

from dashboard.models import ObjectInfo
from dashboard.models import Locality
from dashboard.models import Municipality
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):

    def handle(self, *args, **options):
        objects = ObjectInfo.objects.all()
        counter = 0
        for o in objects:
            locality = self.__extract_locality(o)
            if locality is not None and not isinstance(locality, str):
                counter+=1
                o.locality = locality
                o.save()
                print('{} {} [{}]'.format(counter,o,locality))
                
        print("Total : {}".format(counter))
        
    
    def __extract_locality(self, objectinfo : ObjectInfo):
        locality_string = ''
        full_address = objectinfo.fullAddress
        if full_address == 'None':
            return ''
        
        locality_l =  re.findall(r'с\.[ ]?([А-Яа-я- .]+)[,]', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'с\.[ ]?([А-Яа-я- .]+)$', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'село[ ]?([А-Яа-я- .]+)$', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'селение[ ]?([А-Яа-я- .]+)$', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'с\.[ ]?([А-Я][а-я]+)[, ]', full_address)
       

        '''
        locality_l =  re.findall(r'с\.[ ]?([А-Я][а-я]+)[, ]', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'село[ ]?([А-Яа-я- .,]+)$', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'селение[ ]?([А-Яа-я- .,]+)$', full_address)
        if len(locality_l) == 0:    
            locality_l =  re.findall(r'с\.?([А-Я][а-я]+)', full_address)
        '''


        if len(locality_l)==0:
            return None
        else:
            locality = Locality.objects.filter(name=locality_l[0]).first()
            return locality
           



    
