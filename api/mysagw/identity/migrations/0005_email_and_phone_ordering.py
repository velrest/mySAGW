# Generated by Django 2.2.20 on 2021-04-26 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("identity", "0004_fix_salutation_choices"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="email",
            options={"ordering": ("email",)},
        ),
        migrations.AlterModelOptions(
            name="phonenumber",
            options={"ordering": ("-default", "phone")},
        ),
    ]
