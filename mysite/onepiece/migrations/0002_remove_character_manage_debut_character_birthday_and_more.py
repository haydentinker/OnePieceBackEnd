# Generated by Django 4.2 on 2023-05-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onepiece", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="character",
            name="manage_debut",
        ),
        migrations.AddField(
            model_name="character",
            name="birthday",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="character",
            name="affiliations",
        ),
        migrations.RemoveField(
            model_name="character",
            name="occupations",
        ),
        migrations.DeleteModel(
            name="Affiliations",
        ),
        migrations.DeleteModel(
            name="Occupations",
        ),
        migrations.AddField(
            model_name="character",
            name="affiliations",
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="character",
            name="occupations",
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
