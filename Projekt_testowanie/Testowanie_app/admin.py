from django.contrib import admin

# Register your models here.
from .models import Osoba, Stanowisko
admin.site.register(Osoba)
admin.site.register(Stanowisko)
