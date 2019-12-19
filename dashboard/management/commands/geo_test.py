from dashboard.models import Locality
from dashboard.models import Municipality
from dashboard.models import ObjectInfo


from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import re


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        empty_locality_objects = ObjectInfo.objects.exclude(fullAddress='').filter(locality=None)
        print(len(empty_locality_objects))
        for o in empty_locality_objects:
            #print("{} {}".format(o.fullAddress, self.__extract_locality(o)))
            self.__extract_locality(o)



    def __extract_locality(self, objectinfo : ObjectInfo):
        locality_string = ''
        full_address = objectinfo.fullAddress
        if full_address == 'None':
            return ''
        #locality_l =  re.findall(r'с\.?([А-Я][а-я]+)', full_address)
        #print(locality_l)
        
        locality_l =  re.findall(r'с\.[ ]?([А-Я][а-я]+)[, ]', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'село[ ]?([А-Яа-я- .,]+)$', full_address)
        if len(locality_l) == 0:
            locality_l =  re.findall(r'селение[ ]?([А-Яа-я- .,]+)$', full_address)
        if len(locality_l) == 0:    
            locality_l =  re.findall(r'с\.?([А-Я][а-я]+)', full_address)
        
        
        #print(locality_l)
        
        if len(locality_l)==0:
            return None
        else:
            locality = Locality.objects.filter(name=locality_l[0]).first()
            print(locality)
            return locality
        


        




