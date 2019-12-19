from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
import uuid
from smart_selects.db_fields import ChainedForeignKey
from django.utils.safestring import mark_safe

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{}/{}'.format(instance.slug, filename)


def create_object_info_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.nativeName, 'ru', reversed=True))
        instance.slug = slug + '-'+uuid.uuid4().hex
        print(instance.slug)







class ObjectType(models.Model):
    class Meta:
        verbose_name = 'Тип объектов'
        verbose_name_plural = 'Типы объектов'
    
    name = models.CharField(
        max_length=200,
        verbose_name='Тип объекта',
    )
 
    def __str__(self):
        return self.name


class CategoryType(models.Model):
    class Meta:
        verbose_name = 'Категория объектов'
        verbose_name_plural = 'Категории объектов'
    
    name = models.CharField(
        max_length=200,
        verbose_name='Категория объекта'
    )
 
    def __str__(self):
        return self.name


class Municipality(models.Model):
    
    class Meta:
        verbose_name = 'Муниципальное образование'
        verbose_name_plural = 'Муниципальные образования'
        ordering = ('name', )

    name = models.CharField(
        max_length=200,
        verbose_name='Муниципальное образование'
    )

    def __str__(self):
        return self.name


class Locality(models.Model):

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
        ordering = ('name',)

    name = models.CharField(
        verbose_name='Населенный пункт',
        max_length=200
    )

    municipality = models.ForeignKey(
        'Municipality',
        verbose_name='Муниципальное образование',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return self.name


class Species(models.Model):

    class Meta:
        verbose_name = 'Видовая принадлежность'
        verbose_name_plural = 'Видовые принадлежности'

    name = models.CharField(
        verbose_name='Общая видовая принадлежность',
        max_length=200
    )
    
    def __str__(self):
        return self.name


class ObjectInfo(models.Model):

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    slug = models.SlugField(
        verbose_name='slugURL',
        max_length=400,
        null=True,
        blank=True
    )

    id_openData = models.CharField(
        max_length=200, 
        verbose_name='ID opendata.mkrf.ru',
        blank=True,
        null=True)

    nativeName = models.CharField(
        max_length=200,
        verbose_name='Наименование',
        blank=True,
        null=True
    )
    fullAddress = models.TextField(
        verbose_name='Полный адрес',
        blank=True,
        null=True
    )


    coordinates = models.CharField(
        max_length=200,
        verbose_name = 'Координаты',
        blank=True,
        null=True
    )

    photo_url = models.CharField(
        max_length=500,
        verbose_name = 'URL фото',
        blank=True,
        null=True
    )

    create_date = models.CharField(
        max_length=100,
        verbose_name = 'Дата создания',
        blank=True,
        null=True
    )

    object_type = models.ForeignKey(
        ObjectType,
        on_delete=models.SET_NULL,
        verbose_name='Тип объекта',
        blank=True,
        null=True
    )


    category_type = models.ForeignKey(
        CategoryType,
        on_delete=models.SET_NULL,
        verbose_name='Категория объекта',
        blank=True,
        null=True
    )

    reg_number = models.CharField(
        max_length=100,
        verbose_name='Регистрационный номер',
        blank=True,
        null=True
    )

    con_number = models.CharField(
        max_length=100,
        verbose_name = 'con_number?',
        blank=True,
        null=True
    )

    documents = models.CharField(
        max_length=300,
        verbose_name = 'Документы',
        blank=True,
        null=True
    )

    addr_NPA = models.CharField(
        max_length=300,
        verbose_name = 'Адрес в соответствии с НПА',
        blank=True,
        null=True
    )


    municipality = models.ForeignKey(
        Municipality, 
        on_delete=models.SET_NULL, 
        verbose_name='Муниципальное образование',
        blank=True,
        null=True
    )
    
    locality = ChainedForeignKey(
        Locality, 
        verbose_name='Населенный пункт',
        chained_field='municipality',
        chained_model_field='municipality',
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.SET_NULL, 
        blank=True,
        null=True,
    )
    
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

    OKN_in_ensemble = models.CharField(
        verbose_name='ОКН входит в ансамбль (да/нет)',
        choices=like_BOOLEAN,
        blank=True,
        null=True,
        max_length=10
     
    )
  

    information_sign = models.CharField(
        choices=information_CHOICES, 
        max_length=5,
        verbose_name='Наличие уcтановленной информационной надписи установленного образца',
        blank=True,
        null=True
    ) 
    information_sign_photo = models.ImageField(
        upload_to=image_folder, 
        blank=True,
        null=True,
        verbose_name='Фотография информационной надписи',

    )
    information_sign_conformity = models.CharField(
        verbose_name='Наличие информационной надписи, но не соответствующей требованиям',
        blank=True,
        null=True,
        choices=like_BOOLEAN,
        max_length=10

        
    )
    photo = models.ImageField(
        upload_to=image_folder, 
        blank=True,
        verbose_name='Фото',
        null=True
        

    )
    url = models.CharField(
        max_length=200,
        verbose_name='URL адрес',
        blank=True,
        null=True
        
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    affiliation_U = models.CharField(
        choices=like_BOOLEAN,
        verbose_name='Принадлежность к ЮНЭСКО',
        blank=True,
        null=True,
        max_length=10
        
    )
    esp_valuable_object = models.CharField(
        choices=like_BOOLEAN,
        verbose_name='Особо ценный объект',
        blank=True,
        null=True,
        max_length=10
        
    )
    requisites_and_title = models.TextField(
        verbose_name=' Реквизиты и наименование акта органа государственной власти о постановке на государственную охрану объекта культурного наследия',
        blank=True,
        null=True
    )
    owner = models.CharField(
        max_length=200,
        verbose_name='Собственник',
        blank=True,
        null=True
    )
    management = models.CharField(
        max_length=200,
        verbose_name='Под чьим управлением',
        blank=True,
        null=True
    )
    owner_contacts = models.TextField(
        verbose_name='Контактные данные собственника ОКН',
        blank=True,
        null=True
    )
    has_security_obligation = models.CharField(
        choices=information_CHOICES, 
        max_length=5,
        verbose_name='Наличие охранного обязательства ОКН',
        blank=True,
        null=True
    )
    has_passport_OKN = models.CharField(
        choices=information_CHOICES, 
        max_length=5,
        verbose_name='Наличие паспорта ОКН',
        blank=True,
        null=True
    )
    actual_address = models.TextField(
        verbose_name='Актуальный адрес',
        blank=True,
        null=True
    )
    gen_species_appearance = models.ForeignKey(
        Species, 
        on_delete=models.SET_NULL,
        verbose_name='Общая видовая принадлежность',
        blank=True,
        null=True
    )
    has_docs_boundaries = models.CharField(
        choices=like_BOOLEAN,
        verbose_name='Наличие документов о границах территории ОКН',
        blank=True,
        null=True,
        max_length=10
    )
    req_of_approval = models.TextField(
        verbose_name='Реквизиты об утверждении границ территории',
        blank=True,
        null=True
        
    )
    has_docs_of_aprroval = models.CharField(
        verbose_name='Наличие документов об утвержденых зонах охраны',
        blank=True,
        null=True,
        max_length=10,
        choices=like_BOOLEAN
    )
    document_on_approved_security = models.TextField(
        verbose_name='Документ об утвержденых зонах охраны',
        blank=True,
        null=True
    )
    has_rights = models.CharField(
        verbose_name='Наличие зарегистрированных прав/обременений',
        blank=True,
        null=True,
        max_length=10,
        choices=like_BOOLEAN
    )
    date = models.DateField(
        verbose_name='Дата',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nativeName

pre_save.connect(create_object_info_slug, sender=ObjectInfo)


def photo_path(instance, filename):
    filename = instance.objectinfo.slug + '.' + filename.split('.')[1]
    return '{}/{}'.format(instance.objectinfo.slug, filename)


class Image(models.Model):
    class Meta:
        verbose_name = 'Фотография объекта'
        verbose_name_plural = 'Фотографии объекта'
    
    objectinfo = models.ForeignKey(ObjectInfo, related_name='images')
    
    image = models.ImageField(upload_to=photo_path, max_length=500)
 
    def image_tag(self):
        return mark_safe('<br><img src="{}" style="width:200px;margin-top:5px;"/>'.format(self.image.url))
    
    image_tag.short_description = 'Список изображений'
    image_tag.allow_tags = True
   

    def __str__(self):
        return self.image.name

###################################################################################################
###################### FEEDBACK CODE ##############################################################
class Feedback(models.Model):
    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'

    o_id = models.IntegerField(
        verbose_name='ID объекта'
    )

    o_url = models.CharField(
        verbose_name='Путь к объекту',
        blank=True,
        null=True,
        max_length=200,
    )

    name = models.CharField(
        verbose_name='Имя',
        blank=True,
        null=True,
        max_length=100,
    )

    email = models.CharField(
        verbose_name='Email',
        blank=True,
        null=True,
        max_length=100,
    )

    text = models.TextField(
        verbose_name='Сообщение',
        blank=True,
        null=True
    )

    def __str__(self):
        return o_url

def photo_path_2(instance, filename):
    filename = instance.objectinfo.slug + '.' + filename.split('.')[1]
    return 'UPLOADED/{}/{}'.format(instance.feedback.o_id, filename)


class FeedbackImage(models.Model):
    class Meta:
        verbose_name = 'Загруженная фотография'
        verbose_name_plural = 'Загруженные фотографии'
    
    feedback = models.ForeignKey(Feedback, related_name='images')
    
    image = models.ImageField(upload_to=photo_path_2, max_length=500)
 
    def image_tag(self):
        return mark_safe('<br><img src="{}" style="width:200px;margin-top:5px;"/>'.format(self.image.url))
    
    image_tag.short_description = 'Список изображений'
    image_tag.allow_tags = True
   

    def __str__(self):
        return self.image.name




