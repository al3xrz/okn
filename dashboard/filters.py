import django_filters
from django_filters import filters
from .models import  ObjectInfo
from .models import Municipality

class ObjectInfoFilter(django_filters.FilterSet):

    
    

    class Meta:
        model = ObjectInfo
        fields = ('municipality', 'locality', 'object_type', 'category_type')

    def __init__(self, *args, **kwargs):
        super(ObjectInfoFilter, self).__init__(*args, **kwargs)
        self.filters['municipality'].extra.update({'empty_label': 'Все муниципальные образования'})
        self.filters['locality'].extra.update({'empty_label': 'Все населенные пункты'})
        self.filters['object_type'].extra.update({'empty_label': 'Все типы объектов'})
        self.filters['category_type'].extra.update({'empty_label': 'Все категории'})