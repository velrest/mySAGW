# Generated by Django 2.2.18 on 2021-03-15 11:59

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import localized_fields.fields.char_field
import localized_fields.fields.text_field
import mysagw.models
import phonenumber_field.modelfields
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HistoricalIdentity",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "created_at",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                (
                    "created_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                (
                    "modified_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                ("idp_id", models.CharField(db_index=True, max_length=255, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True, db_index=True, max_length=254, null=True
                    ),
                ),
                (
                    "organisation_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("is_organisation", models.BooleanField(default=False)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical identity",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalInterestCategory",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("archived", models.BooleanField(default=False)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical interest category",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalMembershipRole",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "title",
                    localized_fields.fields.char_field.LocalizedCharField(
                        required=["de"]
                    ),
                ),
                (
                    "description",
                    localized_fields.fields.text_field.LocalizedTextField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("archived", models.BooleanField(default=False)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical membership role",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Identity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "created_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "modified_by_user",
                    models.CharField(
                        blank=True, db_index=True, max_length=255, null=True
                    ),
                ),
                ("idp_id", models.CharField(max_length=255, null=True, unique=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "organisation_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("is_organisation", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("last_name", "first_name", "email"),
            },
        ),
        migrations.CreateModel(
            name="InterestCategory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("archived", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MembershipRole",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    localized_fields.fields.char_field.LocalizedCharField(
                        required=["de"]
                    ),
                ),
                (
                    "description",
                    localized_fields.fields.text_field.LocalizedTextField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("archived", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("authorized", models.BooleanField(default=False)),
                (
                    "time_slot",
                    django.contrib.postgres.fields.ranges.DateRangeField(
                        blank=True, null=True
                    ),
                ),
                ("next_election", models.DateField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("inactive", models.BooleanField(default=False)),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="identity.Identity",
                    ),
                ),
                (
                    "organisation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="members",
                        to="identity.Identity",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="memberships",
                        to="identity.MembershipRole",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("archived", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="interests",
                        to="identity.InterestCategory",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="identity",
            name="interests",
            field=models.ManyToManyField(
                blank=True, related_name="identities", to="identity.Interest"
            ),
        ),
        migrations.CreateModel(
            name="HistoricalPhoneNumber",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "description",
                    localized_fields.fields.char_field.LocalizedCharField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("default", mysagw.models.UniqueBooleanField(default=False)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="identity.Identity",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical phone number",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalMembership",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("authorized", models.BooleanField(default=False)),
                (
                    "time_slot",
                    django.contrib.postgres.fields.ranges.DateRangeField(
                        blank=True, null=True
                    ),
                ),
                ("next_election", models.DateField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
                ("inactive", models.BooleanField(default=False)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="identity.Identity",
                    ),
                ),
                (
                    "organisation",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="identity.Identity",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="identity.MembershipRole",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical membership",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalInterest",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("archived", models.BooleanField(default=False)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="identity.InterestCategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical interest",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalEmail",
            fields=[
                ("history_user_id", models.CharField(max_length=150, null=True)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "description",
                    localized_fields.fields.char_field.LocalizedCharField(
                        blank=True, null=True, required=[]
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="identity.Identity",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical email",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "description",
                    localized_fields.fields.char_field.LocalizedCharField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("default", mysagw.models.UniqueBooleanField(default=False)),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="phone_numbers",
                        to="identity.Identity",
                    ),
                ),
            ],
            options={
                "ordering": ("-default",),
                "unique_together": {("identity", "phone")},
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "description",
                    localized_fields.fields.char_field.LocalizedCharField(
                        blank=True, null=True, required=[]
                    ),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_emails",
                        to="identity.Identity",
                    ),
                ),
            ],
            options={
                "unique_together": {("identity", "email")},
            },
        ),
    ]
