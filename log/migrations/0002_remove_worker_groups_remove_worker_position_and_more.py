# Generated by Django 4.1.3 on 2022-11-16 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("log", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="worker",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="worker",
            name="position",
        ),
        migrations.RemoveField(
            model_name="worker",
            name="user_permissions",
        ),
        migrations.DeleteModel(
            name="Position",
        ),
        migrations.DeleteModel(
            name="Worker",
        ),
    ]