from django.contrib import admin
from .models import ChaiVariety

# Register your models here.
admin.site.register(ChaiVariety)

def __str__(self):
    return self.name
