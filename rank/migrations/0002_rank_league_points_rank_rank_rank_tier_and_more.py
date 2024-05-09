# Generated by Django 4.2.11 on 2024-05-06 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rank", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rank",
            name="league_points",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="rank",
            name="rank",
            field=models.CharField(default="Unranked", max_length=10),
        ),
        migrations.AddField(
            model_name="rank",
            name="tier",
            field=models.CharField(default="Unranked", max_length=30),
        ),
        migrations.AlterField(
            model_name="rank",
            name="tag",
            field=models.CharField(default="BR1", max_length=100),
        ),
        migrations.AlterField(
            model_name="rank",
            name="usuario",
            field=models.CharField(default=None, max_length=100),
        ),
    ]