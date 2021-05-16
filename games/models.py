from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


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
        ANGLICTINA = 'AN', _('Angličtina')
        CESTINA = 'CE', _('Čeština')

    jazyk = models.CharField(
        max_length=2,
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
        return f"{self.hra}"


class Recenzenti(models.Model):
    pocet_hvezd = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], null=False,
                                      help_text="Zadejte počet hvězd",verbose_name="rate")
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        ordering = ["pocet_hvezd"]

    def __str__(self):
        return self.popis


class Recenze(models.Model):
    class Role(models.TextChoices):
        UZIVATEL = 'UZ', _('Uživatel')
        REDAKCE = 'RE', _('Redakce')

    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.UZIVATEL,
    )
    prezdivka = models.CharField(max_length=50, unique=True, verbose_name="Přezdívka",
                                 help_text='Zadejte přezdívku')
    recenze = models.ManyToManyField(Recenzenti, help_text='Zadejte recenzi')
    hra = models.ManyToManyField(Hra, help_text='Vyberte hru na kterou recenze patří')

    class Meta:
        ordering = ["prezdivka"]

    def __str__(self):
        return self.prezdivka

