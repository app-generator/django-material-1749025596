# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
     = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Device(models.Model):

    #__Device_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)
    is_locked = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    category = models.ForeignKey(DeviceCategory, on_delete=models.CASCADE)

    #__Device_FIELDS__END

    class Meta:
        verbose_name        = _("Device")
        verbose_name_plural = _("Device")


class Productcategory(models.Model):

    #__Productcategory_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Productcategory_FIELDS__END

    class Meta:
        verbose_name        = _("Productcategory")
        verbose_name_plural = _("Productcategory")


class Product(models.Model):

    #__Product_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    purchase_price = models.IntegerField(null=True, blank=True)
    sale_price = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Slot(models.Model):

    #__Slot_FIELDS__
    quantity = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    #__Slot_FIELDS__END

    class Meta:
        verbose_name        = _("Slot")
        verbose_name_plural = _("Slot")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    quantity = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    came_from = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")


class Sensor(models.Model):

    #__Sensor_FIELDS__
    label = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    last_value = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(blank=True, null=True, default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    #__Sensor_FIELDS__END

    class Meta:
        verbose_name        = _("Sensor")
        verbose_name_plural = _("Sensor")


class Devicecategory(models.Model):

    #__Devicecategory_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Devicecategory_FIELDS__END

    class Meta:
        verbose_name        = _("Devicecategory")
        verbose_name_plural = _("Devicecategory")



#__MODELS__END
