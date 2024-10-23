from django.db import models

class Zawodnik(models.Model):
    imie_i_nazwisko = models.CharField(max_length=100)
    pozycja = models.CharField(max_length=50)
    numer = models.IntegerField()
    wiek = models.IntegerField()

    def __str__(self):
        return f'{self.imie_i_nazwisko} ({self.numer}) - {self.pozycja}'

# Create your models here.
