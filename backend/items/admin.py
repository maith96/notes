from django.contrib import admin

from .models import Item, NationalID, SchoolID

# Register your models here.
admin.site.register([SchoolID, NationalID])