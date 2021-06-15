from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


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

    class Jazyk(models.TextChoices):
        ANGLICTINA = 'Angličtina', _('Angličtina')
        CESTINA = 'Čeština', _('Čeština')

    jazyk = models.CharField(
        max_length=10,
        choices=Jazyk.choices,
        default=Jazyk.ANGLICTINA,
    )
    zanr = models.CharField(max_length=50, unique=False, verbose_name="Žánr",
                            help_text='Zadejte žánr hry')

    class Rating(models.TextChoices):
        E = 'E', _('E')
        SEVEN = '7', _('7')
        TWELVE = '12', _('12')
        FIFTEEN = '15', _('15')
        EIGHTEEN = '18', _('18')

    rating = models.CharField(
        max_length=2,
        choices=Rating.choices,
        default=Rating.E,
    )
    plakat = models.ImageField(upload_to='hra/plakat/%Y/%m/%d/', blank=True, null=True, verbose_name="plakat")
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")
    vydavatel = models.ManyToManyField(Firma, help_text='Vyberte vydavatele hry')
    platforma = models.ManyToManyField(Platforma, help_text='Vyberte platformu')
    datum_vydani = models.DateField(blank=True, null=True,
                                    help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                                    verbose_name="Release date")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def release_year(self):
        return self.datum_vydani.year

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o filmu"""
        return reverse('hra_detail', args=[str(self.id)])
