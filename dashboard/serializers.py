from rest_framework import serializers
from .models import ObjectInfo
from .models import ObjectType
from .models import CategoryType
from .models import Municipality
from .models import Locality
from .models import Species
from .models import Image
from django import db
   


class LocalitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Locality
        fields = (
            'id',
            'name',
            'municipality',
        )


class MunicipalitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Municipality
        fields = (
            'id',
            'name',
        )




class ObjectTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ObjectType
        fields = (
            'id',
            'name',
        )

class SpeciesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Species
        fields = (
            'id',
            'name',
        )


class CategoryTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CategoryType
        fields = (
            'id',
            'name',
        )

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'image',
        )
        

class ObjectInfoSerializer(serializers.ModelSerializer):


    print("clear objectinfo memory")    
    db.reset_queries()


    object_type = ObjectTypeSerializer()
    category_type = CategoryTypeSerializer()
    municipality = MunicipalitySerializer()
    locality = LocalitySerializer()
    gen_species_appearance = SpeciesSerializer()
    images = serializers.StringRelatedField(many=True)

    class Meta:
       
        model = ObjectInfo
        fields = (
            'id',
            'nativeName',
            'municipality',
            'locality',
            'fullAddress',
            'create_date',
            'object_type',
            'category_type',
            'photo',
            'description',
            'affiliation_U',
            'esp_valuable_object',
            'requisites_and_title',
            'gen_species_appearance',
            'reg_number',
            'documents',
            'images',
        )

