# Generated by Django 3.2.12 on 2022-06-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_alter_productstatus_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstatus',
            name='title',
            field=models.CharField(default=1822778734, max_length=10, unique=True),
        ),
    ]
