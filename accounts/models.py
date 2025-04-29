from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class HotelUser(AbstractUser):
    
    profile_picture = models.ImageField(upload_to="profile")
    phone_number =  models.CharField(unique = True , max_length= 100)
    email_token = models.CharField(max_length = 100 ,null = True , blank=True)
    otp = models.CharField(max_length = 10 , null = True , blank = True)
    is_verified = models.BooleanField(default = False)
    groups = models.ManyToManyField(
    "auth.Group",
    related_name="hotel_users",  
    blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="hotel_users_permissions",  
        blank=True,
    )




class HotelVendor(AbstractUser):
    phone_number =  models.CharField(unique = True, max_length= 100)
    business_name = models.CharField(max_length=100, default="Default Business")
    profile_picture = models.ImageField(upload_to="profile")
    email_token = models.CharField(max_length = 100 ,null = True , blank=True)
    otp = models.CharField(max_length = 10 , null = True , blank = True)

    is_verified = models.BooleanField(default = False)
    groups = models.ManyToManyField(
    "auth.Group",
    related_name="hotel_vendors",  # Unique related_name
    blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="hotel_vendors_permissions",  # Unique related_name
        blank=True,
    )


class Amenities(models.Model):
    name = models.CharField(max_length = 1000)
    icon = models.ImageField(upload_to="hotels")

class Hotel(models.Model):
    hotel_name  = models.CharField(max_length = 100)
    hotel_description = models.TextField()
    hotel_slug = models.SlugField(max_length = 255, unique  = True)
    hotel_owner = models.ForeignKey(HotelVendor, on_delete = models.CASCADE , related_name = "hotels")
    amenities = models.ManyToManyField(Amenities)
    hotel_price = models.FloatField()
    hotel_offer_price = models.FloatField()
    hotel_location = models.TextField()
    is_active = models.BooleanField(default = True)


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE , related_name = "hotel_images")
    image = models.ImageField(upload_to="hotels")

class HotelManager(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE , related_name = "hotel_managers")
    manager_name = models.CharField(max_length = 100)
    manager_contact = models.CharField(max_length = 100)
