
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import reaper
from dashboard.models import Municipality
from dashboard.models import Locality
from dashboard.models import Species
from dashboard.models import ObjectInfo
from dashboard.models import CategoryType
from dashboard.models import ObjectType
import os
from shutil import copyfile
import datetime



class Command(BaseCommand):

    def get_category_type(self, category_type : str):
        try:
            obj = CategoryType.objects.get(name=category_type)
            return obj
        except:
            return None

    def get_object_type(self, object_type : str):
        try:
            obj = ObjectType.objects.get(name=object_type)
            return obj
        except:
            return None
        
    def get_locality(self, locality : str):
        try:
            obj = Locality.objects.get(name=locality)
            return obj
        except:
            return None
    
    def get_municipality(self, municipality : str):
        print(municipality)
        try:
            
            obj = Municipality.objects.get(name=municipality)
            print(obj.name)
            return obj
            
        except:
            print('none')
            return None
        
        finally:
            print('--------------------------------------')
    

    def get_specie(self, specie : str):
        try:
            obj = Species.objects.get(name=specie)
            return obj
        except:
            return None


    def fill_little_tables(self, xlsx_reaper):
        
        for item in xlsx_reaper.object_types:
            print(item)
            object_type_item = ObjectType()
            object_type_item.name = item
            object_type_item.save()
        
        # Заполняются через import_geo
        #
        #for item in xlsx_reaper.municipalitys:
        #    print(item)
        #    municipality_item = Municipality()
        #    municipality_item.name = item
        #    municipality_item.save()
        
        #for item in xlsx_reaper.localitys:
        #    print(item)
        #    locality_item = Locality()
        #    locality_item.name = item
        #    locality_item.save()


        for item in xlsx_reaper.category_types:
            print(item)
            category_type_item = CategoryType()
            category_type_item.name = item
            category_type_item.save()
        
        
        for item in xlsx_reaper.species:
            print(item)
            species_item = Species()
            species_item.name = item
            species_item.save()


    def fill_big_table(self, xlsx_reaper):
       
        counter = 0
        for row in xlsx_reaper.xlsx_items:
            print(counter)
            object_info_item  = ObjectInfo()
            #print(row['nativeName'],' ',row['date'])
            #print(row)
            object_info_item.id_openData = row['_id']
            object_info_item.nativeName = row['nativeName']
            object_info_item.fullAddress = row['fullAddress']
            object_info_item.coordinates = row['coordinates']
            object_info_item.photo_url = row['photo_url']
            object_info_item.create_date = row['create_date']
            object_info_item.object_type = self.get_object_type(row['object_type'])
            object_info_item.category_type = self.get_category_type(row['category_type'])
            object_info_item.reg_number = row['reg_number']
            object_info_item.con_number = row['con_number']
            object_info_item.documents = row['documents']
            object_info_item.addr_NPA = row['addr_NPA']
            object_info_item.municipality = self.get_municipality(row['municipality'])
            object_info_item.locality = self.get_locality(row['locality'])
            object_info_item.OKN_in_ensemble = row['OKN_in_ensemble']
            object_info_item.information_sign = row['information_sign']
            row['information_sign_photo'] = None
            #object_info_item.information_sign_photo = row['information_sign_photo']
            object_info_item.information_sign_conformity = row['information_sign_conformity']
            object_info_item.photo = None
            #object_info_item.photo = row['photo']
            object_info_item.url = row['url']
            object_info_item.description = row['description']
            object_info_item.affiliation_U = row['affiliation_U']
            object_info_item.esp_valuable_object = row['esp_valuable_object']
            object_info_item.requisites_and_title = row['requisites_and_title']
            object_info_item.owner = row['owner']
            object_info_item.management = row['management']
            object_info_item.owner_contacts = row['owner_contacts']
            object_info_item.has_security_obligation = row['has_security_obligation']
            object_info_item.has_passport_OKN = row['has_passport_OKN']
            object_info_item.actual_address = row['actual_address']
            object_info_item.gen_species_appearance = self.get_specie(row['gen_species_appearance'])
            object_info_item.has_docs_boundaries = row['has_docs_boundaries']
            object_info_item.req_of_approval = row['req_of_approval']
            object_info_item.has_docs_of_aprroval = row['has_docs_of_aprroval']
            object_info_item.document_on_approved_security = row['document_on_approved_security']
            object_info_item.has_rights = row['has_rights']
            if row['date']!='None':
                object_info_item.date = datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
         
            object_info_item.save()
            counter += 1

    # &backup for sqlite            
    def clear_tables(self):
        copyfile('db.sqlite3', 'db.sqlite3_backup')
        # упарвляется из import_geo
        #Municipality.objects.all().delete()
        #Locality.objects.all().delete()
        Species.objects.all().delete()
        CategoryType.objects.all().delete()
        ObjectType.objects.all().delete()
        ObjectInfo.objects.all().delete()
    


    def handle(self, *args, **options):
        
        xlsx_reaper = reaper.XLSX_reaper('file.xlsx')
        self.clear_tables()
        self.fill_little_tables(xlsx_reaper)
        self.fill_big_table(xlsx_reaper)
        
        
        #print(self.get_municipality_id('г. Дерd3бент', Municipality_model))
        #xlsx_reaper = reaper.XLSX_reaper('file.xlsx')
        #self.fill_little_tables(xlsx_reaper)

if __name__ == '__main__':
    pass        








