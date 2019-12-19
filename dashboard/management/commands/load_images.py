from dashboard.models import ObjectInfo
from dashboard.models import Image
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import urllib
from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile
from django.core.files import File


class Command(BaseCommand):

    def handle(self, *args, **options):
        #normalize slugs

        for o in ObjectInfo.objects.all():
            if len(o.slug)>80:
                print("{} -> {}".format(o.slug, o.slug[:80]))
                o.slug = o.slug[:80]
                o.save()
        
        for o in ObjectInfo.objects.all():
            if o.photo_url != '' and o.photo_url != 'None' and o.photo_url != None:
                print('ID={}'.format(o.id))
                print(o.photo_url)

                response = requests.get(o.photo_url)
                with open(r"tmp/{}.jpg".format(str(o.id)), 'wb') as f:
                    f.write(response.content)
                
                reopen = open(r"tmp/{}.jpg".format(str(o.id)), 'rb')
                django_file = File(reopen)

                
                
                image = Image()
                image.objectinfo = o
                image.image.save(r"tmp/{}.jpg".format(str(o.id)), django_file, save=True)
                reopen.close()
                
