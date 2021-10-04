# Generated by Django 2.2.20 on 2021-09-20 08:07

from django.db import migrations, models
import localized_fields.fields.char_field


def set_all_title_hstore(apps, schema_editor):
    models = [
        apps.get_model("identity", "Interest"),
        apps.get_model("identity", "HistoricalInterest"),
        apps.get_model("identity", "InterestCategory"),
        apps.get_model("identity", "HistoricalInterestCategory"),
    ]
    for model in models:
        for record in model.objects.iterator():
            record.title_hstore = {"de": record.title}
            record.save()


class Migration(migrations.Migration):

    dependencies = [
        ("identity", "0007_organisation_types"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalinterestcategory",
            name="public",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="interestcategory",
            name="public",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="interestcategory",
            name="title_hstore",
            field=localized_fields.fields.char_field.LocalizedCharField(
                blank=True, null=True, required=[]
            ),
        ),
        migrations.AddField(
            model_name="interest",
            name="title_hstore",
            field=localized_fields.fields.char_field.LocalizedCharField(
                blank=True, null=True, required=[]
            ),
        ),
        migrations.AddField(
            model_name="historicalinterestcategory",
            name="title_hstore",
            field=localized_fields.fields.char_field.LocalizedCharField(
                blank=True, null=True, required=[]
            ),
        ),
        migrations.AddField(
            model_name="historicalinterest",
            name="title_hstore",
            field=localized_fields.fields.char_field.LocalizedCharField(
                blank=True, null=True, required=[]
            ),
        ),
        migrations.RunPython(set_all_title_hstore, migrations.RunPython.noop),
        migrations.RemoveField(model_name="interest", name="title"),
        migrations.RemoveField(model_name="interestcategory", name="title"),
        migrations.RemoveField(model_name="historicalinterest", name="title"),
        migrations.RemoveField(model_name="historicalinterestcategory", name="title"),
        migrations.RenameField(
            model_name="interest", old_name="title_hstore", new_name="title"
        ),
        migrations.RenameField(
            model_name="interestcategory", old_name="title_hstore", new_name="title"
        ),
        migrations.RenameField(
            model_name="historicalinterest", old_name="title_hstore", new_name="title"
        ),
        migrations.RenameField(
            model_name="historicalinterestcategory",
            old_name="title_hstore",
            new_name="title",
        ),
        migrations.AlterField(
            model_name="interest",
            name="title",
            field=localized_fields.fields.char_field.LocalizedCharField(
                required=["de"]
            ),
        ),
        migrations.AlterField(
            model_name="interestcategory",
            name="title",
            field=localized_fields.fields.char_field.LocalizedCharField(
                required=["de"]
            ),
        ),
        migrations.AlterField(
            model_name="historicalinterest",
            name="title",
            field=localized_fields.fields.char_field.LocalizedCharField(
                required=["de"]
            ),
        ),
        migrations.AlterField(
            model_name="historicalinterestcategory",
            name="title",
            field=localized_fields.fields.char_field.LocalizedCharField(
                required=["de"]
            ),
        ),
    ]