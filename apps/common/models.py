from django.db import models
# from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

from apps.cart.models import Cart
from apps.training.models import Course, Book


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(region="UZ")

    message = models.TextField()

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(region="UZ")
    near_subway = models.CharField(max_length=125)

    # location = PlainLocationField(based_fields=['full_name'], zoom=7)

    def __str__(self):
        return self.name


class User(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    register_code = models.IntegerField()
    photo = models.ImageField(upload_to='user/', blank=True, null=True)
    order = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='user_order', null=True)
    wishlist_book = models.ManyToManyField(Book, related_name='ordered_book', blank=True)
    wishlist_course = models.ManyToManyField(Course, related_name='ordered_course', blank=True)

    def __str__(self):
        return self.name
