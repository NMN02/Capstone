# Generated by Django 5.1.1 on 2024-10-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0007_farmersprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmersprofile",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="farmersprofile",
            name="commodities",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="farmersprofile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]