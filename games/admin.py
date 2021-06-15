from django.contrib import admin
from .models import *

# Register your models here.
from django.db.models import Count
from django.utils.html import format_html

admin.site.register(Platforma)
admin.site.register(Firma)
#admin.site.register(Hra)


@admin.register(Hra)
class HraAdmin(admin.ModelAdmin):
    list_display = ("name", "datum_vydani", "zanr")

    def datum_vydani(self, obj):
        return obj.datum_vydani.year
