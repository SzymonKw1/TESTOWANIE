from django.contrib import admin

# Register your models here.
from .models import Osoba, Stanowisko
admin.site.register(Osoba)
admin.site.register(Stanowisko)

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)  # Pole tylko do odczytu
