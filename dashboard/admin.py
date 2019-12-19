from django.contrib import admin
from .models import ObjectType
from .models import CategoryType
from .models import Species
from .models import Image
from .models import Feedback
from .models import FeedbackImage


from .models import Municipality, ObjectInfo, Locality  
from django.contrib.admin import AdminSite
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, RelatedFieldListFilter
from django.contrib.admin.models import LogEntry
from django.contrib.admin import SimpleListFilter

from django.http import HttpResponse
import openpyxl
import csv
import datetime
from openpyxl import Workbook

from django.utils.safestring import mark_safe

#только для тестирования команды
def ExportToCsv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    responce = HttpResponse(content='text/csv')
    responce['Content-Disposition'] = 'attachment; \
        filename = Objects-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(responce, dialect='excel')
    fields = [field for field in opts.get_fields()]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            data_row.append(value)
        print(data_row)
        writer.writerow(data_row) 
    return responce

ExportToCsv.short_description = 'Экспортировать в CSV'    

def ExportToExcel(modeladmin, request, queryset):
    wb = Workbook()
    sheet = wb.active
    opts = modeladmin.model._meta
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=objects.xlsx'
    
    fields = [field for field in opts.get_fields() 
                if not field.many_to_many and not field.one_to_many and 
                field.verbose_name not in ('slugURL', 'Дата', 'ID')
    ]

    sheet.append([field.verbose_name for field in fields])
    
    
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            print(value)
            data_row.append(str(value))
        sheet.append(data_row)
        print(data_row)
        
    wb.save(response)
    return response

ExportToExcel.short_description = 'Экспортировать в Excel'








#admin.site.register(LogEntry)
admin.site.register(CategoryType)
admin.site.register(ObjectType)
admin.site.register(Species)

admin.site.site_header = 'Администрирование' 


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
        )


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
        )
    list_filter = [('municipality', RelatedDropdownFilter)]
        


"""---------------------------------------------------------------------"""



class LocalityFilter(SimpleListFilter):
    title = "Населённый пункт"
    parameter_name = "locality"
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


    def lookups(self, request, model_admin):
        if 'municipality__id__exact' in request.GET:
            # print("test")
            id = request.GET['municipality__id__exact']
            print(id)
            # locality = [obj for obj in model_admin.model.objects.all().filter(municipality=id)]
            municipality = Municipality.objects.filter(id=id)
            print(municipality, "municipality")
            locality2 = Locality.objects.filter(municipality=municipality)
            # obj1 = Locality()
            # obj1.municipality = municipality
            # obj1.name = '-'
            
        else:
            # locality = [obj for obj in model_admin.model.objects.all()]
            locality2 = Locality.objects.all()
            # obj1 = Locality()
            # obj1.name = '-'
        alist =  [(m.id, m.name) for m in locality2]
        alist.append((999999999, '-'))
        return alist

    def queryset(self, request, queryset):
        if self.value():
            if int(self.value()) == 999999999:
                return queryset.filter(locality__isnull=True)
            elif self.value():
                return queryset.filter(locality__id__exact=self.value())
        


class InlineImage(admin.TabularInline):
    model = Image
    fields = ('image', 'render_image',)
    readonly_fields = ('render_image',)

    def render_image(self, obj):
            #print('OBJECT {}'.format(obj.image.url))
            return mark_safe('<img src="%s" style="width:120px;"/>' % obj.image.url)
    
#admin.site.register(Image)

@admin.register(ObjectInfo)
class ObjectInfoAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
        )
    inlines = [InlineImage]
    actions  = [ExportToExcel]
    list_display = ('nativeName','fullAddress', 'locality', )
    #readonly_fields = ['slug']
    exclude = ['slug', 'date', 'photo',]
    
    search_fields = ['nativeName', 'description', 'fullAddress']
    list_filter = (
        # for ordinary fields
        
        #('municipality', DropdownFilter),
        #('locality', DropdownFilter),
        #('gen_species_appearance', DropdownFilter),
        
        # for related fields
        ('municipality', RelatedDropdownFilter),
        (LocalityFilter),
        # ('locality', RelatedDropdownFilter),
        ('gen_species_appearance', RelatedDropdownFilter),
        
        ('object_type', RelatedDropdownFilter), 

        #('category_type', RelatedDropdownFilter), 
        
    )

class InlineFeedbackImage(admin.TabularInline):
    model = FeedbackImage
    fields = ("image", 'render_image', )
    readonly_fields = ('render_image', )

    def render_image(self, obj):
        return mark_safe('<img src="%s" style="width:120px;"/>' % obj.image.url)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    title = 'Письма обратной связи'
    inlines = [InlineFeedbackImage]
  