from django.contrib import admin

from .models import HotelUser

# Register your models here.

from .models import *

admin.site.register(HotelUser)
