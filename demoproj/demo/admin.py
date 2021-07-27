from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Config, Collection

admin.site.register(Config)
admin.site.register(Collection)
