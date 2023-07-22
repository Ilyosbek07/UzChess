from django.db import models
from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class SocialMedia(BaseModel):
    icon = models.FileField(upload_to='social_icon/')
    url = models.URLField()


class Gamer(BaseModel):
    full_name = models.CharField(max_length=255)
    result = models.IntegerField()
    country_icon = models.FileField(upload_to='icon/')
    category = models.ForeignKey(
        Category,
        related_name='gamer_category',
        on_delete=models.CASCADE
    )
    game_number = models.IntegerField()
    walk_number = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.full_name


class News(BaseModel):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='news/')
    description = RichTextField(config_name='awesome_ckeditor')
    view_count = models.IntegerField()
    social_media = models.ForeignKey(
        SocialMedia,
        related_name='media',
        on_delete=models.CASCADE
    )
