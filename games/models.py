from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.


class Platforma(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Název platformy",
                            help_text='Zadejte název platformy')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Firma(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Název firmy",
                            help_text='Zadejte název firmy')
    sidlo = models.CharField(max_length=50, unique=False, verbose_name="Sídlo", help_text='Zadejte sídlo firmy')
    pocet_zamestnancu = models.IntegerField(blank=True, help_text="Zadejte počet zaměstnanců")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Hra(models.Model):
    name = models.CharField(max_length=50, unique=False, verbose_name="Název hry",
                            help_text='Zadejte název hry')
    zanr = models.CharField(max_length=50, unique=False, verbose_name="Žánr",
                            help_text='Zadejte žánr hry')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")
    vydavatel = models.ManyToManyField(Firma, help_text='Vyberte vydavatele hry')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Vydani(models.Model):
    datum = models.DateField(blank=False, null=False, help_text="Zadejte datum vydání hry",verbose_name="Release date")
    hra = models.ManyToManyField(Hra, help_text='Vyberte hru která vychází tento den')
    platforma = models.ManyToManyField(Platforma, help_text='Vyberte platformu na kterou vychází hra')

    class Meta:
        ordering = ["datum"]

    def __str__(self):
        return self.name
