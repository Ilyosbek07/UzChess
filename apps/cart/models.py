from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.training.models import Course


class Cart(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()
    deliver_price = models.IntegerField()
    coupon = models.CharField(max_length=125)

    def __str__(self):
        return f"Cart for Course: {self.course.name}"


class Order(models.Model):
    name = models.CharField(max_length=125)
    phone = PhoneNumberField()
    email = models.EmailField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order')
    total = models.DecimalField(decimal_places=2)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"Order for {self.name}"
