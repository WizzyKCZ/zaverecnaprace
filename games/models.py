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
                            help_text='Zadejte název Firmy')
    sidlo = models.CharField(max_length=50, unique=False, verbose_name="Sídlo", help_text='Zadejte sídlo firmy')
    pocet_zamestnancu = models.IntegerField(blank=True, help_text="Zadejte počet zaměstnanců")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
