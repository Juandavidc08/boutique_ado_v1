# Generated by Django 5.1 on 2024-09-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
