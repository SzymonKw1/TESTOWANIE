from django.db import models

#class Zawodnik(models.Model):
    #imie_i_nazwisko = models.CharField(max_length=100)
    #pozycja = models.CharField(max_length=50)
    #numer = models.IntegerField()
    #wiek = models.IntegerField()

    #def __str__(self):
    #    return f'{self.imie_i_nazwisko} ({self.numer}) - {self.pozycja}'

# Create your models here.

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, blank=False, null=False)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    PLEC_CHOICES = [
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna'),
        ('I', 'Inne'),
    ]

    imie = models.CharField(max_length=50, blank=False, null=False)
    nazwisko = models.CharField(max_length=50, blank=False, null=False)
    plec = models.CharField(max_length=1, choices=PLEC_CHOICES)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
