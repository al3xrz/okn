from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from .views import home
from .views import panel 
from .views import get_id_data
from .views import about 
from .views import feedback
from .views import contact
from .views import more_information_view
from .views import search_ajax
from .views import ObjectInfoViewSet
from .views import MunicipalityViewSet
from .views import LocalityViewSet
from .views import CategoryTypeViewSet
from .views import ObjectTypeViewSet
from .views import SpeciesViewSet
from .views import ImageViewSet


router = routers.DefaultRouter()
router.register(r'objects', ObjectInfoViewSet)
router.register(r'municipalities', MunicipalityViewSet)
router.register(r'localities', LocalityViewSet)
router.register(r'category_types', CategoryTypeViewSet)
router.register(r'object_types', ObjectTypeViewSet)
router.register(r'species', SpeciesViewSet)
router.register(r'images', ImageViewSet)


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^panel/$', panel, name='panel'),
    url(r'^get_id_data/$', get_id_data, name='get_id_data'),
    url(r'^more_information/(?P<id>\d+)/$', more_information_view, name='more_information'),
    url(r'^search_ajax_function/?$', search_ajax, name='search_ajax'),
    url(r'^about/', about, name='about'),
    url(r'^objects/(?P<id>\d+)/$', more_information_view, name='more_information'),
    url(r'^contact/(?P<id>\d+)/$', contact, name='contact'),    
    url(r'^feedback/', feedback, name='feedback'),
    # REST
    url(r'^api/', include(router.urls)),
    

]