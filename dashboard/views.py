from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets


from .models import ObjectInfo, Municipality, Locality, Species, CategoryType, ObjectType
from .models import Image
from .serializers import ObjectInfoSerializer
from .serializers import MunicipalitySerializer
from .serializers import LocalitySerializer
from .serializers import ObjectTypeSerializer
from .serializers import CategoryTypeSerializer
from .serializers import SpeciesSerializer
from .serializers import ImageSerializer


import json


@csrf_exempt
def feedback(request):
    print(request.POST)
    if request.method == 'POST':
        contactName = request.POST.get('contactName')
        print(contactName)
        for f in request.FILES.getlist('fileFF[]'):
            print(f)
    return HttpResponse("OK")


def contact(request, id):
    context = {'id' : id}
    return render(request, 'dashboard/contact.html', context)

def home(request):
    return redirect(reverse('panel'))

def about(request):
    bread = ['О портале']
    context = {'bread': bread}
    return render(request, 'dashboard/about.html', context)


def panel(request):
    bread = ['Данные']
    return render(request, 'dashboard/panel.html', {'bread': bread})




def more_information_view(request, id):
    data = ObjectInfo.objects.get(id=id)
    print(data.__dict__)
    print('_______')
    for key in data.__dict__:
        print(data.__dict__[key])
        if data.__dict__[key] is 'None':
            print(data.__dict__[key])
            data.__dict__[key] = ''
    #print(data.__dict__)
    context = {'data': data}
    return render(request, 'dashboard/more_information.html', context)



def get_id_data(request):
    id = request.GET.get('id_row')
    row = ObjectInfo.objects.get(id=id)
    data = serializers.serialize("json", [row, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data)




#тестовое ajax заполнение населенных пунктов в зависимости от муниципального образования для фильтра
@csrf_exempt
def search_ajax(request):    
    response = []
    print(request.GET)
    if "search_id" in request.GET:
        search_id = request.GET['search_id']
        print("search_id={}".format(search_id))
    else:
        print('problems')
        return HttpResponse(json.dumps(response))

    localities = Locality.objects.filter(municipality_id=search_id)
    
    real_locality_ids = ObjectInfo.objects.exclude(locality_id=None).values('locality_id')
    ids_set = set(z['locality_id'] for z in real_locality_ids)
    print("Len = {}".format(len(ids_set)))
    
    for item in localities:
        if item.id in ids_set:
            response.append({'id': item.id, 'name': item.name})
    
    return HttpResponse(json.dumps(response))

# FOR NEW REST API CODE


class ObjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ObjectInfo.objects.all()
    serializer_class = ObjectInfoSerializer

class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer

class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer

class ObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ObjectType.objects.all()
    serializer_class = ObjectTypeSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer