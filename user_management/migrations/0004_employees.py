# Generated by Django 5.1.1 on 2024-10-01 01:26

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0003_alter_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("user_management.user",),
            managers=[
                ("employee", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]