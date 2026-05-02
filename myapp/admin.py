from django.contrib import admin
from .models import Item,FeatureFlag

# Register your models here.
admin.site.register(Item)
admin.site.register(FeatureFlag)
