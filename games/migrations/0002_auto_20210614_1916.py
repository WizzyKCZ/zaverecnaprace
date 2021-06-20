# Generated by Django 3.2 on 2021-06-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hra',
            name='datum_vydani',
            field=models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, verbose_name='Release date'),
        ),
        migrations.DeleteModel(
            name='Vydani',
        ),
    ]